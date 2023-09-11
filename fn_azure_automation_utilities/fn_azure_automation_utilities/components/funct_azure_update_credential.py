# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import AzureClient, PACKAGE_NAME
from ast import literal_eval

FN_NAME = "azure_update_credential"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_update_credential'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update a credential
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.input_parameters
            -   fn_inputs.credential_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "input_parameters", "credential_name"], fn_inputs)
        input_parameters = literal_eval(getattr(fn_inputs, "input_parameters", "{}"))
        if not input_parameters.get("properties", {}).get("userName") and not input_parameters.get("properties", {}).get("password"):
            raise KeyError("Either Credential Username or Credential password have to be given.")

        # Connect to Azure
        client = AzureClient(
            self.rc,
            self.options.get("client_id"),
            self.options.get("client_secret"),
            self.options.get("tenant_id"),
            self.options.get("subscription_id"),
            self.options.get("scope"),
            self.rc.get_proxies(),
            getattr(fn_inputs, "resource_group_name", None),
            getattr(fn_inputs, "account_name", None),
            refresh_token=self.options.get("refresh_token")
        )

        results = client.update_credential(getattr(fn_inputs, "credential_name"), input_parameters)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
