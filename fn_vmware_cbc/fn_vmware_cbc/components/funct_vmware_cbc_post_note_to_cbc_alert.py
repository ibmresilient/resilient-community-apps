# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_vmware_cbc.lib.app_common import (AppCommon, PACKAGE_NAME, SOAR_HEADER)

PACKAGE_NAME = "fn_vmware_cbc"
FN_NAME = "vmware_cbc_post_note_to_cbc_alert"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'vmware_cbc_post_note_to_cbc_alert'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Post a note to the specified Carbon Black Cloud alert in CBC.
        Inputs:
            -   fn_inputs.vmware_cbc_alert_note_text
            -   fn_inputs.vmware_cbc_alert_id
        """

        validate_fields(["vmware_cbc_alert_id", "vmware_cbc_alert_note_text"], fn_inputs)

        app_common = AppCommon(PACKAGE_NAME, self.options)

        results, error_msg = app_common.post_alert_note(fn_inputs.vmware_cbc_alert_id, 
                                                         clean_html(fn_inputs.vmware_cbc_alert_note_text),
                                                         comment_header=SOAR_HEADER)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)