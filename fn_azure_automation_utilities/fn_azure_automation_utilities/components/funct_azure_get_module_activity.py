# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_get_module_activity"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_get_module_activity'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Retrieve the activity in the module identified by module name and activity name or Retrieve a list of activities in the module identified by module name.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.activity_name
            -   fn_inputs.module_name
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "module_name"], fn_inputs)

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # If activity name given then get the given activity
        if getattr(fn_inputs, "activity_name", None):
            results = client.get_module_activity(getattr(fn_inputs, "module_name", None), getattr(fn_inputs, "activity_name", None))
        else: # If activity name not given then get all activities in the given module
            results = client.list_module_activities(getattr(fn_inputs, "module_name", None))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
