# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_add_user"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_add_user'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add a user to the ePO server. McAfee user requires administrator rights for this function.
        Inputs:
            -   fn_inputs.mcafee_epo_phone_number
            -   fn_inputs.mcafee_epo_username
            -   fn_inputs.mcafee_epo_fullname
            -   fn_inputs.mcafee_epo_user_disabled
            -   fn_inputs.mcafee_epo_notes
            -   fn_inputs.mcafee_epo_admin
            -   fn_inputs.mcafee_epo_email
            -   fn_inputs.mcafee_epo_allowed_ips
            -   fn_inputs.mcafee_epo_pass
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate required parameters
        validate_fields(["mcafee_epo_username", "mcafee_epo_pass"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.addUser",
            {"userName": fn_inputs.mcafee_epo_username,
             "password": getattr(fn_inputs, "mcafee_epo_pass", None),
             "fullName": getattr(fn_inputs, "mcafee_epo_fullname", None),
             "email": getattr(fn_inputs, "mcafee_epo_email", None),
             "phoneNumber": getattr(fn_inputs, "mcafee_epo_phone_number", None),
             "notes": getattr(fn_inputs, "mcafee_epo_notes", None),
             "allowedIPs": getattr(fn_inputs, "mcafee_epo_allowed_ips", None),
             "disabled": getattr(fn_inputs, "mcafee_epo_user_disabled", False),
             "admin": getattr(fn_inputs, "mcafee_epo_admin", False)}
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
