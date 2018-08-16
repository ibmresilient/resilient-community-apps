# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import risk_fabric


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'get_ip_risk"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_risk_fabric", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_risk_fabric", {})

    @function("get_ip_risk")
    def _get_ip_risk_function(self, event, *args, **kwargs):
        """Function: Function to retrieve the latest risk score for an IP address"""
        try:
            # Get the function parameters:
            ipaddress = kwargs.get("ipaddress")  # text

            log = logging.getLogger(__name__)
            log.info("ipaddress: %s", ipaddress)

            yield StatusMessage("starting...")
            result = risk_fabric.get_risk_info(self.options, 'ipaddress', ipaddress)
            yield StatusMessage("done...")

            results = {
                "value": result
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()