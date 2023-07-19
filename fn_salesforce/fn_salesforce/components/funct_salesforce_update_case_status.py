# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_salesforce.lib.app_common import AppCommon

PACKAGE_NAME = "fn_salesforce"
FN_NAME = "salesforce_update_case_status"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_update_case_status'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update the Status field of a case in Salesforce.
        Inputs:
            -   fn_inputs.salesforce_case_id
            -   fn_inputs.salesforce_case_status
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["salesforce_case_id", "salesforce_case_status"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        results = app_common.update_case_status(fn_inputs.salesforce_case_id, 
                                                fn_inputs.salesforce_case_status)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

