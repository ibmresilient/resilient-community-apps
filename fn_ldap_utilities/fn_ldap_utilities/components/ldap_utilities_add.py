# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from ast import literal_eval

from ldap3.core.exceptions import (LDAPEntryAlreadyExistsResult,
                                   LDAPObjectClassError)
from ldap3.extend.microsoft.addMembersToGroups import ad_add_members_to_groups
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import IntegrationError, validate_fields

from fn_ldap_utilities.util.helper import (PACKAGE_NAME, LDAPUtilitiesHelper,
                                           get_domains_list)
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

FN_NAME = "ldap_utilities_add"

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'ldap_utilities_add'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.domains_list = get_domains_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that allows you to add users, groups and organizational units to LDAP
        Inputs:
            -   fn_inputs.ldap_domain_name
            -   fn_inputs.ldap_dn
            -   fn_inputs.ldap_attribute_name_values
            -   fn_inputs.ldap_multiple_group_dn
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate that required fields are given
        validate_fields(["ldap_dn"], fn_inputs)

        ldap_domain_name = getattr(fn_inputs, "ldap_domain_name", "") # text
        ldap_dn = getattr(fn_inputs, "ldap_dn") # text (required)
        attribute_list = getattr(fn_inputs, "ldap_attribute_name_values") # text
        group_list = getattr(fn_inputs, "ldap_multiple_group_dn") # text

        try:
            # Try converting input to an dictionary
            attribute_list = literal_eval("{{ {} }}".format(attribute_list))\
                if attribute_list else {'objectClass': 'user'}
        except Exception:
            raise IntegrationError('ldap_attribute_name_values incorrectly specified e.g. "attribute1": "value1", "attribute2": "value2", "objectClass": "Users"')

        try:
            group_list = literal_eval(group_list) if group_list else []
        except Exception:
            raise IntegrationError("""ldap_multiple_group_dn incorrectly specified e.g. "['cn=Accounts Group,dc=example,dc=com', 'dn=IT Group,dc=example,dc=com']" """)

        self.LOG.info(f"LDAP Domain Name: {ldap_domain_name}")
        self.LOG.info(f"LDAP DN: {ldap_dn}",)
        self.LOG.info(f"ldap_attribute_name_values: {attribute_list}")
        self.LOG.info(f"ldap_multiple_group_dn: {group_list}")

        # Initiate variable, so that it does not error when called
        conn = ""

        # Instansiate helper (which gets appconfigs from file)
        ldap = LDAPDomains(self.opts)
        helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

        # Instantiate LDAP Server and Connection
        conn = helper.get_ldap_connection()
        try:
            # Bind to the connection
            conn.bind()
        except Exception as err:
            raise ValueError(f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

        # Inform user
        yield self.status_message(f"Connected to {'Active Directory' if helper.LDAP_IS_ACTIVE_DIRECTORY else 'LDAP Server'}")

        try:
            yield self.status_message("Attempting to execute add")

            conn.add(ldap_dn, attributes=attribute_list)
            result = conn.result

            try:
                if result.get('description', '') == 'success' and group_list:
                    yield self.status_message("Attempting to execute group add")
                    ad_add_members_to_groups(conn, [ldap_dn], group_list, True)
            except Exception as err:
                raise IntegrationError(f"Unable to add: {ldap_dn} to group(s): {group_list}")
        except LDAPObjectClassError:
            raise ValueError("objectClass is needed in attribute input, EX: 'objectClass': 'user'")
        except LDAPEntryAlreadyExistsResult:
            raise ValueError("User already exists")
        except Exception as err:
            self.LOG.debug(f'Error: {err}')
            raise ValueError("Ensure dn is correct")
        finally:
            # Unbind connection
            if conn:
                conn.unbind()

        # If the call to LDAP was successful
        success = True if result.get('description', '') == 'success' else False

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(result, success=success)
