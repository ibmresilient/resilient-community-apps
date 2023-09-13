# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# Generated with resilient-sdk v50.0.151

"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields
from fn_azure_automation_utilities.util.helper import get_azure_client, PACKAGE_NAME

FN_NAME = "azure_get_node_report"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'azure_get_node_report'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Retrieve the Dsc node report data by node id and report id.
        Inputs:
            -   fn_inputs.report_id
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.node_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "report_id", "node_id"], fn_inputs)

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # Make call to Azure and retrieve results
        results = client.get_node_report(getattr(fn_inputs, "node_id"), getattr(fn_inputs, "report_id"))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
