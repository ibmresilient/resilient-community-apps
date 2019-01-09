# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Feed component implementation"""


from rc_data_feed.lib.file_feed import FileFeedDestination
from rc_data_feed.lib.sqlite_feed import SqliteFeedDestination
from rc_data_feed.lib.odbc_feed import ODBCFeedDestination
from rc_data_feed.lib.type_info import FullTypeInfo, SimpleTypeInfo
from rc_data_feed.lib.feed import FeedContext

from resilient_circuits import ResilientComponent, handler, ActionMessage

import logging
import sys


logger = logging.getLogger(__name__)


def _get_inc_id(payload):
    if 'incident' in payload:
        return payload['incident']['id']

    return None


class FeedComponent(ResilientComponent):
    DATATABLE_TYPE_ID = 8
    INCIDENT_TYPE_ID = 0
    INC_PAGE_SIZE = 500
    SEARCH_PAGE_SIZE = 50
    AVAILABLE_CLASSES = {
        "ODBCFeed": ODBCFeedDestination,
        "FileFeed": FileFeedDestination,
        "SQLiteFeed": SqliteFeedDestination
    }

    """Component that ingests data"""
    def __init__(self, opts):
        super(FeedComponent, self).__init__(opts)

        self.options = opts.get("feeds", {})
        logger.debug(self.options)

        self.channel = "actions." + self.options.get("queue", "feed_data")

        feed_config_names = [name.strip() for name in self.options.get("feed_names").split(',')]

        self.feed_outputs = list()

        for feed_config_name in feed_config_names:
            feed_options = opts.get(feed_config_name, {})

            class_name = feed_options.get("class")

            obj = FeedComponent.AVAILABLE_CLASSES[class_name](self.rest_client(), feed_options)

            self.feed_outputs.append(obj)

        if bool(self.options.get('reload', False)):
            self._reload_all()

    @handler()
    def _feed_ingest_data(self, event, *args, **kwargs):
        """Ingests data of any type that can be sent to a Resilient message destination"""
        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        log = logging.getLogger(__name__)
        log.info("ingesting object")

        type_info = SimpleTypeInfo(event.message['object_type'], event.message['type_info'], self.rest_client())

        type_name = type_info.get_pretty_type_name()

        inc_id = _get_inc_id(event.message)

        is_deleted = 'deleted' == event.message['operation_type']

        context = FeedContext(type_info, inc_id, self.rest_client(), is_deleted)

        if type_info.is_data_table():
            payload = event.message['row']
        else:
            payload = event.message[type_name]

        for feed_output in self.feed_outputs:
            feed_output.send_data(context, payload)

    def _reload_all(self):
        rest_client = self.rest_client()

        # We want to search all of the types that have incident or task as a parent.
        type_info_index = {}
        search_type_names = ['datatable']

        for (type_name, type_dto) in list(rest_client.get("/types").items()):
            parent_types = set(type_dto['parent_types'])

            if type_name == 'incident' or len(set(['incident', 'task']).intersection(parent_types)) > 0:
                id = type_dto['id']
                name = type_dto['type_name']
                type_id = type_dto['type_id']

                info = FullTypeInfo(id, rest_client, refresh=False, all_fields=list(type_dto['fields'].values()))

                # Index by both name and ID.
                type_info_index[id] = info
                type_info_index[name] = info

                if type_id != FeedComponent.DATATABLE_TYPE_ID and type_id != FeedComponent.INCIDENT_TYPE_ID:
                    search_type_names.append(name)

        max_inc_id, min_inc_id = self._populate_incidents(rest_client, type_info_index)

        self._populate_others(rest_client, max_inc_id, min_inc_id, search_type_names, type_info_index)

    def _populate_incidents(self, rest_client, type_info_index):
        min_inc_id = sys.maxsize
        max_inc_id = 0

        try:
            for incident in self._page_incidents(rest_client):
                inc_id = incident['id']

                min_inc_id = min(min_inc_id, inc_id)
                max_inc_id = max(max_inc_id, inc_id)

                type_info = type_info_index[FeedComponent.INCIDENT_TYPE_ID]

                incident_context = FeedContext(type_info, inc_id, rest_client, is_deleted=False)

                # Handle the incident data.
                for feed_output in self.feed_outputs:
                    feed_output.send_data(incident_context, incident)

        except StopIteration:
            pass

        return max_inc_id, min_inc_id

    def _populate_others(self, rest_client, max_inc_id, min_inc_id, search_type_names, type_info_index):
        for r in FeedComponent._range_chunks(min_inc_id, max_inc_id, FeedComponent.SEARCH_PAGE_SIZE):
            # Handle all the other built-in types using the search endpoint (except the incident type, which was already
            # handled above.  Make sure we only get data for our org.
            search_input_dto = {
                'query': 'inc_id:[{0} TO {1}]'.format(r[0], r[1]),
                'types': search_type_names,
                'org_id': rest_client.org_id
            }

            for result in rest_client.search(search_input_dto)['results']:
                # We're not consistent about returning IDs vs names of types.  The search
                # results are returning the type name (even though it's called "type_id").
                type_name = result['type_id']

                result_data = result['result']

                if type_name == 'datatable':
                    # We need the ID of the table, not the ID for the generic "datatable" type.
                    type_id = result_data['type_id']
                    type_info = type_info_index[type_id]
                else:
                    type_info = type_info_index[type_name]

                inc_id = result['inc_id']

                context = FeedContext(type_info, inc_id, rest_client, is_deleted=False)

                for feed_output in self.feed_outputs:
                    feed_output.send_data(context, result_data)

    @staticmethod
    def _page_incidents(rest_client):
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

        url = '/incidents/query_paged?return_level=normal'

        paged_results = rest_client.post(url, query)

        while len(paged_results.get('data')) > 0:
            data = paged_results.get('data')

            for result in data:
                yield result

            query['start'] = len(data) + query['start']

            paged_results = rest_client.post(url, query)

    @staticmethod
    def _range_chunks(in_min, in_max, chunk_size):
        start = in_min - 1

        while start <= in_max:
            yield (start + 1, min(in_max, start + chunk_size))

            start += chunk_size
