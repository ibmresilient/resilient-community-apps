# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_siemplify.lib.resilient_common import ResilientCommon
from fn_siemplify.lib.siemplify_common import SiemplifyCommon
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_siemplify"
FN_NAME = "siemplify_sync_task"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_task'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Sync a SOAR Task to Siemplify
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_task_due_date
            -   fn_inputs.siemlify_task_assignee
            -   fn_inputs.siemplify_task_content
            -   fn_inputs.siemplify_task_name
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_inputs_dict = fn_inputs._asdict()
        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"}
            ],
            self.app_configs._asdict())

        validate_fields([
                {"name": "siemplify_case_id"},
                {"name": "siemplify_soar_task_id"}
            ],
            fn_inputs_dict)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)

        # get the contents of the
        res_common = ResilientCommon(self.rest_client())
        task_info, siemplify_task_id = res_common.get_incident_task(fn_inputs.siemplify_soar_task_id)

        results = siemplify_env.sync_task(fn_inputs.siemplify_case_id, fn_inputs.siemplify_task_assignee,
                                          siemplify_task_id, task_info)

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

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
