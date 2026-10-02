# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError
from fn_sentinelone.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "sentinelone_update_threat_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_update_threat_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the status of a threat in SentinelOne.
        Inputs:
            -   fn_inputs.sentinelone_threat_analyst_verdict
            -   fn_inputs.sentinelone_threat_status
            -   fn_inputs.sentinelone_threat_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)
        threat_id = fn_inputs.sentinelone_threat_id
        threat_status = fn_inputs.sentinelone_threat_status
        threat_analyst_verdict = fn_inputs.sentinelone_threat_analyst_verdict
        success_status = False
        success_verdict = False
        verdict_results = app_common.update_threat_analyst_verdict(threat_id, threat_analyst_verdict)
        verdict_data = verdict_results.get("data")
        if verdict_data.get("affected", -1) < 0:
            IntegrationError("SentinelOne Update Threat Status: unable to update analystVerdict {0} in SentinelOne threat: {1}".format(
                                threat_analyst_verdict, threat_id))
        else:
            success_verdict = True
            status_results = app_common.update_threat_status(threat_id, threat_status)
            status_data = status_results.get("data")
            if status_data.get("affected", -1) < 0:
                IntegrationError("SentinelOne Update Threat Status: unable to update incidentStatus {0} in SentinelOne threat: {1}".format(
                                threat_status, threat_id))
            else:
                success_status = True

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {"success_verdict": success_verdict,
                   "success_status": success_status,
                   "threat_id": threat_id,
                   "threat_analyst_verdict": threat_analyst_verdict,
                   "threat_status": threat_status
                   }
        yield FunctionResult(results)
