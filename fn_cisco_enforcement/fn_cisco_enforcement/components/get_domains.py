# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'get_domains"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_enforcement", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_enforcement", {})

    @function("get_domains")
    def _get_domains_function(self, event, *args, **kwargs):
        """Function: This is a function implementation that uses the Cisco API to gather the lists of domains already added to the shared customer’s domain list"""
        try:
            # Get the function parameters:

            log = logging.getLogger(__name__)
            apikey = self.options.get('apikey')
            isnextpage = True
            resultlist = []
            page = 1
            getapi = 'https://s-platform.api.opendns.com/1.0/domains?customerKey={}'.format(apikey)
            while (isnextpage):
                log.info('Get page {}'.format(page))
                api2 = requests.get(getapi)
                jsonversion = json.loads(api2.content)
                resultlist.extend(jsonversion['data'])
                page += 1
                if (jsonversion['meta']['next'] == False):
                    isnextpage = False
                getapi = jsonversion['meta']['next']

            results = {
                "value": resultlist
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()