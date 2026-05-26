# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, SOARCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME

FN_NAME = "symantec_dlp_update_incident"

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
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["sdlp_incident_severity_id", "sdlp_incident_status", "incident_id"], fn_inputs)

        sdlp_client = SymantecDLPCommon(self.rc, self.options)

        incident_id = getattr(fn_inputs, "incident_id", None)
        sdlp_incident_status = getattr(fn_inputs, "sdlp_incident_status", None)
        sdlp_incident_severity_id = getattr(fn_inputs, "sdlp_incident_severity_id", None)
        success = False

        # Get the SOAR incident
        incident = self.rest_client().get(f"/incidents/{incident_id}?handle_format=names")

        if not incident:
            IntegrationError(f"Symantec DLP Update Incident: Incident {incident_id} not found")

        # Make sure there is an Symantec DLP incident associated with this incident
        sdlp_incident_id = incident.get('properties', {}).get('sdlp_incident_id', None)
        if not sdlp_incident_id:
            IntegrationError(f"Symantec DLP Update Incident: sdlp_incident_id {sdlp_incident_id} not found")

        if sdlp_incident_status or sdlp_incident_severity_id:
            status_response = sdlp_client.update_sdlp_incident_editable_details(sdlp_incident_id, sdlp_incident_status, sdlp_incident_severity_id)

            # Be careful here. It seems like the DLP endpoint to set the status returns 200 even though the status
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
                patch_result = SOARCommon(self.rest_client).update_soar_case(incident_id, update_payload).json()
                success = patch_result.get("success")

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult({"success": success,
            "sdlp_incident_id": sdlp_incident_id,
            "sdlp_incident_status": sdlp_incident_status,
            "sdlp_incident_severity_id": sdlp_incident_severity_id})
