# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from ldap3 import MODIFY_REPLACE
from resilient_circuits import (AppFunctionComponent, FunctionError,
                                FunctionResult, app_function)
from resilient_lib import validate_fields

from fn_ldap_utilities.util.helper import (PACKAGE_NAME, LDAPUtilitiesHelper,
                                           get_domains_list)
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

FN_NAME = "ldap_utilities_toggle_access"
ldap_user_account_control_enabled = 512
ldap_user_account_control_disabled = 514

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'ldap_utilities_toggle_access"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.domains_list = get_domains_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that allows an LDAP user, with the correct privileges to enable or disable another user given their DN
        Inputs:
            -   fn_inputs.ldap_domain_name
            -   fn_inputs.ldap_dn
            -   fn_inputs.ldap_toggle_access
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate that required fields are given
        validate_fields(["ldap_dn", "ldap_toggle_access"], fn_inputs)

        # Get function inputs
        ldap_domain_name = getattr(fn_inputs, "ldap_domain_name", "") # text
        ldap_dn = getattr(fn_inputs, "ldap_dn", None) # text (required)
        ldap_toggle_access = getattr(fn_inputs, "ldap_toggle_access", None) # select, values: "Enable", "Disable" (required)

        self.LOG.info(f"LDAP Domain Name: {ldap_domain_name}")
        self.LOG.info(f"LDAP DN: {ldap_dn}")
        self.LOG.info(f"LDAP Toggle Access: {ldap_toggle_access}")

        # Initiate variable, so that it does not error when called
        c = ""

        # Instantiate helper (which gets app configs from file)
        ldap = LDAPDomains(self.opts)
        helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

        if not helper.LDAP_IS_ACTIVE_DIRECTORY:
            raise FunctionError(
                "This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

        # Set local vars
        ldap_user_account_control_attribute = "userAccountControl"

        if (ldap_toggle_access.lower() == 'enable'):
            ldap_user_account_control_value = ldap_user_account_control_enabled

        elif (ldap_toggle_access.lower() == 'disable'):
            ldap_user_account_control_value = ldap_user_account_control_disabled

        else:
            raise ValueError("ldap_toggle_access function input must be 'Enable' or 'Disable'")

        # Instantiate LDAP Server and Connection
        c = helper.get_ldap_connection()

        try:
            # Bind to the connection
            c.bind()
        except Exception as err:
            raise ValueError(
                f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

        # Inform user
        yield self.status_message(f"Connected to {'Active Directory' if helper.LDAP_IS_ACTIVE_DIRECTORY else 'LDAP Server'}")

        # If the call to LDAP is successful
        success = False
        try:
            yield self.status_message(f"Attempting to {ldap_toggle_access} {ldap_dn}")
            # Perform the Modify operation
            success = c.modify(ldap_dn, {ldap_user_account_control_attribute: [(MODIFY_REPLACE, [ldap_user_account_control_value])]})

        except Exception as err:
            self.LOG.error(f"Error: {err}")
            raise ValueError("Could not toggle access for this user. Ensue ldap_dn is valid")

        finally:
            # Unbind connection
            c.unbind()

        results = {
            "user_dn": ldap_dn,
            "user_status": ldap_toggle_access
        }

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=success)
