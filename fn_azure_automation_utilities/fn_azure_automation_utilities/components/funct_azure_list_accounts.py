# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import AzureClient, PACKAGE_NAME

FN_NAME = "azure_list_accounts"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_list_accounts'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Lists the Automation Accounts within an Azure subscription
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Connect to Azure
        client = AzureClient(
            self.rc,
            self.options.get("client_id"),
            self.options.get("client_secret"),
            self.options.get("tenant_id"),
            self.options.get("subscription_id"),
            self.options.get("scope"),
            self.rc.get_proxies(),
            refresh_token=self.options.get("refresh_token")
        )

        # Make call to Azure to list automation accounts
        results = client.list_accounts()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
