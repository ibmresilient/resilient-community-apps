# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

PACKAGE_NAME = "fn_sentinelone"
FN_NAME = "sentinelone_resolve_threat_in_sentinelone"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sentinelone_resolve_threat_in_sentinelone'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Resolve (close) a threat in SentinelOne.
        Inputs:
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        sentinelone_client = SentinelOneClient(self.opts, self.options)
        incident_id = fn_inputs.incident_id
        success = False

        # Get the incident
        uri = u"/incidents/{}?handle_format=names".format(incident_id)
        incident = self.rest_client().get(uri)

        if not incident:
            IntegrationError("SentinelOne Resolve Threat: Incident {0} not found".format(incident_id))

        # Make sure there is an SentinelOne threat associated with this incident
        threat_id = incident.get('properties', {}).get('sentinelone_threat_id', None)
        if not threat_id:
            IntegrationError("SentinelOne Resolve Threat: sentinelone_threat_id {0} not found".format(threat_id))

        threat_analyst_verdict = incident.get('properties', {}).get('sentinelone_threat_analyst_verdict', None)

        if not threat_analyst_verdict:
            IntegrationError("SentinelOne Resolve Threat: threat_analyst_verdict is None")

        if threat_analyst_verdict == "undefined":
            IntegrationError("SentinelOne Resolve Threat: incident {0} is not closed due to 'analystVerdict' set to 'undefined'.".format(incident_id))

        log = logging.getLogger(__name__)
        verdict_response = sentinelone_client.update_threat_analyst_verdict(threat_id, threat_analyst_verdict)

        verdict_data = verdict_response.get("data")
        if int(verdict_data.get("affected")) <= 0:
            log.info("Unable to update analystVerdict in SentinelOne threat: %s", threat_id)
        else:
            status_response = sentinelone_client.update_threat_status(threat_id, "resolved")
            status_data = status_response.get("data")
            if int(status_data.get("affected")) <= 0:
                log.info("Unable to update incidentStatus to resolved in SentinelOne threat: %s", threat_id)
            else:
                success = True

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {"success": success,
                   "threat_id": threat_id}
        yield FunctionResult(results)

