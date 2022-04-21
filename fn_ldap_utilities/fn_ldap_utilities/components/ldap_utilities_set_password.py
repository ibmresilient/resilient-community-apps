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
from string import ascii_letters, digits
from random import sample

LOG = getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_set_password'"""

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
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_set_password' running in workflow '{}'".format(wf_instance_id))

            # Validate that required fields are given
            validate_fields(["ldap_dn"], kwargs)

            # Get function inputs
            ldap_domain_name = kwargs.get("ldap_domain_name", "") # text
            ldap_dn = kwargs.get("ldap_dn") # text (required)
            ldap_new_password = kwargs.get("ldap_new_password") # text
            ldap_new_auto_password_len = kwargs.get("ldap_new_auto_password_len", 12)  # int Default length is 12
            ldap_return_new_password = kwargs.get("ldap_return_new_password")  # boolean

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP DN: %s", ldap_dn)
            LOG.debug("ldap_new_auto_password_len: %s", ldap_new_auto_password_len)
            LOG.info("ldap_return_new_password: %s", ldap_return_new_password)
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

            # If ldap_new_password empty, auto-generate pwd with length ldap_new_auto_password_len. If ldap_new_auto_password_len empty, creates 12 char length pwd.
            if not ldap_new_password:
                ldap_new_password = "".join(sample(str(ascii_letters+digits+'*#$%&/-_!?'), int(ldap_new_auto_password_len)))

            try:
                yield StatusMessage("Attempting to change password")
                if helper.LDAP_IS_ACTIVE_DIRECTORY:
                    res = c.extend.microsoft.modify_password(str(ldap_dn), ldap_new_password)
                else:
                    res = c.modify(ldap_dn, {'userPassword': [(MODIFY_REPLACE, [ldap_new_password])]})

            except Exception as err:
                LOG.debug("Error: {}".format(err))
                raise ValueError("Could not change password. Check ldap_dn are valid")

            finally:
                # Unbind connection
                c.unbind()

            # If ldap_return_new_password is False then do not return password
            if not ldap_return_new_password:
                ldap_new_password = '********'

            # Initialize ResultPayload object
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            results = rp.done(res, None)
            results["user_dn"] = ldap_dn
            results["inputs"]["ldap_new_password"] = ldap_new_password

            yield StatusMessage("Finished 'ldap_utilities_set_password' that was running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
