# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import risk_fabric


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'set_event_mitigations"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_risk_fabric", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_risk_fabric", {})

    @function("set_event_mitigations")
    def _set_event_mitigations_function(self, event, *args, **kwargs):
        """Function: Function to set event mitigations"""
        try:
            # Get the function parameters:
            riskmodelinstanceid = kwargs.get("riskmodelinstanceid")  # text
            cardinstanceid = kwargs.get("cardinstanceid")  # text
            focusentityid = kwargs.get("focusentityid")  # text
            actionplanguid = kwargs.get("actionplanguid")  # text

            log = logging.getLogger(__name__)
            log.info("riskmodelinstanceid: %s", riskmodelinstanceid)
            log.info("cardinstanceid: %s", cardinstanceid)
            log.info("focusentityid: %s", focusentityid)
            log.info("actionplanguid: %s", actionplanguid)

            params = {
                'RiskModelInstanceID': riskmodelinstanceid,
                'CardInstanceID': cardinstanceid,
                'FocusEntityID': focusentityid,
                'ActionPlanGUID': actionplanguid,
            }

            yield StatusMessage("starting...")
            result = risk_fabric.set_event_mitigations(self.options, params)
            yield StatusMessage("done...")

            results = {
                "value": result
            }
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()