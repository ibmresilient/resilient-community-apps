# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_risk_fabric.util.risk_fabric import get_risk_model_instances


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'rf_get_risk_model_instances"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_risk_fabric", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_risk_fabric", {})

    @function("rf_get_risk_model_instances")
    def _rf_get_risk_model_instances_function(self, event, *args, **kwargs):
        """Function: Function to retrieve risk model instances"""
        try:
            # Get the function parameters:
            rf_limit = kwargs.get("rf_limit")  # number

            log = logging.getLogger(__name__)
            log.info("rf_limit: %s", rf_limit)

            params = {
                'Limit': rf_limit
            }

            yield StatusMessage("starting...")
            result = get_risk_model_instances(self.options, params)
            yield StatusMessage("done...")

            results = {
                "value": result
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()