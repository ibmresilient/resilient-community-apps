# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

PACKAGE_NAME = "fn_teams"
FN_NAME = "ms_teams_read_message_replies"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ms_teams_read_message_replies'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Read message replies from a Teams Channel for a given message
        Inputs:
            -   fn_inputs.ms_message_id
            -   fn_inputs.ms_channel_name
            -   fn_inputs.ms_groupteam_name
            -   fn_inputs.ms_groupteam_id
            -   fn_inputs.ms_group_mail_nickname
            -   fn_inputs.ms_channel_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

        # Example accessing optional attribute in fn_inputs and initializing it to None if it does not exist (this is similar for app_configs)
        # optional_input =  getattr(fn_inputs, "optional_input", None)

        # Example getting access to self.get_fn_msg()
        # fn_msg = self.get_fn_msg()
        # self.LOG.info("fn_msg: %s", fn_msg)

        # Example interacting with REST API
        # res_client = self.rest_client()
        # function_details = res_client.get(f"/functions/{FN_NAME}?handle_format=names")

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
        # yield self.status_message(f"Endpoint reached successfully and returning results for App Function: '{FN_NAME}'")
        #
        # yield FunctionResult(results)
        ##############################################

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Note this is only used for demo purposes! Put your own key/value pairs here that you want to access on the Platform
        results = {"mock_key": "Mock Value!"}

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
