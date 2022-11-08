# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_randori.lib.app_common import AppCommon, PACKAGE_NAME, SOAR_HEADER

PACKAGE_NAME = "fn_randori"
FN_NAME = "randori_send_note_as_comment_to_target"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'randori_send_note_as_comment_to_target'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Post a SOAR note as a comment in the corresponding Randori target.
        Inputs:
            -   fn_inputs.randori_comment_text
            -   fn_inputs.randori_target_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["randori_target_id", "randori_comment_text"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        results = app_common.post_target_comment(fn_inputs.randori_target_id, 
                                                 clean_html(fn_inputs.randori_comment_text),
                                                 comment_header=SOAR_HEADER)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
