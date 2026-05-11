# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "siemplify_add_playbook"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_add_playbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add a playbook to a Siemplify Case
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_run_playbook_automatically
            -   fn_inputs.siemplify_alert_id
            -   fn_inputs.siemplify_playbook_name
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        inputs = fn_inputs._asdict()

        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"},
                {"name": "default_environment"}
            ],
            self.app_configs._asdict())

        # validate input settings
        validate_fields([
                {"name": "siemplify_case_id"},
                {"name": "siemplify_alert_id"},
                {"name": "siemplify_playbook_name"},
                {"name": "siemplify_run_playbook_automatically"},
            ],
            inputs)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        b_results, err_msg = siemplify_env.attach_paybook(inputs)

        results = { "success": b_results }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=isinstance(err_msg, type(None)) and b_results, reason=err_msg)
