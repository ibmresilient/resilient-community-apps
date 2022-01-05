# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from fn_siemplify.lib.resilient_common import ResilientCommon, b_to_s
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, clean_html

FN_NAME = "siemplify_close_case"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_close_case'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Close a Siemplify Case
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_comment
            -   fn_inputs.siemplify_alert_id
            -   fn_inputs.siemplify_root_cause
            -   fn_inputs.siemplify_reason
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
                {"name": "siemplify_root_cause"},
                {"name": "siemplify_reason"},
            ],
            inputs)

        # clean up the input fields
        inputs['siemplify_root_cause'] = clean_html(inputs['siemplify_root_cause'])

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results = siemplify_env.close_case(inputs)

        if not isinstance(results, dict):
            results = { "close_case": results }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
