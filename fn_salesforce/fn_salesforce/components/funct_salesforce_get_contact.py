# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_salesforce.lib.app_common import (AppCommon, PACKAGE_NAME)

FN_NAME = "salesforce_get_contact"


class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'salesforce_get_contact'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get the detailed information on the specified Salesforce Contact, give the ContactId.
        Inputs:
            -   fn_inputs.salesforce_contact_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        validate_fields(["salesforce_contact_id"], fn_inputs)

        if fn_inputs.salesforce_contact_id:
            app_common = AppCommon(self.PACKAGE_NAME, self.options)

            response = app_common.get_contact(fn_inputs.salesforce_contact_id)
        else:
            response = None
            
        results = {"salesforce_contact": response}

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)

