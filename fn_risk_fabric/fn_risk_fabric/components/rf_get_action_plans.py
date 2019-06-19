# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_risk_fabric.util.risk_fabric import get_action_plans


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'rf_get_action_plans"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_risk_fabric", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_risk_fabric", {})

    @function("rf_get_action_plans")
    def _rf_get_action_plans_function(self, event, *args, **kwargs):
        """Function: Action to retrieve action plans"""
        try:
            # Get the function parameters:

            log = logging.getLogger(__name__)

            yield StatusMessage("starting...")
            result = get_action_plans(self.options)
            yield StatusMessage("done...")

            results = {
                "value": result
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()