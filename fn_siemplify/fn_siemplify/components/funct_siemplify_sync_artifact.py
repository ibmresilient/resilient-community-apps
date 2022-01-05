# -*- coding: utf-8 -*-

"""AppFunction implementation"""

from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

FN_NAME = "siemplify_sync_artifact"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_sync_artifact'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: None
        Inputs:
            -   fn_inputs.siemplify_case_id
            -   fn_inputs.siemplify_artifact_type
            -   fn_inputs.siemplify_alert_id
            -   fn_inputs.siemplify_artifact_value
            -   fn_inputs.siemplify_environment
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_inputs_dict = fn_inputs._asdict()

        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"},
                {"name": "default_environment"}
            ],
            self.app_configs._asdict())

        validate_fields([
                {"name": "siemplify_case_id"},
                {"name": "siemplify_alert_id"},
                {"name": "siemplify_artifact_type"},
                {"name": "siemplify_artifact_value"}
            ],
            fn_inputs_dict)

        # use the default environment if none set in the function inputs
        if not fn_inputs_dict.get('siemplify_environment'):
            fn_inputs_dict['siemplify_environment'] = self.app_configs.default_environment

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        status = siemplify_env.sync_artifact(fn_inputs_dict) # returns true/false
        results = {}

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=status)

