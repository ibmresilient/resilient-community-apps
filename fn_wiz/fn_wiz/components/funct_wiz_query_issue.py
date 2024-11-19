# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
# Generated with resilient-sdk v51.0.1.0.695

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_wiz.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "wiz_query_issue"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'wiz_query_issue'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Enrich case data with issue data
        Inputs:
            -   fn_inputs.wiz_issue_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["wiz_issue_id"], fn_inputs)

        app_common = AppCommon(self.rc, PACKAGE_NAME, self.options)
        response = app_common.get_issue(fn_inputs.wiz_issue_id)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        results = {"response": response}

        yield FunctionResult(results)
