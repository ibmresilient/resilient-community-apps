# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_get_runbook"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_get_runbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Retrieve the runbook identified by runbook name or list runbooks on given account.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.runbook_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name"], fn_inputs)

        # Log inputs
        self.LOG.info(f"Azure Automation Account Name: {getattr(fn_inputs, 'account_name', None)}")
        self.LOG.info(f"Azure Automation Resource Group Name: {getattr(fn_inputs, 'resource_group_name', None)}")
        self.LOG.info(f'Runbook Name: {getattr(fn_inputs, "runbook_name", None)}')

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # If runbook_name given then get that runbook
        if getattr(fn_inputs, "runbook_name", None):
            results = client.get_runbook(getattr(fn_inputs, "runbook_name", None))
        else: # If runbook_name not given then list all runbooks on given account
            results = client.list_runbooks_by_automation_account()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
