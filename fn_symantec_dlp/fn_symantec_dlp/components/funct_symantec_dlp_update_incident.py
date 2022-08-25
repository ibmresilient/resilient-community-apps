# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
import logging
from unittest.mock import patch
from resilient import get_client
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon

PACKAGE_NAME = "fn_symantec_dlp"
FN_NAME = "symantec_dlp_update_incident"

LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_update_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update an status or the severity in Symantec DLP.
        Inputs:
            -   fn_inputs.sdlp_incident_severity_id
            -   fn_inputs.sdlp_incident_status
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        rest_client = get_client(self.opts)
        res_common = ResilientCommon(rest_client)
        sdlp_client = SymantecDLPCommon(self.rc, self.options)

        incident_id = fn_inputs.incident_id
        sdlp_incident_status = fn_inputs.sdlp_incident_status
        sdlp_incident_severity_id = fn_inputs.sdlp_incident_severity_id
        success = False

        # Get the SOAR incident
        uri = u"/incidents/{}?handle_format=names".format(incident_id)
        incident = self.rest_client().get(uri)

        if not incident:
            IntegrationError("Symantec DLP Update Incident: Incident {0} not found".format(incident_id))


        # Make sure there is an Symantec DLP incident associated with this incident
        sdlp_incident_id = incident.get('properties', {}).get('sdlp_incident_id', None)
        if not sdlp_incident_id:
            IntegrationError("Symantec DLP Update Incident: sdlp_incident_id {0} not found".format(sdlp_incident_id))

        if sdlp_incident_status or sdlp_incident_severity_id:

            status_response = sdlp_client.update_sdlp_incident_editable_details(sdlp_incident_id, sdlp_incident_status, sdlp_incident_severity_id)

            # Becareful here.  It seems like the DLP endpoint to set the status returns 200 even though the status
            # is not truely set. Both incident status name and status id need to be set to change the incident status but 
            # no matter what you send it still comes back with 200.
            if sdlp_incident_id and sdlp_incident_id in status_response.get("updatedIncidentIds", []):
                update_payload = {}
                if sdlp_incident_status:
                    # If the status was updated in DLP, then update the status in the custom field in SOAR.
                    update_payload["properties"] = { "sdlp_incident_status": sdlp_incident_status}
                if sdlp_incident_severity_id:
                    # If DLP status is Info map to Low in SOAR
                    if sdlp_incident_severity_id == "Info":
                        sdlp_incident_severity_id = "Low"
                    update_payload["severity_code"] = sdlp_incident_severity_id
                # Update the SOAR incident
                patch_result = res_common.update_incident(incident_id, update_payload)
                success = patch_result.get("success")

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        results = {"success": success,
                   "sdlp_incident_id": sdlp_incident_id,
                   "sdlp_incident_status": sdlp_incident_status,
                   "sdlp_incident_severity_id": sdlp_incident_severity_id}
        yield FunctionResult(results)
