# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_randori.lib.app_common import AppCommon, PACKAGE_NAME, SOAR_HEADER

FN_NAME = "randori_update_target_impact_score"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'randori_update_target_impact_score'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the specified target in Randori with the specified target impact score.
        Inputs:
            -   fn_inputs.randori_target_impact_score
            -   fn_inputs.randori_target_id
            -   fn_inputs.randori_note
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["randori_target_id", "randori_target_impact_score", "randori_note"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        results = app_common.update_target_impact_score(fn_inputs.randori_target_id, 
                                                        fn_inputs.randori_target_impact_score)

        if fn_inputs.randori_note:
            note_result = app_common.post_target_comment(fn_inputs.randori_target_id, 
                                                         clean_html(fn_inputs.randori_note), 
                                                         comment_header=SOAR_HEADER)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

