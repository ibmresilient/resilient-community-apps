# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_delete_schedule"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_delete_schedule'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Delete the schedule identified by schedule name.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.schedule_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "schedule_name"], fn_inputs)

        # Log inputs
        self.LOG.info(f"Azure Automation Account Name: {getattr(fn_inputs, 'account_name', None)}")
        self.LOG.info(f"Azure Automation Resource Group Name: {getattr(fn_inputs, 'resource_group_name', None)}")
        self.LOG.info(f'Schedule Name: {getattr(fn_inputs, "schedule_name", None)}')

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Make call to Azure and retrieve results
        response = client.delete_schedule(getattr(fn_inputs, "schedule_name", None))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult({"status": response.status_code}, reason=response.text)
