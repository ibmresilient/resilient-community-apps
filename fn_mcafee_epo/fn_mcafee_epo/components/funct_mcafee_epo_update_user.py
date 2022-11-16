# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_update_user"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_update_user'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Update a user on the ePO server
        Inputs:
            -   fn_inputs.mcafee_epo_phone_number
            -   fn_inputs.mcafee_epo_windowsdomain
            -   fn_inputs.mcafee_epo_subjectdn
            -   fn_inputs.mcafee_epo_username
            -   fn_inputs.mcafee_epo_windowsusername
            -   fn_inputs.mcafee_epo_new_username
            -   fn_inputs.mcafee_epo_fullname
            -   fn_inputs.mcafee_epo_user_disabled
            -   fn_inputs.mcafee_epo_notes
            -   fn_inputs.mcafee_epo_admin
            -   fn_inputs.mcafee_epo_email
            -   fn_inputs.mcafee_epo_allowed_ips
            -   fn_inputs.mcafee_epo_pass
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Get the function parameters:
        validate_fields(["mcafee_epo_username"], fn_inputs)

        # Log parameters
        self.LOG.info(str(fn_inputs))

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.updateUser",
            {"userName": fn_inputs.mcafee_epo_username,
             "password": getattr(fn_inputs, "mcafee_epo_pass", None),
             "windowsUserName": getattr(fn_inputs, "mcafee_epo_windowsusername", None),
             "windowsDomain": getattr(fn_inputs, "mcafee_epo_windowsdomain", None),
             "subjectDN": getattr(fn_inputs, "mcafee_epo_subjectdn", None),
             "newUserName": getattr(fn_inputs, "mcafee_epo_new_username", None),
             "fullName": getattr(fn_inputs, "mcafee_epo_fullname", None),
             "email": getattr(fn_inputs, "mcafee_epo_email", None),
             "phoneNumber": getattr(fn_inputs, "mcafee_epo_phone_number", None),
             "notes": getattr(fn_inputs, "mcafee_epo_notes", None),
             "allowedIPs": getattr(fn_inputs, "mcafee_epo_allowed_ips", None),
             "disabled": getattr(fn_inputs, "mcafee_epo_user_disabled", None),
             "admin": getattr(fn_inputs, "mcafee_epo_admin", None)}
        )

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(response)
