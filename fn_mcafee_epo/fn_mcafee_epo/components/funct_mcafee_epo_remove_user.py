# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_remove_user"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_remove_user'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Delete a user from the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_username
        """

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Validate parameters
        validate_fields(["mcafee_epo_username"], fn_inputs)

        # Log parameters
        self.LOG.info("mcafee_epo_username: %s", fn_inputs.mcafee_epo_username)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.removeUser",
            {"userName": fn_inputs.mcafee_epo_username}
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
