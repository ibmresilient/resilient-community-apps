# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import fn_threatminer.util.selftest as selftest
import requests

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_domain_subdomains"""

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

    @function("threatminer_domain_subdomains")
    def _threatminer_domain_subdomains_function(self, event, *args, **kwargs):
        """Function: Grab all Subdomains for a Domain from Threatminer"""
        try:
            # Get the function parameters:
            domain_name = kwargs.get("domain_name")  # text

            log = logging.getLogger(__name__)
            log.info("domain_name: %s", domain_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            url = self.options.get('url', None)
            if not url:
                raise LookupError('missing url from [fn_threatminer] in app_config')

            response = requests.get("{}/domain.php?q={}&rt={}".format(url,domain_name,'5'))

            if response.status_code == 200:
                yield StatusMessage("Results Returned for {}".format(domain_name))
            elif response.status_code == 404:
                yield StatusMessage("No Results Returned for {}".format(domain_name))
            else:
                raise Exception("Unexpected return code of {}".format(response.status_code))

            domain_subdomain_data = response.text



            results = {
                "subdomains": domain_subdomain_data
            }
            yield StatusMessage("done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
