# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "siemplify_sync_comment"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_comment'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a Siemplify Case comment
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_comment
            -   fn_inputs.siemplify_alert_id
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
                {"name": "siemplify_alert_id"},
                {"name": "siemplify_comment"}
            ],
            fn_inputs_dict)

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results = siemplify_env.sync_insight(fn_inputs_dict)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results)
        # yield FunctionResult({}, success=False, reason="Bad call")
