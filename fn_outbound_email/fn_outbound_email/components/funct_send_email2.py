# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_outbound_email"
FN_NAME = "send_email2"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'send_email2'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Send a plain text or HTML-formatted email with Resilient Incident details in the email body as well as incident attachments added to this outgoing email.
        Inputs:
            -   fn_inputs.mail_in_reply_to
            -   fn_inputs.mail_cc
            -   fn_inputs.mail_template
            -   fn_inputs.mail_bcc
            -   fn_inputs.mail_message_id
            -   fn_inputs.mail_attachments
            -   fn_inputs.mail_importance
            -   fn_inputs.mail_to
            -   fn_inputs.mail_body
            -   fn_inputs.mail_subject
            -   fn_inputs.mail_template_name
            -   fn_inputs.mail_from
            -   fn_inputs.mail_incident_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

        # Example accessing optional attribute in fn_inputs (this is similar for app_configs)
        # optional_input = fn_inputs.optional_input if hasattr(fn_inputs, "optional_input") else "Default Value"

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get("/functions/{0}?handle_format=names".format(FN_NAME))

        # Example raising an exception
        # raise IntegrationError("Example raising custom error")

        ##############################################
        # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
        ##############################################

        # Call API implementation example:
        # params = {
        #     "api_key": self.app_configs.api_key,
        #     "ip_address": fn_inputs.artifact_value
        # }
        #
        # response = self.rc.execute(
        #     method="get",
        #     url=self.app_configs.api_base_url,
        #     params=params
        # )
        #
        # results = response.json()
        #
        # yield self.status_message("Endpoint reached successfully and returning results for App Function: '{0}'".format(FN_NAME))
        #
        # yield FunctionResult(results)
        ##############################################

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        results = {"mock_key": "Mock Value!"}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
