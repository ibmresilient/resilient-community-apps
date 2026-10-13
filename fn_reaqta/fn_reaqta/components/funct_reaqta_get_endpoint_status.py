# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME, get_hive_options
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

PACKAGE_NAME = "fn_reaqta"
FN_NAME = "reaqta_get_endpoint_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_get_endpoint_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the current status of an endpoint
        Inputs:
            -   fn_inputs.reaqta_endpoint_id
            -   fn_inputs.reaqta_hive
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_hive", "reaqta_endpoint_id"], fn_inputs)

        hive_settings = get_hive_options(fn_inputs.reaqta_hive, self.opts)
        if not hive_settings:
            results = {}
            err_msg = "Hive section not found: {}".format(fn_inputs.reaqta_hive)
        else:
            app_common = AppCommon(self.rc, hive_settings)
            results, err_msg = app_common.get_endpoint_status(fn_inputs.reaqta_endpoint_id)

        # Example validating app_configs
        # validate_fields([
        #     {"name": "api_key", "placeholder": "<your-api-key>"},
        #     {"name": "base_url", "placeholder": "<api-base-url>"}],
        #     self.app_configs)

        # Example validating required fn_inputs
        # validate_fields(["required_input_one", "required_input_two"], fn_inputs)

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

        # Call API implemtation example:
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

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
