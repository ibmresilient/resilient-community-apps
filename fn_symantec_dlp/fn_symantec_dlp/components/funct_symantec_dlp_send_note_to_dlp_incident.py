# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, clean_html, validate_fields
from fn_symantec_dlp.lib.constants import FROM_SYMANTEC_DLP_COMMENT_HDR, SENT_TO_SYMANTEC_DLP_HDR
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME

FN_NAME = "symantec_dlp_send_note_to_dlp_incident"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_send_note_to_dlp_incident'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Send a note from SOAR to the corresponding Symantec DLP incident.
        Inputs:
            -   fn_inputs.sdlp_incident_id
            -   fn_inputs.sdlp_note_text
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")
        validate_fields(["sdlp_incident_id", "sdlp_note_text"], fn_inputs)
        note_text = getattr(fn_inputs, "sdlp_note_text", None)
        sdlp_incident_id = getattr(fn_inputs, "sdlp_incident_id", None)

        reason = None
        success = False
        if FROM_SYMANTEC_DLP_COMMENT_HDR in note_text or SENT_TO_SYMANTEC_DLP_HDR in note_text:
            yield self.status_message(f"Bypassing synchronization of note: {note_text}")
            success = True
        else:
            try:
                sdlp_client = SymantecDLPCommon(self.rc, self.options)
                response = sdlp_client.send_note_to_sdlp(sdlp_incident_id, clean_html(note_text))

                updated_incident_ids = response.get("updatedIncidentIds")

                if sdlp_incident_id in updated_incident_ids:
                    success = True
                    yield self.status_message(f"Symantec DLP comment added to DLP incident id: {sdlp_incident_id}")
                else:
                    reason = "failure"
                    yield self.status_message(f"Symantec DLP comment failure for incident id {sdlp_incident_id}: {reason}")
            except IntegrationError as err:
                reason = str(err)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
        yield FunctionResult({"success": success, "reason:": reason})
