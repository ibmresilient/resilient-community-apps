# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""Feed component implementation."""

import ast
import logging
import sys
import traceback

from pydoc import locate
from resilient_circuits import ResilientComponent, handler, ActionMessage
from resilient_lib import str_to_bool, get_file_attachment
from resilient import SimpleHTTPException


from rc_data_feed.lib.type_info import FullTypeInfo, ActionMessageTypeInfo, get_incident
from rc_data_feed.lib.feed import FeedContext
from rc_data_feed.lib.rest_client_helper import RestClientHelper

LOG = logging.getLogger(__name__)

def _get_inc_id(payload):
    if 'incident' in payload:
        return payload['incident']['id']

    return None

def _is_incident_or_task(parent_types):
    return {'incident', 'task'}.intersection(parent_types)

def build_feed_outputs(rest_client_helper, opts, feed_names):
    """
    build array of all the classes which of datastores to populate
    :param rest_client_helper:
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
        obj = locate(namespace)(rest_client_helper, feed_options)

        feed_outputs[feed_config_name] = obj

    return feed_outputs

def range_chunks(chunk_range, chunk_size):
    """
    build array of lists to break the queries into smaller chunks
    :param chunk_range:
    :param chunk_size:
    :return:
    """
    if isinstance(chunk_range, list):
        start = chunk_range[0]-1
        stop = chunk_range[-1]
    else:
        start = chunk_range.start - 1
        stop = chunk_range.stop

    while start <= stop:
        yield (start + 1, min(stop, start + chunk_size))

        start += chunk_size

def send_data(type_info, inc_id, rest_client_helper, payload,\
              feed_outputs, workspaces, is_deleted, incl_attachment_data):
    """
    perform the sync to the different datastores
    :param type_info:
    :param inc_id:
    :param rest_client:
    :param payload of incident, task, artifact, etc.:
    :param feed_outputs:
    :param workspaces: mapping of workspace to feeds
    :param is_deleted: true/false
    :param incl_attachment_data: true/false
    :return: None
    """
    context = FeedContext(type_info, inc_id, rest_client_helper.inst_rest_client, is_deleted)

    type_name = type_info.get_pretty_type_name()
    # make sure the incident has a org_name
    if type_name == 'incident':
        payload['org_name'] = type_info.get_org_name(payload['org_id'])

    # collect attachment data to pass on
    elif not is_deleted and incl_attachment_data \
            and type_name == 'attachment':
        # this will return a byte string
        payload['content'] = get_file_attachment(rest_client_helper.inst_rest_client, inc_id,
                                                 task_id=payload.get('task_id'),
                                                 attachment_id=payload['id'])
    elif not is_deleted and incl_attachment_data \
            and type_name == 'artifact' \
            and payload.get('attachment'):
        # this will return a byte string
        payload['content'] = get_file_attachment(rest_client_helper.inst_rest_client, inc_id,
                                                 artifact_id=payload['id'])

    # get the incident workspace for this data
    # reload=true will not work as type_info is the wrong object type
    if type_name == 'incident':
        workspace = type_info.get_workspace_from_id(payload['workspace'])
    else:
        workspace = type_info.get_incident_workspace(inc_id)

    item_sent = False
    for feed_name, feed_output in feed_outputs.items():
        # don't let a failure in one feed break all the rest
        try:
            if not workspaces or (workspace in workspaces and feed_name in workspaces[workspace]):
                LOG.debug("Calling feed %s for workspace: %s", feed_output.__class__.__name__, workspace)
                feed_output.send_data(context, payload)
                item_sent = True
        except Exception as err:
            LOG.error("Failure in update to %s %s", feed_output.__class__.__name__, err)
            error_trace = traceback.format_exc()
            LOG.error("Traceback %s", error_trace)

    if not item_sent:
        LOG.debug("No workspace found to satisfy data feed for %s (%s)", type_name, payload.get('id'))

class FeedComponent(ResilientComponent):
    """This component handles initial population of a feed and ongoing
    modifications from the associated queue."""

    DATATABLE_TYPE_ID = 8
    INCIDENT_TYPE_ID = 0
    INC_PAGE_SIZE = 500
    SEARCH_PAGE_SIZE = 50

    """Component that ingests data"""
    def __init__(self, opts):
        super(FeedComponent, self).__init__(opts)

        try:
            self.options = opts.get("feeds", {})

            self.channel = "actions." + self.options.get("queue", "feed_data")

            if self.options.get("feed_names") is None:
                LOG.error("No feed_names are specified")
            else:
                rest_client_helper = RestClientHelper(self.rest_client)

                self.feed_outputs = build_feed_outputs(rest_client_helper, opts, self.options.get("feed_names", None))
                # build the list workspaces to plugin, if present
                try:
                    self.workspaces = ast.literal_eval("{{ {0} }}".format(self.options.get("workspaces", "")))
                    LOG.info("Workspaces: %s", self.workspaces)
                except SyntaxError as e:
                    LOG.error("Unable to use workspaces. Disabling workspace filtering: %s", str(e))
                    LOG.error('Syntax: workspaces="workspaceA": "odbcfeed", "workspaceB": ["odbcfeed", "elasticfeed"]')
                    self.workspaces = {}

                # expose attachment content setting
                self.incl_attachment_data = str_to_bool(self.options.get("include_attachment_data", 'false'))

                # determine the reload options to follow
                if str_to_bool(self.options.get('reload', 'false')):
                    query_api_method = str_to_bool(self.options.get("reload_query_api_method", 'false'))

                    reload_feeds = Reload(rest_client_helper, self.feed_outputs, self.workspaces,
                                    [ type.strip() for type in self.options.get("reload_types", "").split(",") \
                                        if type ],
                                    query_api_method=query_api_method,
                                    incl_attachment_data=self.incl_attachment_data)
                    reload_feeds.reload_all()

        except Exception as err:
            LOG.error("exception: %s", err)
            error_trace = traceback.format_exc()
            LOG.error("Traceback %s", error_trace)

    @handler()
    def _feed_ingest_data(self, event, *args, **kwargs):    # pylint: disable=unused-argument
        """Ingests data of any type that can be sent to a Resilient message destination"""
        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        try:
            log = logging.getLogger(__name__)
            log.info("ingesting object")
            rest_client_helper = RestClientHelper(self.rest_client)

            type_info = ActionMessageTypeInfo(event.message['object_type'],
                                              event.message['type_info'],
                                              rest_client_helper.inst_rest_client)

            type_name = type_info.get_pretty_type_name()

            inc_id = _get_inc_id(event.message)

            is_deleted = event.message['operation_type'] == 'deleted'

            if type_info.is_data_table():
                payload = event.message['row']
            else:
                payload = event.message[type_name]

            send_data(type_info, inc_id, rest_client_helper, payload,
                      self.feed_outputs, self.workspaces, is_deleted, self.incl_attachment_data)

        except Exception as err:
            error_trace = traceback.format_exc()
            LOG.error("Traceback %s", error_trace)
            LOG.error("Failure on action %s object %s type_info %s",
                      event.message['operation_type'], event.message['object_type'], event.message['type_info'])


class Reload(object):
    def __init__(self, rest_client_helper, feed_outputs, workspaces, \
                 reload_types,
                 query_api_method=False, incl_attachment_data=False):
        """

        :param rest_client: not the instance as we may need to refresh the client at a later point
        :param feed_outputs: dict of plugins installed: { 'feed_name': plugin_object }
        :param workspace: dict of workspaces and the feeds to use: { 'workspace': ['workspaceA', 'workspaceB'] }
        :param reload_types: comma separated list of object types to reload. datatables can be specified
        :param query_api_method:
        :param incl_attachment_data: true/false
        """
        self.rest_client_helper = rest_client_helper
        self.feed_outputs = feed_outputs
        self.workspaces = workspaces
        self.query_api_method = query_api_method
        self.incl_attachment_data = incl_attachment_data
        self.type_info_index = {}
        self.search_type_names = []
        self.datatable_search_type_names = {}

        self.lookup = {
            "attachment": self._query_attachment,
            "artifact": self._query_artifact,
            "datatable": self._query_datatable,
            "milestone": self._query_milestone,
            "note": self._query_note,
            "task": self._query_task,
            "__emailmessage": None
        }

        self.init_type_info(reload_types)

    def init_type_info(self, reload_types):
        # We want to search all of the types that have incident or task as a parent.

        type_list = list(self.rest_client_helper.get("/types").items())
        # sync everything if nothing specified from app.config
        if not reload_types:
            reload_types = [type_name for (type_name, _type_dto) in type_list]

        for (type_name, type_dto) in type_list:
            parent_types = set(type_dto['parent_types'])

            if type_name == 'incident' or _is_incident_or_task(parent_types):
                real_id = type_dto['id']
                name = type_dto['type_name']
                type_id = type_dto['type_id']

                info = FullTypeInfo(real_id,
                                    self.rest_client_helper,
                                    refresh=False,
                                    all_fields=list(type_dto['fields'].values()))

                # Index by both name and ID.
                self.type_info_index[real_id] = info
                self.type_info_index[name] = info

                if type_name in reload_types:
                    # datatables all have the same type_id, so need to capture the specific table name
                    if type_id == FeedComponent.DATATABLE_TYPE_ID:
                        self.search_type_names.append('datatable')
                        self.datatable_search_type_names[real_id] = type_dto['display_name']
                    else:
                        self.search_type_names.append(type_name)

        self.search_type_names = list(dict.fromkeys(self.search_type_names))  # dedup list
        LOG.info("reload_types allowed: %s", self.search_type_names)
        LOG.info("reload_types datatables allowed: %s", self.datatable_search_type_names)

    def reload_all(self, min_inc_id=0, max_inc_id=sys.maxsize):
        """
        load incidents and related notes, tasks, artifacts, etc based on min and max values
        :param min_inc_id: defaults to 0 for all incidents
        :param max_inc_id: defaults to max number for all incidents
        :return: # of incidents sync'd
        """

        # get the actual min and max values
        actual_max_inc_id, actual_min_inc_id = self._populate_incidents(self.type_info_index,
                                                                            min_inc_id,
                                                                            max_inc_id,
                                                                            self.query_api_method,
                                                                            ('incident' in self.search_type_names))

        if not self.query_api_method:
            rng = range(actual_min_inc_id, actual_max_inc_id)
            self._populate_others(rng,
                                  [search_type for search_type in self.search_type_names if search_type != 'incident'],
                                  self.type_info_index)

        return 0 if actual_max_inc_id == 0 else (actual_max_inc_id - actual_min_inc_id) + 1

    def _populate_incidents(self, type_info_index, min_inc_id, max_inc_id, query_api_method, sync_incident):
        """
        :param type_info_index:
        :param min_inc_id:
        :param max_inc_id:
        :param query_api_method:
        :param sync_incident: boolean to send incident to plugins
        :return:
        """
        actual_min_inc_id = sys.maxsize
        actual_max_inc_id = 0

        try:
            for incident in self._page_incidents(min_inc_id, max_inc_id):
                inc_id = incident['id']

                actual_min_inc_id = min(actual_min_inc_id, inc_id)
                actual_max_inc_id = max(actual_max_inc_id, inc_id)

                type_info = type_info_index[FeedComponent.INCIDENT_TYPE_ID]

                if sync_incident:
                    send_data(type_info, inc_id, self.rest_client_helper, incident,
                              self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

                # query api call should be done now
                if query_api_method:
                    self._populate_others_query(inc_id,
                                                [search_type for search_type in self.search_type_names if search_type != 'incident'],
                                                self.type_info_index)

        except StopIteration:
            pass

        return actual_max_inc_id, actual_min_inc_id

    def _populate_others(self,
                         inc_range,
                         search_type_names,
                         type_info_index):
        for chunk in range_chunks(inc_range, FeedComponent.SEARCH_PAGE_SIZE):
            # Handle all the other built-in types using the search endpoint (except
            # the incident type, which was already handled above.  Make sure we only
            self._populate_others_chunk(chunk, search_type_names, type_info_index)

    def _populate_others_chunk(self, chunk, search_type_names, type_info_index):
        # get data for our org.
        #
        search_input_dto = {
            'query': 'inc_id:[{0} TO {1}]'.format(chunk[0], chunk[1]),
            'types': search_type_names,
            'org_id': self.rest_client_helper.get_inst_rest_client().org_id
        }

        search_results = self.rest_client_helper.search(search_input_dto)
        for result in search_results['results']:
            # We're not consistent about returning IDs vs names of types.  The search
            # results are returning the type name (even though it's called "type_id").
            type_name = result['type_id']

            result_data = result['result']

            if type_name == 'datatable':
                # skip any datatable not intended to sync
                if result['obj_name'] not in self.datatable_search_type_names.values():
                    continue

                # We need the ID of the table, not the ID for the generic "datatable" type.
                type_id = result_data['type_id']
                type_info = type_info_index[type_id]
            else:
                type_info = type_info_index[type_name]

            inc_id = result['inc_id']

            send_data(type_info, inc_id, self.rest_client_helper, result_data,
                      self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

    def _populate_others_query(self,
                               inc_id,
                               object_type_names,
                               type_info_index):

        # ensure the incident is found
        try:
            _incident = get_incident(self.rest_client_helper, inc_id)
            for object_type in object_type_names:
                if not self.lookup.get(object_type):
                    LOG.error("Method for synchronization not found: %s", object_type)
                else:
                    try:
                        type_info = type_info_index.get(object_type, None)  # datatables will not have a type_info object at this time

                        sync_count = self.lookup[object_type](self.rest_client_helper, inc_id, type_info)
                        LOG.debug("inc_id: %s %s: %s", inc_id, object_type, sync_count)
                    except AttributeError:
                        LOG.error("Query error for synchronization method: %s", object_type)
        except SimpleHTTPException:
            pass


    def _query_artifact(self, rest_client_helper, inc_id, type_info):
        query = "/incidents/{}/artifacts".format(inc_id)
        item_list = rest_client_helper.get(query)
        for item in item_list:
            send_data(type_info, inc_id, rest_client_helper,
                      item, self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

        return len(item_list)

    def _query_milestone(self, rest_client_helper, inc_id, type_info):
        query = "/incidents/{}/milestones".format(inc_id)
        item_list = rest_client_helper.get(query)
        for item in item_list:
            send_data(type_info, inc_id, rest_client_helper, item,
                      self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

        return len(item_list)

    def _query_note(self, rest_client_helper, inc_id, type_info):
        query = "/incidents/{}/comments".format(inc_id)
        item_list = rest_client_helper.get(query)
        for item in item_list:
            send_data(type_info, inc_id, rest_client_helper, item,
            self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

        return len(item_list)

    def _query_task(self, rest_client_helper, inc_id, type_info):
        query = "/incidents/{}/tasks".format(inc_id)
        item_list = rest_client_helper.get(query)
        for item in item_list:
            send_data(type_info, inc_id, rest_client_helper, item,
                      self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

        return len(item_list)

    def _query_attachment(self, rest_client_helper, inc_id, type_info):
        query = "/incidents/{}/attachments/query?include_tasks=true".format(inc_id)
        item_list = rest_client_helper.post(query, None)
        for item in item_list['attachments']:
            send_data(type_info, inc_id, rest_client_helper, item,
                      self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

        return len(item_list)

    def _query_datatable(self, rest_client_helper, inc_id, type_info):
        query = "/incidents/{}/table_data".format(inc_id)
        item_list = rest_client_helper.get(query)
        for _, table in item_list.items():
            datatable_id = table['id']
            # only sync datatables expressed in app.config
            if datatable_id in self.datatable_search_type_names.keys():
                # We need the ID of the table, not the ID for the generic "datatable" type.
                type_info = self.type_info_index[datatable_id]

                for row in table['rows']:
                    send_data(type_info, inc_id, rest_client_helper, row,
                            self.feed_outputs, self.workspaces, False, self.incl_attachment_data)

        return len(item_list)


    def _page_incidents(self, min_inc_id, max_inc_id):
        query = {
            'start': 0,
            'length': FeedComponent.INC_PAGE_SIZE,
            'sorts': [
                {
                    'field_name': 'id',
                    'type': 'asc'
                }
            ]
        }

        conditions = []

        if min_inc_id:
            condition = {
                    "method": "gte",
                    "field_name": "id",
                    "value": min_inc_id
            }
            conditions.append(condition)

        if conditions:
            query['filters'] = [{
                "conditions": conditions
            }]

        LOG.debug("query filter: %s", query)
        url = '/incidents/query_paged?return_level=full'

        paged_results = self.rest_client_helper.post(url, query)

        while paged_results.get('data'):
            data = paged_results.get('data')

            for result in data:
                if result['id'] <= max_inc_id:
                    yield result

            query['start'] = len(data) + query['start']

            paged_results = self.rest_client_helper.post(url, query)
