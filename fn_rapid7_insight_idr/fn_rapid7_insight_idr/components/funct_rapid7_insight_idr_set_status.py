# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.0.430

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, IntegrationError
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "rapid7_insight_idr_set_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rapid7_insight_idr_set_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Set the status of a Rapid7 InsightIDR investigation. Optionally, set the investigation, the close reason and free text.
        Inputs:
            -   fn_inputs.rapid7_insight_idr_rrn
            -   fn_inputs.rapid7_insight_idr_incident_id
            -   fn_inputs.rapid7_insight_idr_status
            -   fn_inputs.rapid7_insight_idr_disposition
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["rapid7_insight_idr_rrn", "rapid7_insight_idr_status", "rapid7_insight_idr_disposition"], fn_inputs)

        if "rapid7_insight_idr_status" == "CLOSED" and "rapid7_insight_idr_disposition" == "Undecided":
            IntegrationError("ERROR: Cannot close an investigation with Disposition: Undecided")

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        results_disposition, error_msg_disposition = app_common.set_disposition(fn_inputs.rapid7_insight_idr_rrn, 
                                                                                fn_inputs.rapid7_insight_idr_disposition)
        
        results_status, error_msg_status = app_common.set_status(fn_inputs.rapid7_insight_idr_rrn, 
                                                                 fn_inputs.rapid7_insight_idr_status)

        yield self.status_message("Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results_status, success=False if error_msg_status else True, reason=error_msg_status)

