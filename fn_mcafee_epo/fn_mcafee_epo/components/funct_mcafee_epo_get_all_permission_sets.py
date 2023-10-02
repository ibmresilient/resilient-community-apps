# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME, clear

FN_NAME = "mcafee_epo_get_all_permission_sets"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_get_all_permission_sets'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get all of the permission sets on an ePO server. McAfee user requires administrator rights for this function.
        Inputs:
            -   fn_inputs.mcafee_epo_username
            -   fn_inputs.datatable_name
            -   fn_inputs.incident_id
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.listPermSets",
            {"userName": getattr(fn_inputs, "mcafee_epo_username", None)}
        )

        # Clear datatable if required params are given
        if hasattr(fn_inputs, "datatable_name") and hasattr(fn_inputs, "incident_id"):
            clear(self.rest_client(), fn_inputs.datatable_name, fn_inputs.incident_id)

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
