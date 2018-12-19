# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_query_tar_network.util.selftest as selftest
import requests

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'query_tor_network"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_query_tar_network", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_query_tar_network", {})

    @function("query_tor_network")
    def _query_tor_network_function(self, event, *args, **kwargs):
        """Function: This Function to Search for Given Parameter in TOR Relay Exit Node"""
        try:
            # Get the function parameters:
            search_data = kwargs.get("search_data")  # text

            log = logging.getLogger(__name__)
            log.info("search_data: %s", search_data)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            __params_data = {'flag': self.options.get('flag'), 'fields': self.options.get('data_fields'),
                             'search': search_data}

            __response_data = requests.get(self.options.get('base_url'), params=__params_data)

            __response_data = __response_data.text
            if __response_data.find(search_data) != -1:
                results = {'status': 'success', 'data': __response_data, 'value': True}
            else:
                log.info("No Data found for given search element...!")
                results = {'status': 'failed', 'data': __response_data, 'value': False}

            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)