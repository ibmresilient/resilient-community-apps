# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_sumo_logic.lib.app_common import (PACKAGE_NAME, SOAR_HEADER, AppCommon)

PACKAGE_NAME = "fn_sumo_logic"
FN_NAME = "sumo_logic_update_insight_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sumo_logic_update_insight_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the status of an insight in Sumo Logic.  If the status is set to closed, set the resolution reason.
        Inputs:
            -   fn_inputs.sumo_logic_insight_id
            -   fn_inputs.sumo_logic_insight_status
            -   fn_inputs.sumo_logic_insight_resolution
        """

        validate_fields(["sumo_logic_insight_id", "sumo_logic_insight_status"], fn_inputs)

        status = getattr(fn_inputs, "sumo_logic_insight_status", None)
        resolution = getattr(fn_inputs, "sumo_logic_insight_resolution", None)

        app_common = AppCommon(PACKAGE_NAME, self.options)

        results, error_msg = app_common.update_insights_status(
                                            insight_id=fn_inputs.sumo_logic_insight_id,
                                            status=status,
                                            resolution=resolution)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
