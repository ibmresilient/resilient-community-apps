# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import AzureClient, PACKAGE_NAME

FN_NAME = "azure_delete_runbook"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_delete_runbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Delete the runbook by name.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.runbook_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "runbook_name"], fn_inputs)
        
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

        # Make call to Azure to delete given runbook
        response = client.delete_runbook(getattr(fn_inputs, "runbook_name"))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult({"status": response.status_code}, reason=response.text)
