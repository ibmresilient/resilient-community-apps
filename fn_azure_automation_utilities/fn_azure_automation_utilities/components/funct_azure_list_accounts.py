# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

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
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Make call to Azure to list automation accounts
        results = client.list_accounts()

        # Make call to Azure and retrieve results
        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
