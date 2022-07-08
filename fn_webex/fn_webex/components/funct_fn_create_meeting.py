# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_webex"
FN_NAME = "fn_create_meeting"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'fn_create_meeting'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Creates a WebEx meeting and returns the Host URL and Attendee URL.
        Inputs:
            -   fn_inputs.webex_meeting_password
            -   fn_inputs.webex_meeting_name
            -   fn_inputs.webex_meeting_agenda
            -   fn_inputs.webex_meeting_start_time
            -   fn_inputs.webex_meeting_end_time
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
