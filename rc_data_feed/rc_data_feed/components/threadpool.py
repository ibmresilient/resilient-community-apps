# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

"""Feed component implementation."""

import logging
from fnmatch import filter as fnmatch_filter
from multiprocessing.pool import ThreadPool
import traceback

from pydoc import locate
from resilient_lib import get_file_attachment
from rc_data_feed.lib.feed import FeedContext, CriticalPluginError
from rc_data_feed.lib.type_info import convert_timer_fields
from rc_data_feed.lib.constants import TIME_SERIES_PREFIX

LOG = logging.getLogger(__name__)

DEF_NUM_WORKERS = 25
POOL_RATIO = 1.0 # multiplier for number of pool threads to allow

def error_callback(err):
    LOG.error((f"Plugin error during apply_async: {str(err)}"))
    LOG.error(traceback.format_exception(type(err), err, None))

class PluginPool(object):
    _instance = None
    def __init__(self,
                 rest_client_helper,
                 num_workers,
                 options,
                 opts,
                 workspaces,
                 parallel_execution=False):

        self.rest_client_helper = rest_client_helper
        self.num_workers = num_workers if num_workers else DEF_NUM_WORKERS
        self.feed_outputs = self.build_feed_outputs(opts, options.get("feed_names"))
        self.workspaces = workspaces
        self.parallel_execution = parallel_execution
        self.pool = None
        self.timeseries = options.get("timeseries", "never")
        self.timeseries_fields = [field.strip() for field in options.get("timeseries_fields", "*").split(",")]

        if self.parallel_execution:
            # increase the number of threads for handling event messages
            thread_pool_size = int(self.num_workers*POOL_RATIO) # could be +/- num_workers
            LOG.info(f"PluginPool_Factory size: {thread_pool_size}")
            self.pool = ThreadPool(thread_pool_size)
        else:
            LOG.info("PluginPool_Factory disabled")

    @staticmethod
    def get_instance(rest_client_helper,
                     num_workers,
                     options,
                     opts,
                     workspaces,
                     parallel_execution=False):

        if not PluginPool._instance:
            PluginPool._instance = PluginPool(rest_client_helper,
                                              num_workers,
                                              options,
                                              opts,
                                              workspaces,
                                              parallel_execution=parallel_execution)
        return PluginPool._instance

    def build_feed_outputs(self, opts, feed_names):
        """
        build array of all the classes which of datastores to populate
        :param opts:
        :param feed_names:
        :return: array of datastore classes
        """
        feed_config_names = [name.strip() for name in feed_names.split(',')]

        feed_outputs = {}

        for feed_config_name in feed_config_names:
            feed_options = opts.get(feed_config_name, {})

            if not feed_options:
                LOG.error(f"feed_name: {feed_config_name} not found in app.config")
                continue

            class_name = feed_options.get("class")

            # initialize the class for this given plugin
            namespace = 'data_feeder_plugins.{ns}.{ns}.{claz}Destination'.format(ns=class_name.lower(), claz=class_name)
            LOG.debug(f"{feed_config_name}:{namespace}")
            obj = locate(namespace)

            if not obj:
                LOG.error(f"Unable to find plugin: {namespace}. Check if plugin is installed.")
                continue

            # initialize class
            feed_outputs[feed_config_name] = obj(self.rest_client_helper, feed_options)

        return feed_outputs

    def run_plugin(self, task, args):
        # support both parallel execution and serial
        if self.parallel_execution:
            _async_result = self.pool.apply_async(task, args=args, error_callback=error_callback)
        else:
            task(*args)

    def _is_workspace_valid(self, workspace, feed_name):
        result = not self.workspaces or (feed_name in self.workspaces.get(workspace, []))
        return result

    def async_send_data(self, type_name, workspace, context, payload):
        """handler for asynchronously sending data to a plugin

        :param type_name: type of incident to sync: incident, task, note, artifact, etc.
        :type type_name: str
        :param workspace: workspace for this content
        :type workspace: str
        :param context: collection of information for synchronization include the rest_client to use
        :type context: FeedContext
        :param payload: payload to feed
        :type payload: dict
        """
        item_sent = False
        failure_feeds = []
        for feed_name, feed_output in self.feed_outputs.items():
            # don't let a failure in one feed break all the rest
            try:
                if self._is_workspace_valid(workspace, feed_name):
                    LOG.info("Calling feed %s:%s for workspace: %s", feed_name, feed_output.__class__.__name__, workspace)
                    self.run_plugin(feed_output.send_data, args=(context, payload))
                    item_sent = True
            except CriticalPluginError as cerr:
                LOG.error("Critical failure in feed: %s %s. Removing plugin", feed_name, str(cerr))
                failure_feeds.append(feed_name)
            except Exception as err:
                LOG.error("Failure in feed %s %s", feed_name, err)
                error_trace = traceback.format_exc()
                LOG.error("Traceback %s", error_trace)

        if not item_sent:
            LOG.info("No feed found or failure to satisfy workspace: '%s' for %s (%s)", workspace, type_name, payload.get('id'))

        for feed_name in failure_feeds:
            del self.feed_outputs[feed_name]

    def send_data(self, type_info, inc_id, payload, is_deleted, incl_attachment_data):
        """
        perform the sync to the different datastores
        :param type_info:
        :param inc_id:
        :param rest_client:
        :param payload of incident, task, artifact, etc.:
        :param is_deleted: true/false
        :param incl_attachment_data: true/false
        :return: None
        """
        context = FeedContext(type_info, inc_id, None, is_deleted)

        type_name = type_info.get_pretty_type_name()
        # make sure the incident has a org_name
        if type_name == 'incident':
            payload['org_name'] = type_info.get_org_name(payload['org_id'])

            # collect time series information for the incident?
            if not is_deleted:
                if self.timeseries == "always" \
                    or (self.timeseries == "onclose" and payload.get("plan_status") == "C"):
                    inc_time_series = get_time_series_data(self.rest_client_helper.inst_rest_client,
                                                        inc_id,
                                                        self.timeseries_fields)
                    payload[TIME_SERIES_PREFIX] = inc_time_series

        # collect attachment data to pass on
        elif not is_deleted and incl_attachment_data \
                and type_name == 'attachment':
            try:
                # this will return a byte string
                payload['content'] = get_file_attachment(self.rest_client_helper.inst_rest_client, inc_id,
                                                         task_id=payload.get('task_id'),
                                                         attachment_id=payload['id'])
            except Exception:
                LOG.error("Unable to get attachment content for incident {0} attachment {1}".format(inc_id, payload['id']))
                payload['content'] = None
        elif not is_deleted and incl_attachment_data \
                and type_name == 'artifact' \
                and payload.get('attachment'):
            try:
                # this will return a byte string
                payload['content'] = get_file_attachment(self.rest_client_helper.inst_rest_client, inc_id,
                                                         artifact_id=payload['id'])
            except Exception as err:
                LOG.error("Unable to get artifact content for incident {0} artifact {1}".format(inc_id, payload['id']))
                payload['content'] = None

        # get the incident workspace for this data
        # reload=true will not work as type_info is the wrong object type
        if type_name == 'incident':
            workspace = type_info.get_workspace_from_id(payload['workspace'])
        else:
            workspace = type_info.get_incident_workspace(inc_id)

        self.async_send_data(type_name, workspace, context, payload)

def get_time_series_data(rest_client, inc_id, filter_list):
    """get timeseries data for an incident, extracting only the fields requested

    :param rest_client: class to make API calls back to SOAR
    :type rest_client: object
    :param inc_id: incident to collect timeseries data
    :type inc_id: str
    :param filter_list: list of fields to return timeseries data
    :type filter_list: list
    :return: list of timeseries data to return
    :rtype: list
    """
    results = rest_client.post("/timers", [inc_id])
    if results.get("entities"):
        timer_fields = results["entities"][0].get("timer_fields", [])
        # extract fields requested
        if not filter_list:
            return convert_timer_fields(timer_fields)

        # get all field names
        timer_field_dict = {timer_field.get("field_name"): timer_field for timer_field in timer_fields}

        # extract fields requested
        matches = [fnmatch_filter(timer_field_dict.keys(), filter_pattern) for filter_pattern in filter_list]
        # consolidate returned lists
        match_list = []
        for match in matches:
            match_list += match
        match_list = list(set(match_list)) # dedup list

        result = [timer_field_dict[matched_field] for matched_field in match_list if matched_field]
        return convert_timer_fields(result)

    return []
