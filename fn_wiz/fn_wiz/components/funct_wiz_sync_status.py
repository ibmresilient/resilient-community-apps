# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import IntegrationError, validate_fields, clean_html
from fn_wiz.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "wiz_sync_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'wiz_sync_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update Wiz issue status if case status changed
        Inputs:
            -   fn_inputs.wiz_issue_id
            -   fn_inputs.wiz_resolution_reason
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["wiz_issue_id", "wiz_resolution_reason"], fn_inputs)
        res_summary = getattr(fn_inputs, "wiz_resolution_summary", None)

        self.LOG.info("Closing Wiz issue %s because corresponding SOAR case closed.", fn_inputs.wiz_issue_id)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)
        response = app_common.sync_status_with_wiz(fn_inputs.wiz_issue_id, fn_inputs.wiz_resolution_reason, clean_html(res_summary))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"response": response}

        yield FunctionResult(results)
