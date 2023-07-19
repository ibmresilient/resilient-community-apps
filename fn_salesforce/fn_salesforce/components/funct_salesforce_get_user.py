# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_salesforce.lib.app_common import AppCommon

PACKAGE_NAME = "fn_salesforce"
FN_NAME = "salesforce_get_user"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_get_user'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the detailed information of a Salesforce User, given the UserId.
        Inputs:
            -   fn_inputs.salesforce_user_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["salesforce_user_id"], fn_inputs)

        app_common = AppCommon(self.rc, self.PACKAGE_NAME, self.options)

        response = app_common.get_user(fn_inputs.salesforce_user_id)

        results = {"salesforce_user": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)


