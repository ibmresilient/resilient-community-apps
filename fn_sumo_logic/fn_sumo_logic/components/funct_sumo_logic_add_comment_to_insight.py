# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import (validate_fields, clean_html)
from fn_sumo_logic.lib.app_common import (PACKAGE_NAME, SOAR_HEADER, AppCommon)

PACKAGE_NAME = "fn_sumo_logic"
FN_NAME = "sumo_logic_add_comment_to_insight"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'sumo_logic_add_comment_to_insight'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Post a comment to a Sumo Logic insight in Sumo Logic.
        Inputs:
            -   fn_inputs.sumo_logic_insight_id
            -   fn_inputs.sumo_logic_comment_text
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["sumo_logic_insight_id", "sumo_logic_comment_text"], fn_inputs)

        app_common = AppCommon(PACKAGE_NAME, self.options)

        response, error_msg = app_common.post_comment(fn_inputs.sumo_logic_insight_id,
                                          clean_html(fn_inputs.sumo_logic_comment_text),
                                          comment_header=SOAR_HEADER)
        results = response

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)