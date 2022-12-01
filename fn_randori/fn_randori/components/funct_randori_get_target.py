# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_randori.lib.app_common import AppCommon, PACKAGE_NAME

FN_NAME = "randori_get_target"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'randori_get_target'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the target data for a single Randori target instance.
        Inputs:
            -   fn_inputs.randori_target_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["randori_target_id"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        results = app_common.get_target(fn_inputs.randori_target_id)
        results["entity_url"] = app_common.make_linkback_url(fn_inputs.randori_target_id)
        
        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
