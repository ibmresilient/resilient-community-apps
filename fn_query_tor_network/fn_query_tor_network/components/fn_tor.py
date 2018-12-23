# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_query_tor_network.util.selftest as selftest
import requests

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_tor"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_query_tor_network", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_query_tor_network", {})

    @function("fn_tor")
    def _fn_tor_function(self, event, *args, **kwargs):
        """Function: This TOR function searches for the given IP Address or host names in TOR exit node Network by using RESTful API"""
        try:
            # Get the function parameters:
            tor_search_data = kwargs.get("tor_search_data")  # text

            log = logging.getLogger(__name__)
            log.info("tor_search_data: %s", tor_search_data)

            yield StatusMessage("starting...")

            __params_data = {'flag': self.options.get('flag'), 'fields': self.options.get('data_fields'),
                             'search': tor_search_data}
            __params_data = "&".join("%s=%s" % (k, v) for k, v in __params_data.items())
            __response_data = requests.get(self.options.get('base_url'), params=__params_data)
            __MATCH_FLAG = False
            if __response_data.status_code == 200:
                __response_data_json_obj = __response_data.json()
                __relays_data_list = __response_data_json_obj.get('relays')
                search_field_list = self.options.get('data_fields').split(',')
                if not __relays_data_list:
                    log.info("Given Search Artifact is Not Matched...!")
                    __MATCH_FLAG = False
                else:
                    for relay_data in __relays_data_list:
                        for field in search_field_list:
                            data = relay_data.get(field)
                            if data is not None:
                                if isinstance(data, list):
                                    for element in data:
                                        if element.find(tor_search_data) != -1:
                                            log.info('Given Search Artifact matched..!')
                                            __MATCH_FLAG = True
                                else:
                                    if data.find(tor_search_data) != -1:
                                        log.info('Given Search Artifact matched..!')
                                        __MATCH_FLAG = True
            else:
                __MATCH_FLAG = False
                log.info(__response_data.text)

            if __MATCH_FLAG:
                results = {'status': 'success', 'value': True, 'data': __response_data.text}
            else:
                log.info("Given Search Artifact is Not Matched...!")
                results = {'status': 'failed', 'value': False, 'data': __response_data.text}

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)