# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import validate_fields
from fn_joe_sandbox_analysis.util.helper import connect_to_joe_sandbox, PACKAGE_NAME

FN_NAME = "fn_joe_sandbox_analysis"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_joe_sandbox_analysis"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Allows an Attachment or Artifact (File/URL) to be analyzed by Joe Sandbox.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.attachment_id
            -   fn_inputs.artifact_value
            -   fn_inputs.artifact_type
            -   fn_inputs.artfact_id
            -   fn_inputs.jsb_report_type
        """

        # Instansiate new Joe Sandbox object and get ANALYSIS_URL
        ANALYSIS_URL, joesandbox = connect_to_joe_sandbox(self.opts, self.options)

        # Get Joe Sandbox options from app.config file
        ANALYSIS_REPORT_PING_DELAY = int(self.options.get("jsb_analysis_report_ping_delay"))
        ANALYSIS_REPORT_REQUEST_TIMEOUT = float(self.options.get("jsb_analysis_report_request_timeout"))

        # Validate required input fields
        validate_fields(["incident_id", "jsb_report_type"], fn_inputs)

        # Define inputs
        incident_id = getattr(fn_inputs, "incident_id", None)
        jsb_report_type = getattr(fn_inputs, "jsb_report_type", None)

        # Get optional inputs
        attachment_id = getattr(fn_inputs, "attachment_id", None)
        artifact_id = getattr(fn_inputs, "artifact_id", None)
        artifact_value = getattr(fn_inputs, "artifact_value", None)
        artifact_type = getattr(fn_inputs, "artifact_type", None)

        # Either `attachment_id` or `artifact_value` and `artifact_type` and `artifact_id` have to be defined
        if not attachment_id and not (artifact_value and artifact_type and artifact_id):
            raise ValueError("attachment_id or artifact_value and ( artifact_type and artifact_id ) is required")

        # Get input content and decide which joe sandbox call to make
        if artifact_value and artifact_type and artifact_id: # Artifact_value and artifact_type given
            if artifact_type in ["IP Address", "DNS Name", "URL", "URI Path"]: # URL type submission
                submission_id = joesandbox.submit_url(artifact_value)
            elif artifact_type in ["Other File", "Email Attachment"]: # File type submission
                attachment_content = self.rest_client().get(f"/incidents/{incident_id}/artifacts/{artifact_id}/contents")
        else: # Attachment_id given
            pass # Get attachment content

        print("s")
