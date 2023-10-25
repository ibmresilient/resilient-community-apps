# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_get_credential"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_get_credential'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get credential from given credential name or list all credentials on given resource group.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.credential_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name"], fn_inputs)

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # If credential name given get that credential
        if getattr(fn_inputs, "credential_name", None):
            results = client.get_credential(getattr(fn_inputs, "credential_name", None))
        else: # If credential name not given get all credentials on given resource
            results = client.list_credentials_by_automation_account().get("value", [])

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
