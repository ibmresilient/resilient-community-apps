# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_apility.util.selftest as selftest
import requests
from fn_apility.lib.resilient_common import api_url

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_apility"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_apility", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_apility", {})

    @function("fn_apility")
    def _fn_apility_function(self, event, *args, **kwargs):
        """Function: Apility's anti-abuse API helps you know immediately if a user’s IP address, domain or email address is blacklisted so you can decide whether to block it or not."""
        
        try:
            # Get the function parameters:
            apility_lookup_type = self.get_select_param(kwargs.get("apility_lookup_type"))  # select, values: "Email", "IP Address", "Domain"
            apility_lookup_value = kwargs.get("apility_lookup_value")  # text

            log = logging.getLogger(__name__)
            log.info("apility_lookup_type: %s", apility_lookup_type)
            log.info("apility_lookup_value: %s", apility_lookup_value)
            # log.info("apility_lookup_type type: %s", type(apility_lookup_value))

            HEADERS = {'content-type': 'application/json', 'X-Auth-Token': self.options['api_token']}
            api = api_url(apility_lookup_type)
            url = '/'.join((self.options['url'], api, apility_lookup_value))

            response = requests.get(url, headers=HEADERS)

            if(response.status_code == 200):
                res = response.json()
                res['query'] = apility_lookup_value
            else:
                msg = "Some error occured while retrieving the information from Apility.io with status code: {}"
                raise ValueError(msg.format(response.status_code))

            results = {
                "value": res
            }


            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
