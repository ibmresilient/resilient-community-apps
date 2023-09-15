# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME
from ast import literal_eval

FN_NAME = "azure_execute_runbook"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_execute_runbook'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Execute a given Azure runbook and retrieve the results
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.input_parameters
            -   fn_inputs.runbook_name
            -   fn_inputs.time_to_wait
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "runbook_name"], fn_inputs)
        # fn_inputs.input_parameters is a string dictionary. Convert it into a dictionary from a string.
        input_parameters = literal_eval(getattr(fn_inputs, "input_parameters", "{}"))
        time_to_wait = getattr(fn_inputs, "time_to_wait", 30)

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Start an Azure job to run the given runbook
        start_runbook = client.run_runbook(getattr(fn_inputs, "runbook_name"), runbook_parameters=input_parameters)
        job_name = start_runbook.get("name")
        # Wait a given amount of time and then get the status of the Azure run job started above. When the status equals Completed return that status
        _ = client.get_job_final_status(job_name, time_to_wait)
        # Get the results from the completed Azure runbook
        results = client.get_job_results(job_name)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
