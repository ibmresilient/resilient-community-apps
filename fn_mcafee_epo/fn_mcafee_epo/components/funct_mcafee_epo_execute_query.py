# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME, clear
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult

FN_NAME = "mcafee_epo_execute_query"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_execute_query'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Execute a query on the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_target
            -   fn_inputs.mcafee_epo_queryid
            -   fn_inputs.mcafee_epo_query_select
            -   fn_inputs.mcafee_epo_query_group
            -   fn_inputs.mcafee_epo_query_order
            -   fn_inputs.datatable_name
            -   fn_inputs.incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Get function parameters:
        query_id = getattr(fn_inputs, "mcafee_epo_queryid", None)
        target = getattr(fn_inputs, "mcafee_epo_target", None)

        if query_id and target:
            raise ValueError("Define either mcafee_epo_queryid or mcafee_epo_target, but not both.")
        elif query_id:
            response = client.request(
                "core.executeQuery",
                {"queryId": query_id}
            )
        elif target:
            select = getattr(fn_inputs, "mcafee_epo_query_select", None)
            group = getattr(fn_inputs, "mcafee_epo_query_group", None)
            order = getattr(fn_inputs, "mcafee_epo_query_order", None)
            response = client.request(
                "core.executeQuery",
                {"target": target,
                 "select": f"(select {select})" if select else None,
                 "group": f"(group {group})" if group else None,
                 "order": f"(order ({order}))" if order else None}
            )
        else:
            raise ValueError("Either mcafee_epo_queryid or mcafee_epo_target have to be defined.")

        # Clear datatable if required params are given
        if hasattr(fn_inputs, "datatable_name") and hasattr(fn_inputs, "incident_id"):
            clear(self.rest_client(), fn_inputs.datatable_name, fn_inputs.incident_id)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
