# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME, clear

FN_NAME = "mcafee_epo_get_all_users"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_get_all_users'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Get all the users on a ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_permsetname
            -   fn_inputs.datatable_name
            -   fn_inputs.incident_id
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Set parameters
        permsetname = fn_inputs.mcafee_epo_permsetname if hasattr(fn_inputs, "mcafee_epo_permsetname") else None
        datatable = fn_inputs.datatable_name if hasattr(fn_inputs, "datatable_name") else None
        incident_id = fn_inputs.incident_id if hasattr(fn_inputs, "incident_id") else None

        # Log parameters
        self.LOG.info("mcafee_epo_permsetname: %s", permsetname)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.listUsers",
            {"permSetName": permsetname}
        )

        # Clear datatable if requires params are given
        if datatable and incident_id:
            clear(self.rest_client(), datatable, incident_id)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
