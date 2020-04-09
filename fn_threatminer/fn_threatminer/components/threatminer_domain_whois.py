# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_threatminer.lib.threatminer_common import ThreatMiner, PACKAGE
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_domain_whois"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE, {})
        self.threatminer = ThreatMiner(opts, self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values

        """
        self.options = opts.get(PACKAGE, {})
        self.threatminer = ThreatMiner(opts, self.options)

    @function("threatminer_domain_whois")
    def _threatminer_domain_whois_function(self, event, *args, **kwargs):
        """Function: Grab Whois Data from Threatminer"""
        try:
            # Get the function parameters:
            domain_name = kwargs.get("domain_name")  # text

            log = logging.getLogger(__name__)
            log.info("domain_name: %s", domain_name)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            data, msg = self.threatminer.get(u'/domain.php?q={}&rt={}'.format(domain_name, '1'))

            yield StatusMessage(u"{} for {}".format(msg, domain_name))

            results = {
                "whois": data
            }

            yield StatusMessage("done ... ")
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
