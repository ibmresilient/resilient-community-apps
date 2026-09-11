# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.0.430

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_rapid7_insight_idr.lib.app_common import (AppCommon, PACKAGE_NAME, SOAR_HEADER)

FN_NAME = "rapid7_insight_idr_post_comment"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'rapid7_insight_idr_post_comment'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Send a note to Rapid7 InsightIDR investigation as a comment.
        Inputs:
            -   fn_inputs.rapid7_insight_idr_rrn
            -   fn_inputs.rapid7_insight_idr_comment_text
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["rapid7_insight_idr_rrn", "rapid7_insight_idr_comment_text"], fn_inputs)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)

        response, error_msg = app_common.post_comment(fn_inputs.rapid7_insight_idr_rrn, 
                                          clean_html(fn_inputs.rapid7_insight_idr_comment_text),
                                          comment_header=SOAR_HEADER)
        results = response

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)