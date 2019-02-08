# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import requests
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_threatminer.util.selftest as selftest



class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_ip_whois"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_threatminer", {})
        selftest.selftest_function(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values

        Default:

        [fn_threatminer]
        url=https://api.threatminer.org/v2
        """

        self.options = opts.get("fn_threatminer", {})

    @function("threatminer_ip_whois")
    def _threatminer_ip_whois_function(self, event, *args, **kwargs):
        """Function: Return WHOIS information for IP Address from Threatminer API"""
        try:
            # Get the function parameters:
            ip_address = kwargs.get("ip_address")  # text

            log = logging.getLogger(__name__)
            log.info("ip_address: %s", ip_address)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            url = self.options.get('url', None)
            if not url:
                raise LookupError('missing url from [fn_threatminer] in app_config')

            response = requests.get('{}/host.php?q={}&rt={}'.format(url, ip_address, '1'))

            if response.status_code == 200:
                yield StatusMessage('Results returned for {}'.format(ip_address))
            elif response.status_code == 404:
                yield StatusMessage('No Results Returned for {}'.format(ip_address))
            else:
                yield StatusMessage('Unexpected return code of {}'.format(response.status_code))

            ip_whois_data = response.text

            yield StatusMessage("done...")

            results = {
                "whois": ip_whois_data
            }
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")


            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            print "Error"
            yield FunctionError(e)