# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_get_account"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_get_account'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get a specified Azure automation account information or list accounts.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # If account name given then get information for that account
        if getattr(fn_inputs, "account_name", None):
            # Validate inputs
            validate_fields(["resource_group_name"], fn_inputs)
            results = client.get_account()
        else: # If no account name given then list all accounts
            results = results = client.list_accounts().get("value", [])

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
