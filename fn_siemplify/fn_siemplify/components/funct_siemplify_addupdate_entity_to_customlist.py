# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "siemplify_addupdate_entity_to_customlist"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_addupdate_entity_to_customlist'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add an artifact to the Siemplify Blacklist
        Inputs:
            -   fn_inputs.siemplify_artifact_type
            -   fn_inputs.siemplify_artifact_value
            -   fn_inputs.siemplify_environment
            -   fn_inputs.siemplify_category
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        fn_inputs_dict = fn_inputs._asdict()
        app_configs = self.app_configs._asdict()

        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"},
                {"name": "default_environment"}
            ],
            app_configs)

        validate_fields([
                {"name": "siemplify_artifact_type"},
                {"name": "siemplify_artifact_value"}
            ],
            fn_inputs_dict)

        # use the default environment if none set in the function inputs
        if not fn_inputs_dict.get('siemplify_environment'):
            fn_inputs_dict['siemplify_environment'] = [self.app_configs.default_environment]
        else:
            fn_inputs_dict['siemplify_environment'] = [env.strip() for env in fn_inputs_dict['siemplify_environment'].split(",")]

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results, error_msg = siemplify_env.add_update_customlist(fn_inputs_dict) # returns blank when complete

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=isinstance(error_msg, type(None)), reason=error_msg)
