# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v50.1.262

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "rapid7_insight_idr_get_investigation"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rapid7_insight_idr_get_investigation'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the investigation information from Rapid7 InsightIDR given the Rapid7 Resource Name (rrn) of the investigation.
        Inputs:
            -   fn_inputs.rapid7_insight_idr_rrn
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["rapid7_insight_idr_rrn"], fn_inputs)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        response, error_msg = app_common.get_investigation(fn_inputs.rapid7_insight_idr_rrn)

        # Add the link back to Rapid7 InsightIDR investigation
        response["entity_url"] = app_common.make_linkback_url(entity_id=fn_inputs.rapid7_insight_idr_rrn)
 
        results = {"rapid7_insight_idr_investigation": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
