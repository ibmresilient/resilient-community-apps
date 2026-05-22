# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.0.430

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "rapid7_insight_idr_list_attachments"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rapid7_insight_idr_list_attachments'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get list of the attachments of a Rapid7 InsightIDR investigation.
        Inputs:
            -   fn_inputs.rapid7_insight_idr_rrn
            -   fn_inputs.rapid7_insight_idr_incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["rapid7_insight_idr_rrn"], fn_inputs)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        response, error_msg = app_common.list_attachments(fn_inputs.rapid7_insight_idr_rrn)

        results = {"data": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)

