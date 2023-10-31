# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
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
        Function: Retrieve the Dsc node report data by node id and report id or
        List Dsc node reports by node id.
        Inputs:
            -   fn_inputs.report_id
            -   fn_inputs.resource_group_name
            -   fn_inputs.account_name
            -   fn_inputs.node_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate inputs
        validate_fields(["account_name", "resource_group_name", "node_id"], fn_inputs)

        # Connect to Azure
        client = get_azure_client(self.rc, self.options, getattr(fn_inputs, "resource_group_name", None), getattr(fn_inputs, "account_name", None))

        # If report id given then get the specified node report
        if getattr(fn_inputs, "report_id", None):
            results = client.get_node_report(getattr(fn_inputs, "node_id", None), getattr(fn_inputs, "report_id", None))
        else: # If report id not given then list all reports on the specified node
            results = client.list_node_report_by_node(getattr(fn_inputs, "node_id", None))

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        yield FunctionResult(results)
