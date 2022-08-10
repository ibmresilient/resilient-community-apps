# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""AppFunction implementation"""

from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from fn_mcafee_epo.lib.epo_helper import init_client, PACKAGE_NAME
from resilient_lib import validate_fields

FN_NAME = "mcafee_epo_add_user"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'mcafee_epo_add_user'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.opts = opts
        self.options = opts.get(PACKAGE_NAME, {})

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Add a user to the ePO server
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

        yield self.status_message("Starting App Function: '{}'".format(FN_NAME))

        # Get the function parameters:
        validate_fields(
            ["mcafee_epo_username", "mcafee_epo_pass"], fn_inputs)

        # Set parameters
        username = fn_inputs.mcafee_epo_username
        password = fn_inputs.mcafee_epo_pass if hasattr(fn_inputs, "mcafee_epo_pass") else None
        fullname = fn_inputs.mcafee_epo_fullname if hasattr(fn_inputs, "mcafee_epo_fullname") else None
        email = fn_inputs.mcafee_epo_email if hasattr(fn_inputs, "mcafee_epo_email") else None
        phonenumber = fn_inputs.mcafee_epo_phonenumber if hasattr(fn_inputs, "mcafee_epo_phonenumber") else None
        notes = fn_inputs.mcafee_epo_notes if hasattr(fn_inputs, "mcafee_epo_notes") else None
        allowed_ips = fn_inputs.mcafee_epo_allowed_ips if hasattr(fn_inputs, "mcafee_epo_allowed_ips") else None
        user_disabled = fn_inputs.mcafee_epo_user_disabled if hasattr(fn_inputs, "mcafee_epo_user_disabled") else False
        admin = fn_inputs.mcafee_epo_admin if hasattr(fn_inputs, "mcafee_epo_admin") else False

        # Log parameters
        self.LOG.info("mcafee_epo_username: %s", username)
        self.LOG.info("mcafee_epo_fullname: %s", fullname)
        self.LOG.info("mcafee_epo_email: %s", email)
        self.LOG.info("mcafee_epo_phonenumber: %s", phonenumber)
        self.LOG.info("mcafee_epo_notes: %s", notes)
        self.LOG.info("mcafee_epo_allowed_ips: %s", allowed_ips)
        self.LOG.info("mcafee_epo_user_disabled: %s", user_disabled)
        self.LOG.info("mcafee_epo_admin: %s", admin)

        # Connect to ePO server
        client = init_client(self.opts, self.options)

        response = client.request(
            "core.addUser",
            {"userName": username,
             "password": password,
             "fullName": fullname,
             "email": email,
             "phoneNumber": phonenumber,
             "notes": notes,
             "allowedIPs": allowed_ips,
             "disabled": user_disabled,
             "admin": admin
             }
        )

        yield self.status_message("Finished running App Function: '{}'".format(FN_NAME))

        yield FunctionResult(response)
