# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from resilient_circuits import AppFunctionComponent, FunctionError, FunctionResult, app_function
from resilient_lib import validate_fields
from fn_joe_sandbox_analysis.util import helper

FN_NAME = "fn_joe_sandbox_analysis"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'fn_joe_sandbox_analysis"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, helper.PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Allows an Attachment or Artifact (File/URL) to be analyzed by Joe Sandbox.
        Inputs:
            -   fn_inputs.incident_id
            -   fn_inputs.attachment_id
            -   fn_inputs.artifact_value
            -   fn_inputs.jsb_report_type
        """

        # Instansiate new Joe Sandbox object and get ANALYSIS_URL
        ANALYSIS_URL, joesandbox = helper.connect_to_joe_sandbox(self.options)

        # Get Joe Sandbox options from app.config file
        ANALYSIS_REPORT_PING_DELAY = int(self.options.get("jsb_analysis_report_ping_delay"))
        ANALYSIS_REPORT_REQUEST_TIMEOUT = float(self.options.get("jsb_analysis_report_request_timeout"))

        # Validate required input fields
        validate_fields(["incident_id", "jsb_report_type"], fn_inputs)

        # Define inputs
        incident_id = getattr(fn_inputs, )
        kwargs.get("incident_id")
        jsb_report_type = kwargs.get("jsb_report_type")["name"]

        # Get optional inputs
        attachment_id = kwargs.get("attachment_id")  # number
        artifact_id = kwargs.get("artifact_id")  # number

        if not attachment_id and not artifact_id:
            raise ValueError("attachment_id or artifact_id is required")




