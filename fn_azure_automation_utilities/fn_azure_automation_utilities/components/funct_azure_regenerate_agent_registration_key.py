# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v49.1.51

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME
from ast import literal_eval

FN_NAME = "azure_regenerate_agent_registration_key"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_regenerate_agent_registration_key'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Regenerate a primary or secondary agent registration key
        Inputs:
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.input_parameters
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name"], fn_inputs)
        # fn_inputs.input_parameters is a string dictionary. Convert it into a dictionary from a string.
        input_parameters = literal_eval(getattr(fn_inputs, "input_parameters", "{}"))

        # Log inputs
        self.LOG.info(f"Azure Automation Account Name: {getattr(fn_inputs, 'account_name', None)}")
        self.LOG.info(f"Azure Automation Resource Group Name: {getattr(fn_inputs, 'resource_group_name', None)}")
        self.LOG.info(f'Input Parameters: {str(input_parameters)}')

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Make call to Azure and retrieve results
        results = client.regenerate_account_registration_key(input_parameters)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
