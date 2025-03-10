# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long

"""Feed component implementation."""

import ast
import logging
import sys
import traceback

from resilient_circuits import ResilientComponent, handler, ActionMessage, is_this_a_selftest
from resilient_lib import str_to_bool, get_workflow_status
from resilient import SimpleHTTPException

from rc_data_feed.lib.type_info import FullTypeInfo, ActionMessageTypeInfo
from rc_data_feed.lib.rest_client_helper import RestClientHelper
from rc_data_feed.components.threadpool import PluginPool

LOG = logging.getLogger(__name__)
MOD_10 = 10

def _get_inc_id(payload):
    if 'incident' in payload:
        return payload['incident']['id']

    return None

def _is_incident_or_task(parent_types):
    return {'incident', 'task'}.intersection(parent_types)

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

class FeedComponent(ResilientComponent):
    """This component handles initial population of a feed and ongoing
    modifications from the associated queue."""

    DATATABLE_TYPE_ID = 8
    INCIDENT_TYPE_ID = 0
    NOTE_TYPE_ID = 2
    INC_PAGE_SIZE = 500
    SEARCH_PAGE_SIZE = 50

    """Component that ingests data"""
    def __init__(self, opts):
        super(FeedComponent, self).__init__(opts)

        try:
            self.options = opts.get("feeds", {})

            if self.options.get("feed_names") is None:
                LOG.error("No feed_names are specified")
            else:
                self.rest_client_helper = RestClientHelper(self.rest_client)

                # build the list workspaces to plugin, if present
                try:
                    self.workspaces = ast.literal_eval("{{ {0} }}".format(self.options.get("workspaces", "")))
                    LOG.info("Workspaces: %s", self.workspaces)
                except SyntaxError as e:
                    LOG.error("Unable to use workspaces. Disabling workspace filtering: %s", str(e))
                    LOG.error('Syntax: workspaces="workspaceA": "odbcfeed", "workspaceB": ["odbcfeed", "elasticfeed"]')
                    self.workspaces = {}

                self.plugin_pool = PluginPool.get_instance(self.rest_client_helper,
                                                           int(opts.get("resilient", {}).get("num_workers", 0)),
                                                           self.options,
                                                           opts,
                                                           self.workspaces,
                                                           parallel_execution=str_to_bool(self.options.get("parallel_execution", 'false')))

                # expose attachment content setting
                self.incl_attachment_data = str_to_bool(self.options.get("include_attachment_data", 'false'))

                # set the channel to receive messages
                self.channel = "actions." + self.options.get("queue", "feed_data")

                # determine the reload options to follow
                if str_to_bool(self.options.get('reload', 'false')) and not is_this_a_selftest(self):
                    query_api_method = str_to_bool(self.options.get("reload_query_api_method", 'false'))

                    reload_feeds = Reload(self.plugin_pool,
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

        # make sure the key parts of event and message exist before continuing.
        if not (event.message.get('object_type') is not None and \
                event.message.get('type_info') is not None and \
                event.message.get('operation_type') is not None):
            LOG.warning("Key fields missing in event.message. Skipped: %s", event.message)
            return

        try:
            log = logging.getLogger(__name__)
            log.info("ingesting object")

            type_info = ActionMessageTypeInfo(event.message['object_type'],
                                              event.message['type_info'],
                                              self.rest_client_helper.inst_rest_client)

            type_name = type_info.get_pretty_type_name()

            inc_id = _get_inc_id(event.message)

            is_deleted = event.message['operation_type'] == 'deleted'

            if type_info.is_data_table():
                payload = event.message['row']
            else:
                payload = event.message[type_name]

            self.plugin_pool.send_data(type_info, inc_id, payload, is_deleted, self.incl_attachment_data)

        except Exception:
            error_trace = traceback.format_exc()
            LOG.error("Traceback %s", error_trace)
            LOG.error("Failure on action %s object %s type_info %s",
                      event.message['operation_type'], event.message['object_type'], event.message['type_info'])

class Reload(object):
    def __init__(self,
                 plugin_pool,
                 reload_types,
                 query_api_method=False,
                 incl_attachment_data=False,
                 workflow_id=None):
        """

        :param plug_pool: pool for multi threading execution of the feed_outputs
        :param reload_types: comma separated list of object types to reload. datatables can be specified
        :param query_api_method:
        :param incl_attachment_data: true/false
        """
        self.plugin_pool = plugin_pool
        self.query_api_method = query_api_method
        self.incl_attachment_data = incl_attachment_data
        self.type_info_index = {}
        self.search_type_names = []
        self.datatable_search_type_names = {}
        self.workflow_id = workflow_id
        self.is_workflow_terminated = False

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

        type_list = list(self.plugin_pool.rest_client_helper.get("/types").items())
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
                                    self.plugin_pool.rest_client_helper,
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

        if not self.query_api_method and not self.is_workflow_terminated:
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

                # check if workflow is active every 10 incidents
                if not (inc_id % MOD_10) and self._is_workflow_terminated():
                    LOG.info("Playbook/workflow terminated")
                    self.is_workflow_terminated = True
                    break

                actual_min_inc_id = min(actual_min_inc_id, inc_id)
                actual_max_inc_id = max(actual_max_inc_id, inc_id)

                type_info = type_info_index[FeedComponent.INCIDENT_TYPE_ID]

                if sync_incident:
                    self.plugin_pool.send_data(type_info, inc_id, incident, False, self.incl_attachment_data)

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
            if self._is_workflow_terminated():
                LOG.info("Playbook/workflow terminated")
                self.is_workflow_terminated = True
                break

            # Handle all the other built-in types using the search endpoint (except
            # the incident type, which was already handled above.  Make sure we only
            self._populate_others_chunk(chunk, search_type_names, type_info_index)

    def _populate_others_chunk(self, chunk, search_type_names, type_info_index):
        # get data for our org.
        #
        search_input_dto = {
            'query': 'inc_id:[{0} TO {1}]'.format(chunk[0], chunk[1]),
            'types': search_type_names,
            'org_id': self.plugin_pool.rest_client_helper.get_inst_rest_client().org_id
        }

        search_results = self.plugin_pool.rest_client_helper.search(search_input_dto)
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

            self.plugin_pool.send_data(type_info, inc_id, result_data, False, self.incl_attachment_data)

    def _populate_others_query(self,
                               inc_id,
                               object_type_names,
                               type_info_index):

        try:
            for object_type in object_type_names:
                if not self.lookup.get(object_type):
                    LOG.error("Method for synchronization not found: %s", object_type)
                else:
                    try:
                        type_info = type_info_index.get(object_type, None)  # datatables will not have a type_info object at this time

                        sync_count = self.lookup[object_type](inc_id, type_info)
                        LOG.debug("inc_id: %s %s: %s", inc_id, object_type, sync_count)
                    except AttributeError:
                        LOG.error("Query error for synchronization method: %s", object_type)
        except SimpleHTTPException:
            pass


    def _query_artifact(self, inc_id, type_info):
        query = "/incidents/{}/artifacts".format(inc_id)
        item_list = self.plugin_pool.rest_client_helper.get(query)
        for item in item_list:
            self.plugin_pool.send_data(type_info, inc_id, item, False, self.incl_attachment_data)

        return len(item_list)

    def _query_milestone(self, inc_id, type_info):
        query = "/incidents/{}/milestones".format(inc_id)
        item_list = self.plugin_pool.rest_client_helper.get(query)
        for item in item_list:
            self.plugin_pool.send_data(type_info, inc_id, item, False, self.incl_attachment_data)

        return len(item_list)

    def _query_note(self, inc_id, type_info):
        query = "/incidents/{}/comments".format(inc_id)
        item_list = self.plugin_pool.rest_client_helper.get(query)
        for item in item_list:
            self.plugin_pool.send_data(type_info, inc_id, item, False, self.incl_attachment_data)

        return len(item_list)

    def _query_task(self, inc_id, type_info):
        # collect tasks and task notes
        query = "/incidents/{}/tasks?want_notes=true".format(inc_id)
        item_list = self.plugin_pool.rest_client_helper.get(query)

        # get the type for a note to use within loop
        task_note_type_info = self.type_info_index.get(FeedComponent.NOTE_TYPE_ID, None)
        for item in item_list:
            self.plugin_pool.send_data(type_info, inc_id, item, False, self.incl_attachment_data)

            # go through all the task notes
            self._process_task_notes(item.get('notes', []), task_note_type_info, inc_id)

        return len(item_list)

    def _process_task_notes(self, notes_list, task_note_type_info, inc_id):
        # go through all the task notes
        for note in notes_list:
            self.plugin_pool.send_data(task_note_type_info, inc_id, note, False, self.incl_attachment_data)
            # children notes?
            self._process_task_notes(note.get('children', []), task_note_type_info, inc_id)

    def _query_task_note(self, inc_id, task_id, type_info):
        query = "/tasks/{}/comments".format(task_id)
        item_list = self.plugin_pool.rest_client_helper.get(query)
        for item in item_list:
            self.plugin_pool.send_data(type_info, inc_id, item, False, self.incl_attachment_data)


    def _query_attachment(self, inc_id, type_info):
        query = "/incidents/{}/attachments/query?include_tasks=true".format(inc_id)
        item_list = self.plugin_pool.rest_client_helper.post(query, None)
        for item in item_list['attachments']:
            self.plugin_pool.send_data(type_info, inc_id, item, False, self.incl_attachment_data)

        return len(item_list)

    def _query_datatable(self, inc_id, type_info):
        query = "/incidents/{}/table_data".format(inc_id)
        item_list = self.plugin_pool.rest_client_helper.get(query)
        for _, table in item_list.items():
            datatable_id = table['id']
            # only sync datatables expressed in app.config
            if datatable_id in self.datatable_search_type_names:
                # We need the ID of the table, not the ID for the generic "datatable" type.
                type_info = self.type_info_index[datatable_id]

                for row in table['rows']:
                    self.plugin_pool.send_data(type_info, inc_id, row, False, self.incl_attachment_data)

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

        paged_results = self.plugin_pool.rest_client_helper.post(url, query)

        while paged_results.get('data'):
            data = paged_results.get('data')

            for result in data:
                if result['id'] <= max_inc_id:
                    yield result

            query['start'] = len(data) + query['start']

            paged_results = self.plugin_pool.rest_client_helper.post(url, query)

    def _is_workflow_terminated(self) -> bool:
        """determine if the workflow is still active or we should abort

        :return: True if the workflow as been cancelled
        :rtype: bool
        """
        if not self.workflow_id:
            return False

        workflow_status = get_workflow_status(self.plugin_pool.rest_client_helper, self.workflow_id)
        return workflow_status.is_terminated
