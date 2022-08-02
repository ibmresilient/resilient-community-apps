# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME

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
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Log parameters
        self.LOG.info("mcafee_epo_permsetname: %s", fn_inputs.mcafee_epo_permsetname if hasattr(fn_inputs, "mcafee_epo_permsetname") else None)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(client.request(
            "core.listUsers",
            {"permSetName": fn_inputs.mcafee_epo_permsetname}
        ))
