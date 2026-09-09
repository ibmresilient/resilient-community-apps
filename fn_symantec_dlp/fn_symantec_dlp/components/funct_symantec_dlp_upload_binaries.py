# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_symantec_dlp.lib.dlp_common import SymantecDLPCommon, PACKAGE_NAME

FN_NAME = "symantec_dlp_upload_binaries"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'symantec_dlp_upload_binaries'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Upload the Symantec DLP Component binary files and add as artifact files or incident attachment.
        Inputs:
            -   fn_inputs.sdlp_incident_id
            -   fn_inputs.incident_id
            -   fn_inputs.sdlp_attachment_upload_type
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["sdlp_incident_id", "incident_id"], fn_inputs)
        sdlp_incident_id = getattr(fn_inputs, "sdlp_incident_id", None)
        soar_case_id = getattr(fn_inputs, "incident_id", None)
        # This defines is the sdlp attachment will be uploaded to SOAR as an artifact or an attachment.
        # The value can be either artifact or attachment. Default is artifact.
        attachment_upload_type = getattr(fn_inputs, "sdlp_attachment_upload_type", "artifact") or "artifact"

        sdlp_client = SymantecDLPCommon(self.rc, self.options)

        artifact_name_list = sdlp_client.upload_sdlp_binaries(sdlp_incident_id, soar_case_id, self.rest_client(), attachment_upload_type)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult({"success": True, "artifact_name_list": artifact_name_list})
