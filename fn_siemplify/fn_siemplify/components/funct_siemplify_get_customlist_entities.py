# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""AppFunction implementation"""

from fn_siemplify.lib.siemplify_common import SiemplifyCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "siemplify_get_customlist_entities"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'siemplify_get_customlist_entities'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get entities from Siemplify's Blacklist
        Inputs:
            -   fn_inputs.siemplify_limit
            -   fn_inputs.siemplify_search
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        # validate app.config settings
        validate_fields([
                {"name": "api_key"},
                {"name": "base_url"}
            ],
            self.app_configs._asdict())

        inputs = fn_inputs._asdict()

        siemplify_env = SiemplifyCommon(self.rc, self.app_configs)
        results, error_msg = siemplify_env.get_customlist()

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=isinstance(error_msg, type(None)), reason=error_msg)
