# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, SOARCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME
from fn_symantec_dlp.lib.jinja_common import JinjaEnvironment

DEFAULT_CREATE_DLP_CASE = "templates/dlp_create_case_template.jinja"
DEFAULT_SOAR_CLOSE_CASE = "templates/dlp_close_case_template.jinja"
DEFAULT_SOAR_UPDATE_CASE = "templates/dlp_update_case_template.jinja"

FN_NAME = "symantec_dlp_close_dlp_case"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_close_dlp_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Close SOAR case when the DLP incident status is set to Resolve.
        Inputs:
            -   fn_inputs.incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["incident_id"], fn_inputs)
        soar_case_id = getattr(fn_inputs, "incident_id", None)

        sdlp_client = SymantecDLPCommon(self.rc, self.options)
        jinja_env = JinjaEnvironment()

        # Get the SOAR incident
        incident = self.rest_client().get(f"/incidents/{soar_case_id}?handle_format=names")

        if not incident:
            IntegrationError(f"Symantec DLP: Close DLP Case: case {soar_case_id} not found")

        # Make sure there is an Symantec DLP incident associated with this incident
        sdlp_incident_id = incident.get('properties', {}).get('sdlp_incident_id', None)
        if not sdlp_incident_id:
            IntegrationError(f"Symantec DLP: Close DLP Case: sdlp_incident_id {sdlp_incident_id} not found")

        # Get the SDLP
        sdlp_incident_payload = sdlp_client.get_sdlp_incident_editable_detail_payload(sdlp_incident_id)

        # Close the case in SOAR
        incident_close_payload = jinja_env.make_payload_from_template(
            self.options.get("close_case_template"),
            DEFAULT_SOAR_CLOSE_CASE,
            sdlp_incident_payload)

        _close_resilient_incident = SOARCommon(self.rest_client).update_soar_case(soar_case_id, incident_close_payload)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
        yield FunctionResult({"success": True})
