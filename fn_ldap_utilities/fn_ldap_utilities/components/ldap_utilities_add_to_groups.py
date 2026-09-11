# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from ast import literal_eval

from ldap3.extend.microsoft.addMembersToGroups import \
    ad_add_members_to_groups as ad_add_members_to_groups
from resilient_circuits import (AppFunctionComponent, FunctionError,
                                FunctionResult, app_function)
from resilient_lib import validate_fields

from fn_ldap_utilities.util.helper import (PACKAGE_NAME, LDAPUtilitiesHelper,
                                           get_domains_list)
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

FN_NAME = "ldap_utilities_add_to_groups"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'ldap_utilities_add_to_groups'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.domains_list = get_domains_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that allows adding multiple users to multiple groups
        Inputs:
            -   fn_inputs.ldap_domain_name
            -   fn_inputs.ldap_multiple_user_dn
            -   fn_inputs.ldap_multiple_group_dn
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate that required fields are given
        validate_fields(["ldap_multiple_user_dn", "ldap_multiple_group_dn"], fn_inputs)

        # Get function inputs
        ldap_domain_name = getattr(fn_inputs, "ldap_domain_name", "") # text
        input_ldap_multiple_user_dn_asString = getattr(fn_inputs, "ldap_multiple_user_dn", None) # text (required) [string representation of an array]
        input_ldap_multiple_group_dn_asString = getattr(fn_inputs, "ldap_multiple_group_dn", None) # text (required) [string representation of an array]

        self.LOG.info(f"LDAP Domain Name: {ldap_domain_name}")
        self.LOG.info(f"LDAP User DN: {input_ldap_multiple_user_dn_asString}")
        self.LOG.info(f"LDAP Group DN: {input_ldap_multiple_group_dn_asString}")

        # Initiate variable, so that it does not error when called
        c = ""

        # Instantiate helper (which gets app.configs from file)
        ldap = LDAPDomains(self.opts)
        helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

        if not helper.LDAP_IS_ACTIVE_DIRECTORY:
            raise FunctionError(
                "This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

        try:
            # Try converting input to an array
            input_ldap_multiple_user_dn = literal_eval(input_ldap_multiple_user_dn_asString)
            input_ldap_multiple_group_dn = literal_eval(input_ldap_multiple_group_dn_asString)

        except Exception:
            raise ValueError(
                """input_ldap_multiple_user_dn and input_ldap_multiple_group_dn must be a string representation of an array e.g. "['dn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']" """)

        # Instantiate LDAP Server and Connection
        c = helper.get_ldap_connection()

        try:
            # Bind to the connection
            c.bind()
        except Exception as err:
            raise ValueError(
                f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

        # Inform user
        yield self.status_message("Connected to Active Directory")

        # If the call LDAP was successful
        success = False

        try:
            yield self.status_message("Attempting to add user(s) to group(s)")
            # Perform the removeMembersFromGroups operation
            success = ad_add_members_to_groups(c, input_ldap_multiple_user_dn, input_ldap_multiple_group_dn, True)

        except Exception as err:
            self.LOG.error(f"Error: {err}")
            raise ValueError("Ensure all user and group DNs exist")

        finally:
            # Unbind connection
            c.unbind()

        results = {
            "users_dn": input_ldap_multiple_user_dn,
            "groups_dn": input_ldap_multiple_group_dn
        }

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=success)
