# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
import functools
from threading import Event
from datetime import datetime
from logging import getLogger
from traceback import format_exc
from resilient import SimpleHTTPException

LOG = getLogger(__name__)

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
        # when the last poller run to the function it's calling
        @functools.wraps(func)
        def wrapped(self):
            last_poller_time = getattr(self, named_last_poller_time)
            exit_event = Event()

            while not exit_event.is_set():
                try:
                    LOG.info(u"%s polling start.", package_name)
                    poller_start = datetime.now()
                    # function execution with the last poller time in ms
                    func(self, last_poller_time=int(last_poller_time.timestamp()*1000))

                except Exception as err:
                    LOG.error(str(err))
                    LOG.error(format_exc())
                finally:
                    LOG.info(u"%s polling complete.", package_name)
                    # set the last poller time for next cycle
                    last_poller_time = poller_start

                    # sleep before the next poller execution
                    exit_event.wait(getattr(self, named_poller_interval)*60)
            exit_event.set() # loop complete

        return wrapped
    return poller_wrapper

class SOARCommon():
    """ common methods for accessing IBM SOAR cases and their entities: comment, attachments, etc. """

    def get_open_soar_cases(search_fields, rest_client, open_cases=True):
        """ find all IBM SOAR cases which are associated with the endpoint platform
        Args:
            search_fields [dict]: list of field(s) used to track the relationship with a SOAR case
                                 field values can be True/False for 'has_a_value' or 'does_not_have_a_value'
                                 Otherwise a field will use 'equals' for the value
            NOTE: search_fields only supports custom fields
        Returns:
            soar_cases [list]: returned list of cases
            error_msg [str]: any error during the query or None
        """
        query = SOARCommon._build_search_query(search_fields, open_cases=open_cases)

        try:
            return rest_client.post('/incidents/query?return_level=normal', query), None
        except SimpleHTTPException as err:
            LOG.error(str(err))
            LOG.error(query)
            return None, str(err)

    def _build_search_query(search_fields, open_cases=True):
        """[Build the json structure needed to search for cases]
        Args:
            search_fields ([dict/list]): [key/value pairs to search custom fields with specific values. If
                                         a value contains "*" then a search is used with 'has_a_value']
            NOTE: search_fields works on custom fields
        Returns:
            query_string ([dict]): [json stucture used for cases searching]
        """
        query = {
            "filters": [{
                "conditions": [
                 ]
            }],
            "sorts": [{
                "field_name": "create_date",
                "type": "desc"
            }]
        }

        if open_cases:
            field_search = {
                            "field_name": "plan_status",
                            "method": "equals",
                            "value": "A"
                          }
            query['filters'][0]['conditions'].append(field_search)

        if isinstance(search_fields, dict):
            for search_field, search_value in search_fields.items():
                field_search = {
                            "field_name": "properties.{0}".format(search_field)
                        }
                if isinstance(search_value, bool):
                    field_search['method'] = "has_a_value" if search_value else "does_not_have_a_value"
                else:
                    field_search['method'] = "equals"
                    field_search['value'] = search_value

                query['filters'][0]['conditions'].append(field_search)

        return query
