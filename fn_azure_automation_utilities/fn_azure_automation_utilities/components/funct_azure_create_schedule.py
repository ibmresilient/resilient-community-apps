# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
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

    def convertTime(self, time_to_convert):
        """
        Convert time_to_convert to the correct format. Milliseconds are removed from the time.
        """
        time_to_convert = datetime.fromtimestamp(time_to_convert / 1e3)
        return time_to_convert.strftime("%Y-%m-%dT%H:%M:%SZ")

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Create or update a schedule.
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
        # Convert startTime to the correct date time format.
        if input_parameters.get("properties", {}).get("startTime", None):
            input_parameters["properties"]["startTime"] = self.convertTime(input_parameters.get("properties", {}).get("startTime"))
        # If expiryTime given convert it to the correct date time format.
        if input_parameters.get("properties", {}).get("expiryTime", None):
            input_parameters["properties"]["expiryTime"] = self.convertTime(input_parameters.get("properties", {}).get("expiryTime", None))

        # Log inputs
        self.LOG.info(f"Azure Automation Account Name: {getattr(fn_inputs, 'account_name', None)}")
        self.LOG.info(f"Azure Automation Resource Group Name: {getattr(fn_inputs, 'resource_group_name', None)}")
        self.LOG.info(f'Schedule Name: {getattr(fn_inputs, "schedule_name", None)}')
        self.LOG.info(f'Input Parameters: {str(input_parameters)}')
        self.LOG.info(f'Schedule Update: {getattr(fn_inputs, "schedule_update", False)}')

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Make call to Azure and retrieve results
        results = client.create_schedule(getattr(fn_inputs, "schedule_name", None), input_parameters, getattr(fn_inputs, "schedule_update", False))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
