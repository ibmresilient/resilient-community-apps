# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_risk_fabric.util.risk_fabric import set_event_mitigations


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'rf_set_event_mitigations"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_risk_fabric", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_risk_fabric", {})

    @function("rf_set_event_mitigations")
    def _rf_set_event_mitigations_function(self, event, *args, **kwargs):
        """Function: Function to set event mitigations"""
        try:
            # Get the function parameters:
            rf_riskmodelinstanceid = kwargs.get("rf_riskmodelinstanceid")  # text
            rf_cardinstanceid = kwargs.get("rf_cardinstanceid")  # text
            rf_focusentityid = kwargs.get("rf_focusentityid")  # text
            rf_actionplanguid = kwargs.get("rf_actionplanguid")  # text

            log = logging.getLogger(__name__)
            log.info("rf_riskmodelinstanceid: %s", rf_riskmodelinstanceid)
            log.info("rf_cardinstanceid: %s", rf_cardinstanceid)
            log.info("rf_focusentityid: %s", rf_focusentityid)
            log.info("rf_actionplanguid: %s", rf_actionplanguid)

            params = {
                'RiskModelInstanceID': rf_riskmodelinstanceid,
                'CardInstanceID': rf_cardinstanceid,
                'FocusEntityID': rf_focusentityid,
                'ActionPlanGUID': rf_actionplanguid,
            }

            yield StatusMessage("starting...")
            result = set_event_mitigations(self.options, params)
            yield StatusMessage("done...")

            results = {
                "value": result
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()