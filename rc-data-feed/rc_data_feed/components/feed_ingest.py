"""Feed component implementation."""

import logging
import sys

from resilient_circuits import ResilientComponent, handler, ActionMessage

from rc_data_feed.lib.file_feed import FileFeedDestination
from rc_data_feed.lib.sqlite_feed import SqliteFeedDestination
from rc_data_feed.lib.odbc_feed import ODBCFeedDestination
from rc_data_feed.lib.elastic_feed import ElasticFeedDestination
from rc_data_feed.lib.splunk_hec_feed import SplunkHECFeedDestination
from rc_data_feed.lib.type_info import FullTypeInfo, ActionMessageTypeInfo
from rc_data_feed.lib.feed import FeedContext


LOG = logging.getLogger(__name__)


def _get_inc_id(payload):
    if 'incident' in payload:
        return payload['incident']['id']

    return None


def _is_incident_or_task(parent_types):
    return {'incident', 'task'}.intersection(parent_types)


class FeedComponent(ResilientComponent):
    """This component handles initial population of a feed and ongoing
    modifications from the associated queue."""

    DATATABLE_TYPE_ID = 8
    INCIDENT_TYPE_ID = 0
    INC_PAGE_SIZE = 500
    SEARCH_PAGE_SIZE = 50
    AVAILABLE_CLASSES = {
        "ODBCFeed": ODBCFeedDestination,
        "FileFeed": FileFeedDestination,
        "ElasticFeed": ElasticFeedDestination,
        "SQLiteFeed": SqliteFeedDestination,
        "SplunkHECFeed": SplunkHECFeedDestination
    }

    """Component that ingests data"""
    def __init__(self, opts):
        super(FeedComponent, self).__init__(opts)

        try:
            self.options = opts.get("feeds", {})
            LOG.debug(self.options)

            self.channel = "actions." + self.options.get("queue", "feed_data")

            if self.options.get("feed_names") is None:
                LOG.error("No feed_names are specified")
            else:
                feed_config_names = [name.strip() for name in self.options.get("feed_names", None).split(',')]

                self.feed_outputs = list()

                for feed_config_name in feed_config_names:
                    feed_options = opts.get(feed_config_name, {})

                    class_name = feed_options.get("class")

                    if FeedComponent.AVAILABLE_CLASSES.get(class_name) is None:
                        LOG.error("Incorrect feed class %s, skipping", class_name)

                    else:
                        obj = FeedComponent.AVAILABLE_CLASSES[class_name](self.rest_client(), feed_options)

                        self.feed_outputs.append(obj)

                if self.options.get('reload', 'false').lower() == 'true':
                    self._reload_all()

        except Exception as err:
            LOG.error("exception: %s", err)

    @handler()
    def _feed_ingest_data(self, event, *args, **kwargs):    # pylint: disable=unused-argument
        """Ingests data of any type that can be sent to a Resilient message destination"""
        if not isinstance(event, ActionMessage):
            # Some event we are not interested in
            return

        try:
            log = logging.getLogger(__name__)
            log.info("ingesting object")

            type_info = ActionMessageTypeInfo(event.message['object_type'],
                                              event.message['type_info'],
                                              self.rest_client())

            type_name = type_info.get_pretty_type_name()

            inc_id = _get_inc_id(event.message)

            is_deleted = event.message['operation_type'] == 'deleted'

            context = FeedContext(type_info, inc_id, self.rest_client(), is_deleted)

            if type_info.is_data_table():
                payload = event.message['row']
            else:
                payload = event.message[type_name]

            for feed_output in self.feed_outputs:
                # don't let a failure in one feed break all the rest
                try:
                    feed_output.send_data(context, payload)
                except Exception as err:
                    LOG.error("Failure in update to %s %s", feed_output.__class__.__name__, err)

        except Exception as err:
            LOG.error("Failure on action %s object %s type_info %s",
                      event.message['operation_type'], event.message['object_type'], event.message['type_info'])

    def _reload_all(self):
        rest_client = self.rest_client()

        LOG.debug("reload all")

        # We want to search all of the types that have incident or task as a parent.
        type_info_index = {}
        search_type_names = ['datatable']

        for (type_name, type_dto) in list(rest_client.get("/types").items()):
            parent_types = set(type_dto['parent_types'])

            if type_name == 'incident' or _is_incident_or_task(parent_types):
                real_id = type_dto['id']
                name = type_dto['type_name']
                type_id = type_dto['type_id']

                info = FullTypeInfo(real_id,
                                    rest_client,
                                    refresh=False,
                                    all_fields=list(type_dto['fields'].values()))

                # Index by both name and ID.
                type_info_index[real_id] = info
                type_info_index[name] = info

                if type_id not in [FeedComponent.DATATABLE_TYPE_ID, FeedComponent.INCIDENT_TYPE_ID]:
                    search_type_names.append(name)

        max_inc_id, min_inc_id = self._populate_incidents(rest_client, type_info_index)

        rng = range(min_inc_id, max_inc_id)

        if (len(rng) > 0):
            self._populate_others(rest_client,
                                  rng,
                                  search_type_names,
                                  type_info_index)

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
                    try:
                        feed_output.send_data(incident_context, incident)
                    except Exception as err:
                        LOG.error("Failure in update to %s %s", feed_output.__class__.__name__, err)

        except StopIteration:
            pass

        return max_inc_id, min_inc_id

    def _populate_others(self,
                         rest_client,
                         inc_range,
                         search_type_names,
                         type_info_index):
        for chunk in FeedComponent._range_chunks(inc_range,
                                                 FeedComponent.SEARCH_PAGE_SIZE):
            # Handle all the other built-in types using the search endpoint (except
            # the incident type, which was already handled above.  Make sure we only
            self._populate_others_chunk(chunk, rest_client, search_type_names, type_info_index)

    def _populate_others_chunk(self, chunk, rest_client, search_type_names, type_info_index):
        # get data for our org.
        #
        search_input_dto = {
            'query': 'inc_id:[{0} TO {1}]'.format(chunk[0], chunk[1]),
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
                try:
                    feed_output.send_data(context, result_data)
                except Exception as err:
                    LOG.error("Failure in update to %s %s", feed_output.__class__.__name__, err)

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

        while paged_results.get('data'):
            data = paged_results.get('data')

            for result in data:
                yield result

            query['start'] = len(data) + query['start']

            paged_results = rest_client.post(url, query)

    @staticmethod
    def _range_chunks(chunk_range, chunk_size):
        if isinstance(chunk_range, list):
            start = chunk_range[0]-1
            stop = chunk_range[-1]
        else:
            start = chunk_range.start - 1
            stop = chunk_range.stop

        while start <= stop:
            yield (start + 1, min(stop, start + chunk_size))

            start += chunk_size
