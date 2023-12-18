# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

"""Feed component implementation."""

import logging
import multiprocessing
import traceback

from pydoc import locate
from resilient_lib import get_file_attachment
from rc_data_feed.lib.feed import FeedContext

LOG = logging.getLogger(__name__)

DEF_NUM_WORKERS = 25
POOL_RATIO = 1.0 # multiplier for number of pool threads to allow

def error_callback(exception):
    LOG.error((f"Plugin error during apply_async: {str(exception)}"))

class PluginPool_Factory():
    thread_pool = None

    @staticmethod
    def get_thread_pool(rest_client_helper,
                        num_workers,
                        feed_outputs,
                        opts,
                        workspaces,
                        parallel_execution=False):
        if not PluginPool_Factory.thread_pool:
            PluginPool_Factory.thread_pool = PluginPool(rest_client_helper,
                                                        num_workers,
                                                        feed_outputs,
                                                        opts,
                                                        workspaces,
                                                        parallel_execution=parallel_execution)

        return PluginPool_Factory.thread_pool

class PluginPool():
    """This class allows for separate, long running threads to perform the plugin logic.
        It frees up the application threads to service other message queue actions
    """
    def __init__(self,
                 rest_client_helper,
                 num_workers,
                 feed_list,
                 opts,
                 workspaces,
                 parallel_execution=False):
        self.rest_client_helper = rest_client_helper
        self.num_workers = num_workers if num_workers else DEF_NUM_WORKERS
        self.feed_outputs = self.build_feed_outputs(opts, feed_list)
        self.workspaces = workspaces
        self.parallel_execution = parallel_execution
        self.pool = None

        if self.parallel_execution:
            # increase the number of threads for handling event messages
            thread_pool_size = int(self.num_workers*POOL_RATIO) # could be +/- num_workers
            LOG.info(f"PluginPool_Factory size: {thread_pool_size}")
            self.pool = multiprocessing.Pool(thread_pool_size)
        else:
            LOG.info("PluginPool_Factory disabled")

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

            class_name = feed_options.get("class")

            namespace = 'data_feeder_plugins.{ns}.{ns}.{claz}Destination'.format(ns=class_name.lower(), claz=class_name)
            LOG.debug(namespace)
            obj = locate(namespace)(self.rest_client_helper, feed_options)

            feed_outputs[feed_config_name] = obj

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
        for feed_name, feed_output in self.feed_outputs.items():
            # don't let a failure in one feed break all the rest
            try:
                if self._is_workspace_valid(workspace, feed_name):
                    LOG.info("Calling feed %s for workspace: %s", feed_output.__class__.__name__, workspace)
                    self.run_plugin(feed_output.send_data, args=(context, payload))
                    item_sent = True
            except Exception as err:
                LOG.error("Failure in update to %s %s", feed_output.__class__.__name__, err)
                error_trace = traceback.format_exc()
                LOG.error("Traceback %s", error_trace)

        if not item_sent:
            LOG.info("No feed found to satisfy workspace: '%s' for %s (%s)", workspace, type_name, payload.get('id'))


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

        # collect attachment data to pass on
        elif not is_deleted and incl_attachment_data \
                and type_name == 'attachment':
            try:
                # this will return a byte string
                payload['content'] = get_file_attachment(self.rest_client_helper.inst_rest_client, inc_id,
                                                         task_id=payload.get('task_id'),
                                                         attachment_id=payload['id'])
            except Exception as err:
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
