# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_threatminer.lib.threatminer_common import ThreatMiner, PACKAGE
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'threatminer_ip_whois"""

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

            data, msg = self.threatminer.get(u'/host.php?q={}&rt={}'.format(ip_address, '1'))

            yield StatusMessage(u"{} for {}".format(msg, ip_address))

            yield StatusMessage("done...")

            results = {
                "whois": data
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
