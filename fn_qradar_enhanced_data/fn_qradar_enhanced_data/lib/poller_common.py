# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import datetime
import functools
import logging
import traceback
from ast import literal_eval
from threading import Event
from resilient import SimpleHTTPException, Patch
from resilient_lib import IntegrationError, get_file_attachment, get_file_attachment_name
from cachetools import cached, LRUCache

LOG = logging.getLogger(__name__)

IBM_SOAR = "IBM SOAR" # common label
SOAR_HEADER = "Created by {}".format(IBM_SOAR)

TYPES_URI = "/types"
INCIDENTS_URI = "/incidents"

# P O L L E R   L O G I C
def poller(named_poller_interval, named_last_poller_time, package_name):
    """[decorator for poller, manage poller time, calling the customized method for getting the next entities]
    Args:
        named_poller_interval ([str]): [name of instance variable containing the poller interval in seconds]
        named_last_poller_time ([datetime]): [name of instance variable containing the lookback value in mseconds]
        package_name ([str]: [name of package for loggging]
    """
    def poller_wrapper(func):
        # decorator for running a function forever, passing the ms timestamp of
        #  when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(u"%s polling start.", package_name)
                    poller_start = datetime.datetime.now()
                    # function execution with the last poller time in ms
                    func(self, last_poller_time=int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(traceback.format_exc())
                finally:
                    LOG.info(u"%s polling complete.", package_name)
                    # set the last poller time for next cycle
                    last_poller_time = poller_start

                    # sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval))
            exit_event.set() # loop complete

        return wrapped
    return poller_wrapper

class SOARCommon():
    """ common methods for accessing IBM SOAR cases and their entities: comment, attachments, etc. """
    def __init__(self, rest_client):
        self.rest_client = rest_client

    def get_open_soar_cases(self, search_fields, open_cases=True):
        """ find all open IBM SOAR cases which are associated with the endpoint platform
        Args:
            search_fields [list]: list of field(s) used to track the relationship with a SOAR case
        Returns:
            soar_case [dict]: returned list is indexed by the first field in search_fields
        """
        query = self._build_search_query(search_fields)

        cases = self._query_cases(query)
        # return dictionary of cases indexed first field in the list
        return { case['properties'][search_fields[0]]: case['id'] for case in cases }

    def _build_search_query(self, search_fields):
        """[Build the json structure needed to search for cases]
        Args:
            search_fields ([dict/list]): [key/value pairs to search custom fields with specific values or
                                         a list of search fields to ensure they have values]
        Returns:
            query_string ([dict]): [json stucture used for cases searching]
        """
        query = {
            "filters": [{
                "conditions": [ ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }

        if isinstance(search_fields, dict):
            for search_field, search_value in search_fields.items():
                field_search = {
                            "field_name": "properties.{0}".format(search_field),
                            "method": "equals",
                            "value": search_value
                        }
                query['filters'][0]['conditions'].append(field_search)
        elif isinstance(search_fields, list):
            for search_field in search_fields:
                field_search = {
                            "field_name": "properties.{0}".format(search_field),
                             "method": "has_a_value"
                        }
                query['filters'][0]['conditions'].append(field_search)

        return query

    def _query_cases(self, query):
        """ run a query to find case(s) which match the query string
        Args:
            query [str]: query string to find cases
        Returns:
            query_results [list]: List of query results
        """
        query_uri = "/".join([INCIDENTS_URI, "query?return_level=normal"])

        try:
            return self.rest_client.post(query_uri, query), None
        except SimpleHTTPException as err:
            LOG.error(str(err))
            LOG.error(query)
            return None, str(err)

    def _patch_case(self, case_id, case_payload):
        """ _patch_case will update an case with the specified json payload.
        :param case_id: case ID of case to be updated.
        ;param case_payload: case fields to be updated.
        :return:
        """
        try:
            # Update case
            case_url = "/".join([INCIDENTS_URI, str(case_id)])
            case = self.rest_client.get(case_url)
            patch = Patch(case)

            # Iterate over payload dict.
            for name, _ in case_payload.items():
                if name == 'properties':
                    for field_name, field_value in case_payload['properties'].items():
                        patch.add_value(field_name, field_value)
                else:
                    payload_value = case_payload.get(name)
                    patch.add_value(name, payload_value)

            patch_result = self.rest_client.patch(case_url, patch)
            result = self._chk_status(patch_result)
            # add back the case id
            result['id'] = case_id
            return result

        except Exception as err:
            LOG.error(str(err))
            raise IntegrationError from err

    def _chk_status(self, resp, rc=200):
        """
        check the return status. If return code is not met, raise IntegrationError,
        if success, return the json payload
        :param resp:
        :param rc:
        :return:
        """
        if hasattr(resp, "status_code"):
            if isinstance(rc, list):
                if resp.status_code < rc[0] or resp.status_code > rc[1]:
                    raise IntegrationError(u"status code failure: {0}".format(resp.status_code))
            elif resp.status_code != rc:
                raise IntegrationError(u"status code failure: {0}".format(resp.status_code))

            return resp.json()

        return {}

@cached(cache=LRUCache(maxsize=100))
def eval_mapping(eval_value, wrapper=None):
    """
    Args:
            eval_value ([str]): [json fragment to evaluate]
            wrapper ([str]): [values such as '[{}]' or '{{ {} }}']
        Returns:
            mapping ([list or dict]): converted data
    """
    if not eval_value:
        return None

    try:
        if wrapper:
            eval_value = wrapper.format(eval_value)

        # Try converting input to a dict or array
        result = literal_eval(eval_value)
        # expecting the result to be a list or dictionary
        if not isinstance(result, (list, dict)):
            raise IndentationError("Unexpected result: %s", result)

        return result

    except Exception as err:
        LOG.error(str(err))
        LOG.error(traceback.format_exc())
        LOG.error("""mapping eval_value must be a string representation of a (partial) array or dictionary e.g. "'value1', 'value2'" or "'key':'value'" """)

    return None