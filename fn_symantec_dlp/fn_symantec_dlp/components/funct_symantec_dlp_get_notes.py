# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, SOARCommon
from fn_symantec_dlp.lib.resilient_common import ResilientCommon
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME

FN_NAME = "symantec_dlp_get_notes"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_get_notes'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Synchronize the notes between Symantec DLP and corresponding SOAR incident.
        Inputs:
            -   fn_inputs.incident_id
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["incident_id"], fn_inputs)
        soar_case_id = getattr(fn_inputs, "incident_id", None)
        sdlp_client = SymantecDLPCommon(self.rc, self.options)

        # Get the SOAR incident
        incident = self.rest_client().get(f"/incidents/{soar_case_id}?handle_format=names")

        if not incident:
            IntegrationError(f"Symantec DLP: Get DLP Notes: Case {soar_case_id} not found")

        # Make sure there is an Symantec DLP incident associated with this incident
        sdlp_incident_id = incident.get('properties', {}).get('sdlp_incident_id', None)
        if not sdlp_incident_id:
            IntegrationError(f"Symantec DLP Get Notes: sdlp_incident_id {sdlp_incident_id} not found")

        # SYNC DLP Comments
        sdlp_notes  = sdlp_client.get_sdlp_incident_notes(sdlp_incident_id)
        new_comments = ResilientCommon(self.rest_client).filter_resilient_comments(soar_case_id, sdlp_notes)
        self.LOG.info(new_comments)

        for comment in new_comments:
            _ = SOARCommon(self.rest_client).create_case_comment(soar_case_id, comment)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
        yield FunctionResult({"success": True, "new_notes": new_comments})
