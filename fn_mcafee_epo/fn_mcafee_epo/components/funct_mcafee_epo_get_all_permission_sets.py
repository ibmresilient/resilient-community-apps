# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
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
        Function: Get all of the permission sets on an ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_username
            -   fn_inputs.datatable_name
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Set parameters
        username = fn_inputs.mcafee_epo_username if hasattr(fn_inputs, "mcafee_epo_username") else None
        datatable = fn_inputs.datatable_name if hasattr(fn_inputs, "datatable_name") else None
        incident_id = fn_inputs.incident_id if hasattr(fn_inputs, "incident_id") else None

        # Log parameters
        self.LOG.info("mcafee_epo_username: %s", username)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.listPermSets",
            {"userName": username}
        )

        # Clear datatable if requires params are given
        if datatable and incident_id:
            clear(self.rest_client(), datatable, incident_id)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
