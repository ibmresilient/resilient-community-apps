# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME
from ast import literal_eval
from datetime import datetime

FN_NAME = "azure_create_schedule"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_create_schedule'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create a schedule.
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.input_parameters
            -   fn_inputs.schedule_name
            -   fn_inputs.schedule_update
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "input_parameters", "schedule_name"], fn_inputs)
        # fn_inputs.input_parameters is a string dictionary. Convert it into a dictionary from a string.
        input_parameters = literal_eval(getattr(fn_inputs, "input_parameters", "{}"))
        if input_parameters.get("properties", {}).get("startTime"):
            # Convert startTime to the correct format. Milliseconds are removed from the time.
            start_time = datetime.fromtimestamp(input_parameters.get("properties", {}).get("startTime") / 1e3)
            input_parameters["properties"]["startTime"] = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Make call to Azure and retrieve results
        results = client.create_schedule(getattr(fn_inputs, "schedule_name", None), input_parameters)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
