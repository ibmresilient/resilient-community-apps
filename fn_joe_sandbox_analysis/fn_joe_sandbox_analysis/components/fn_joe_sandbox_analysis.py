# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from resilient_lib import validate_fields, str_to_bool
from fn_joe_sandbox_analysis.util.helper import connect_to_joe_sandbox, PACKAGE_NAME
from io import BytesIO
from time import sleep

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

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Instansiate new Joe Sandbox object and get ANALYSIS_URL
        ANALYSIS_URL, joesandbox = connect_to_joe_sandbox(self.opts, self.options)

        # Get Joe Sandbox options from app.config file
        ANALYSIS_REPORT_PING_DELAY = int(self.options.get("jsb_analysis_report_ping_delay", 120))
        ANALYSIS_TIMEOUT = int(self.options.get("jsb_analysis_report_request_timeout", 500))
        if ANALYSIS_TIMEOUT > 500: # Timeout can not be greater than 500
            ANALYSIS_TIMEOUT = 500
        email_notification = str_to_bool(self.options.get("jsb_email_notification", True))
        systems = self.options.get("jsb_systems", None)
        secondary_results = str_to_bool(self.options.get("jsb_secondary_results", True))

        # Validate required input fields
        validate_fields(["incident_id", "jsb_report_type"], fn_inputs)

        # Define inputs
        incident_id = fn_inputs.incident_id
        jsb_report_type = fn_inputs.jsb_report_type

        # Get optional inputs
        attachment_id = getattr(fn_inputs, "attachment_id", None)
        artifact_id = getattr(fn_inputs, "artifact_id", None)
        artifact_value = getattr(fn_inputs, "artifact_value", None)
        artifact_type = getattr(fn_inputs, "artifact_type", None)

        # Either `attachment_id` or `artifact_value` and `artifact_type` and `artifact_id` have to be defined
        if not attachment_id and not (artifact_value and artifact_type and artifact_id):
            raise ValueError("attachment_id or artifact_value and ( artifact_type and artifact_id ) is required")

        # Initialize variable
        attachment_content = None

        # Get input content and decide which joe sandbox call to make
        if artifact_value and artifact_type and artifact_id: # Artifact_value and artifact_type given
            if artifact_type in ["IP Address", "DNS Name", "URL", "URI Path"]: # URL type submission
                # Run specified windows machine, because if not specified it might run on android which will fail
                submission_id = joesandbox.submit_url(artifact_value,
                                                params={"systems": "w7x64" if not systems else list(systems),
                                                        "analysis-time": ANALYSIS_TIMEOUT,
                                                        "email-notification": email_notification,
                                                        "secondary-results": secondary_results}
                                                ).get("submission_id")
                self.LOG.info(f"Submission_id: {submission_id}")
            elif artifact_type in ["Other File", "Email Attachment"]: # File type submission
                attachment_content = self.rest_client().get_content(f"/incidents/{incident_id}/artifacts/{artifact_id}/contents")
        else: # Attachment_id given
            attachment_content = self.rest_client().get_content(f"/incidents/{incident_id}/attachments/{attachment_id}/contents")

        # If input is an attachment
        if attachment_content:
            submission_id = joesandbox.submit_sample(BytesIO(attachment_content),
                                            params={"systems": list(systems) if systems else None,
                                                    "analysis-time": ANALYSIS_TIMEOUT,
                                                    "email-notification": email_notification,
                                                    "secondary-results": secondary_results}
                                            ).get("submission_id")
            self.LOG.info(f"Submission_id: {submission_id}")

        # Get submission status
        submission_status = joesandbox.submission_info(submission_id).get("status")
        yield self.status_message(f"Submission ID: {submission_id}, Submission Status: {submission_status}")

        # Sleep and loop until submission status equals finished
        while submission_status != 'finished':
            self.LOG.debug(f"Submission Status: {submission_status}, sleeping: {ANALYSIS_REPORT_PING_DELAY} seconds.")
            sleep(ANALYSIS_REPORT_PING_DELAY)
            submission_status = joesandbox.submission_info(submission_id).get("status")

        yield self.status_message(f"Submission Status: {submission_status}")
        self.LOG.debug(f"Submission Status: {submission_status}")

        # Get analysis information
        analysis = joesandbox.analysis_info(submission_id)

        # Download the analysis file
        name, report = joesandbox.analysis_download(submission_id, jsb_report_type)

        MIMETYPES = {"pdf": "application/pdf",
                     "json": "application/json",
                     "html": "text/html"}

        try:
            # POST report as attachment to incident
            self.rest_client().post_attachment(f'/incidents/{incident_id}/attachments',
                                               None,
                                               bytes_handle=report,
                                               filename=name,
                                               mimetype=MIMETYPES[jsb_report_type])
        except Exception as e:
            self.LOG.debug(str(e))

        # Fill results
        results = {
            "analysis_report_name": name,
            "analysis_report_id": submission_id,
            "analysis_report_url": f"{ANALYSIS_URL}/analysis/{submission_id}",
            "analysis_status": analysis.get("detection")
        }

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results)