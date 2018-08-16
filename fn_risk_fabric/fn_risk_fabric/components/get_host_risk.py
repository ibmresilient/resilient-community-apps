# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import risk_fabric


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'get_host_risk"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_risk_fabric", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_risk_fabric", {})

    @function("get_host_risk")
    def _get_host_risk_function(self, event, *args, **kwargs):
        """Function: Function to retrieve the latest risk score for a host"""
        try:
            # Get the function parameters:
            hostname = kwargs.get("hostname")  # text

            log = logging.getLogger(__name__)
            log.info("hostname: %s", hostname)

            yield StatusMessage("starting...")
            result = risk_fabric.get_risk_info(self.options, 'computerendpoint', hostname)
            yield StatusMessage("done...")

            results = {
                "value": result
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()