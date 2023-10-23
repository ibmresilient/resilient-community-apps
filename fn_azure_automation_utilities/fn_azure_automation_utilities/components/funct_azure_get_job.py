# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_get_job"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_get_job'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Retrieve the job identified by job name or list jobs
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.job_name
            -   fn_inputs.job_results
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name"], fn_inputs)

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # If job_name is given either get job output or job information
        if getattr(fn_inputs, "job_name", None):
            # If job_output equal True then return given job output
            if getattr(fn_inputs, "job_output", False):
                results = client.get_job_results(getattr(fn_inputs, "job_name", None))
            else: # If job_output equals False then return job information
                results = client.get_job(getattr(fn_inputs, "job_name", None))
        else: # If job_name not given then list jobs
            results = client.list_jobs_by_automation_account()

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
