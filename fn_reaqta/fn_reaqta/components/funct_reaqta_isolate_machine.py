# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""
from fn_reaqta.lib.app_common import AppCommon, PACKAGE_NAME
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields

FN_NAME = "reaqta_isolate_machine"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'reaqta_isolate_machine'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Isolate a ReaQta controlled machine based on it's endpoint ID
        Inputs:
            -   fn_inputs.reaqta_endpoint_id
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        validate_fields(["reaqta_url",
                        "api_version",
                        "cafile",
                        "api_key",
                        "api_secret"],
                        self.app_configs)

        validate_fields(["reaqta_endpoint_id"], fn_inputs)

        app_common = AppCommon(self.rc, self.app_configs._asdict())
        results, err_msg = app_common.isolate_machine(fn_inputs.reaqta_endpoint_id)

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        yield FunctionResult(results, success=True if not err_msg else False, reason=err_msg)
