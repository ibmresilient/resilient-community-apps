# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from ast import literal_eval

from ldap3 import MODIFY_REPLACE
from resilient_circuits import (AppFunctionComponent, FunctionResult,
                                app_function)
from resilient_lib import validate_fields

from fn_ldap_utilities.util.helper import (PACKAGE_NAME, LDAPUtilitiesHelper,
                                           get_domains_list)
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

FN_NAME = "ldap_utilities_update"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'ldap_utilities_update"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        self.domains_list = get_domains_list(opts)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: A function that updates the attribute of a DN with a new value
        Inputs:
            -   fn_inputs.ldap_domain_name
            -   fn_inputs.ldap_dn
            -   fn_inputs.ldap_attribute_name
            -   fn_inputs.ldap_attribute_values
        """
        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        # Validate that required fields are given
        validate_fields(["ldap_dn", "ldap_attribute_name", "ldap_attribute_values"], fn_inputs)

        # Get function inputs
        ldap_domain_name = getattr(fn_inputs, "ldap_domain_name", "") # text
        ldap_dn = getattr(fn_inputs, "ldap_dn") # text (required)
        ldap_attribute_name = getattr(fn_inputs, "ldap_attribute_name") # text (required)
        ldap_attribute_values_asString = getattr(fn_inputs, "ldap_attribute_values") # text (required) [string repersentation of an array]

        self.LOG.info(f"LDAP Domain Name: {ldap_domain_name}")
        self.LOG.info(f"LDAP DN: {ldap_dn}")
        self.LOG.info(f"LDAP Attribute name: {ldap_attribute_name}")
        self.LOG.info(f"LDAP Attribute Value: {ldap_attribute_values_asString}")

        # Initiate variable, so that it does not error when called
        c = ""

        # Instansiate helper (which gets appconfigs from file)
        ldap = LDAPDomains(self.opts)
        helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))

        try:
            # Try converting input to an array
            ldap_attribute_values = literal_eval(ldap_attribute_values_asString)
        except Exception as err:
            self.LOG.error(f"Error: {err}")
            raise ValueError(
                """ldap_attribute_values must be a string repersenation of an array e.g. "['stringValue1, 1234, 'stringValue2']" """)

        # Instansiate LDAP Server and Connection
        c = helper.get_ldap_connection()

        try:
            # Bind to the connection
            c.bind()
        except Exception as err:
            raise ValueError(f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

        # Inform user
        yield self.status_message(f"Connected to {'Active Directory' if helper.LDAP_IS_ACTIVE_DIRECTORY else 'LDAP Server'}")

        # If the call to LDAP is successful
        success = False
        try:
            yield self.status_message(f"Attempting to update {ldap_attribute_name}")
            # Perform the Modify operation
            success = c.modify(ldap_dn, {ldap_attribute_name: [(MODIFY_REPLACE, ldap_attribute_values)]})

        except Exception as err:
            self.LOG.error(f"Error: {err}")
            raise ValueError("Failed to update. Ensure 'ldap_dn' is valid and the update meets your LDAP CONSTRAINTS")

        finally:
            # Unbind connection
            c.unbind()

        results = {
            "attribute_name": ldap_attribute_name,
            "attribute_values": ldap_attribute_values,
            "user_dn": ldap_dn
        }

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results, success=success)
