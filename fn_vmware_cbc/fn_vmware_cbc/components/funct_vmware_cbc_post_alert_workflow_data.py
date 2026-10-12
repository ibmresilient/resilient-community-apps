# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, clean_html
from fn_vmware_cbc.lib.app_common import (AppCommon, PACKAGE_NAME, SOAR_HEADER)

PACKAGE_NAME = "fn_vmware_cbc"
FN_NAME = "vmware_cbc_post_alert_workflow_data"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'vmware_cbc_post_alert_workflow_data'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the alert workflow information in VMware Carbon Black Cloud.
        Inputs:
            -   fn_inputs.vmware_cbc_determination
            -   fn_inputs.vmware_cbc_status
            -   fn_inputs.vmware_cbc_note_text
            -   fn_inputs.vmware_cbc_alert_id
            -   fn_inputs.vmware_cbc_closure_reason
        """

        validate_fields(["vmware_cbc_alert_id"], fn_inputs)

        # Set optional params to None if not specified.
        # None value sent to CBC does not change the value in CBC.
        status = getattr(fn_inputs, "vmware_cbc_status", None)
        determination = getattr(fn_inputs, "vmware_cbc_determination", None)
        closure_reason = getattr(fn_inputs, "vmware_cbc_closure_reason", None)
        note_text = getattr(fn_inputs, "vmware_cbc_note_text", None)

        app_common = AppCommon(PACKAGE_NAME, self.options)

        results, error_msg = app_common.post_alert_workflow_data(
                                            alert_id=fn_inputs.vmware_cbc_alert_id,
                                            status=status,
                                            determination=determination,
                                            closure_reason=closure_reason,
                                            note_text=clean_html(note_text),
                                            comment_header=SOAR_HEADER)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results, success=False if error_msg else True, reason=error_msg)
