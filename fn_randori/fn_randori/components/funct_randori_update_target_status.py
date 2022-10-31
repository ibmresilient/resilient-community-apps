# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_randori.lib.app_common import AppCommon, PACKAGE_NAME

PACKAGE_NAME = "fn_randori"
FN_NAME = "randori_update_target_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'randori_update_target_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the specified target in Randori with the specified target status and /or impact score.
        Inputs:
            -   fn_inputs.randori_target_id
            -   fn_inputs.randori_target_status
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["randori_target_id", "randori_target_status"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        results = app_common.update_target_status(fn_inputs.randori_target_id, fn_inputs.randori_target_status)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

