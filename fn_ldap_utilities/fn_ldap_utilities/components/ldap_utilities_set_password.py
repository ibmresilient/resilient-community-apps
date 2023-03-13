# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from random import sample
from string import ascii_letters, digits

from ldap3 import MODIFY_REPLACE
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

from fn_ldap_utilities.util.helper import (PACKAGE_NAME, LDAPUtilitiesHelper,
                                           get_domains_list)
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

FN_NAME = "ldap_utilities_set_password"
DEFAULT_MAX_PASSWORD_LEN = 12
FN_NAME = "ldap_utilities_set_password"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'ldap_utilities_set_password'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.domains_list = get_domains_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that allows you to set a new password for an LDAP entry given the entry's DN
        Inputs:
            -   fn_inputs.ldap_domain_name
            -   fn_inputs.ldap_dn
            -   fn_inputs.ldap_new_password
            -   fn_inputs.ldap_new_auto_password_len
            -   fn_inputs.ldap_return_new_password
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate that required fields are given
        validate_fields(["ldap_dn"], fn_inputs)

        # Get function inputs
        ldap_domain_name = getattr(fn_inputs, "ldap_domain_name", "") # text
        ldap_dn = getattr(fn_inputs, "ldap_dn") # text (required)
        ldap_new_password = getattr(fn_inputs, "ldap_new_password") # text
        ldap_new_auto_password_len = getattr(fn_inputs, "ldap_new_auto_password_len", DEFAULT_MAX_PASSWORD_LEN) # int Default length is 12
        ldap_return_new_password = getattr(fn_inputs, "ldap_return_new_password") # boolean

        self.LOG.info(f"LDAP Domain Name: {ldap_domain_name}")
        self.LOG.info(f"LDAP DN: {ldap_dn}")
        self.LOG.debug(f"ldap_new_auto_password_len: {ldap_new_auto_password_len}")
        self.LOG.info(f"ldap_return_new_password: {ldap_return_new_password}")

        # Initiate variable, so that it does not error when called
        c = ""

        # Instansiate helper (which gets appconfigs from file)
        ldap = LDAPDomains(self.opts)
        helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

        # Instansiate LDAP Server and Connection
        c = helper.get_ldap_connection()

        try:
            # Bind to the connection
            c.bind()
        except Exception as err:
            raise ValueError(
                f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

        # Inform user
        yield self.status_message(f"Connected to {'Active Directory' if helper.LDAP_IS_ACTIVE_DIRECTORY else 'LDAP Server'}")

        # If ldap_new_password empty, auto-generate pwd with length ldap_new_auto_password_len. If ldap_new_auto_password_len empty, creates 12 char length pwd.
        if not ldap_new_password:
            ldap_new_password = "".join(sample(str(ascii_letters+digits+'*#$%&/-_!?'), int(ldap_new_auto_password_len)))

        # If the call to LDAP is successful
        success = False

        try:
            yield self.status_message("Attempting to change password")
            if helper.LDAP_IS_ACTIVE_DIRECTORY:
                success = c.extend.microsoft.modify_password(str(ldap_dn), ldap_new_password)
            else:
                success = c.modify(ldap_dn, {'userPassword': [(MODIFY_REPLACE, [ldap_new_password])]})

        except Exception as err:
            self.LOG.debug(f"Error: {err}")
            raise ValueError("Could not change password. Check ldap_dn are valid")

        finally:
            # Unbind connection
            c.unbind()

        results = {
            "user_dn": ldap_dn,
            "ldap_new_password": ldap_new_password if ldap_return_new_password else None
        }

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=success)
