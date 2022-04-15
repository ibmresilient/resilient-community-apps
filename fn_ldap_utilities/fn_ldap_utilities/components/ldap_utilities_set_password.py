# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

from logging import getLogger
from resilient_lib import validate_fields, ResultPayload
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper, get_domains_list, PACKAGE_NAME
from fn_ldap_utilities.util.ldap_utils import LDAPDomains
from ldap3 import MODIFY_REPLACE

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_set_password"""

    def __init__(self, opts):
        """Constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.domains_list = get_domains_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.domains_list = get_domains_list(opts)

    @function("ldap_utilities_set_password")
    def _ldap_utilities_set_password_function(self, event, *args, **kwargs):
        """Function: A function that allows you to set a new password for an LDAP entry given the entry's DN"""

        try:
            yield StatusMessage("Starting ldap_utilities_set_password")

            # Validate that required fields are given
            validate_fields(["ldap_dn", "ldap_new_password"], kwargs)

            # Get function inputs
            ldap_domain_name = kwargs.get("ldap_domain_name") # text
            input_ldap_dn = kwargs.get("ldap_dn") # text (required)
            input_ldap_new_password = kwargs.get("ldap_new_password") # text (required)

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP DN: %s", input_ldap_dn)

            yield StatusMessage("Function Inputs OK")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(LDAPDomains.ldap_domain_name_test(ldap_domain_name, self.domains_list))
            yield StatusMessage("Appconfig Settings OK")

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
                # Bind to the connection
                c.bind()
            except Exception as err:
                raise ValueError(
                    "Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {}".format(err))

            # Inform user
            yield StatusMessage("Connected to {}".format("Active Directory" if helper.LDAP_IS_ACTIVE_DIRECTORY else "LDAP Server"))

            res = False

            try:
                yield StatusMessage("Attempting to change password")
                if helper.LDAP_IS_ACTIVE_DIRECTORY:
                    res = c.extend.microsoft.modify_password(str(input_ldap_dn), input_ldap_new_password)
                else:
                    res = c.modify(input_ldap_dn, {'userPassword': [(MODIFY_REPLACE, [input_ldap_new_password])]})

            except Exception:
                raise ValueError(
                    "Could not change password. Check input_ldap_dn and input_ldap_new_password are valid")

            finally:
                # Unbind connection
                c.unbind()

            # Initialize ResultPayload object
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            results = rp.done(res, None)
            results["user_dn"] = input_ldap_dn

            LOG.info("Completed")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
