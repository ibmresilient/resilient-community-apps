# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields

PACKAGE_NAME = "fn_reaqta"
FN_NAME = "reaqta_create_policy"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_create_policy'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create an alert trigger based on a program's SHA256 hash
        Inputs:
            -   fn_inputs.reaqta_policy_title
            -   fn_inputs.reaqta_policy_block
            -   fn_inputs.reaqta_policy_included_groups
            -   fn_inputs.reaqta_policy_excluded_groups
            -   fn_inputs.reaqta_sha256
            -   fn_inputs.reaqta_policy_description
            -   fn_inputs.reaqta_policy_enabled
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_policy_title",
                        "reaqta_sha256",
                        "reaqta_policy_enabled",
                        "reaqta_policy_block"
                       ],
                       fn_inputs)

        app_common = AppCommon(self.rc, self.app_configs._asdict())
        response, err_msg = app_common.create_policy(fn_inputs._asdict())

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(response.json(), success=True if not err_msg else False, reason=err_msg)
