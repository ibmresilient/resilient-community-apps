# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields
from fn_harfanglab_edr.lib.harfanglab_sdk import *

PACKAGE_NAME = "fn_harfanglab_edr"
FN_NAME = "harfanglab_isolate_endpoint"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'harfanglab_isolate_endpoint'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Isolate an endpoint
        Inputs:
            - fn_inputs.harfanglab_agent_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        verify = True
        if self.options.get('verify').lower() == 'false':
            verify = False
        conn = HarfangLabConnector(self.options.get('api_url'), self.options.get('api_key'), verify, self.options.get('http_proxy'), self.options.get('https_proxy'))


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

        agent_id = fn_inputs.harfanglab_agent_id
        try:
            results = conn.isolate_endpoint(agent_id)
            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionResult({}, success=False, reason=str(e))

