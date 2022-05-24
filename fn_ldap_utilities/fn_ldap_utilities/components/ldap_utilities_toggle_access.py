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
ldap_user_account_control_enabled = 512
ldap_user_account_control_disabled = 514

class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'ldap_utilities_toggle_access"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.domains_list = get_domains_list(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.domains_list = get_domains_list(opts)

    @function("ldap_utilities_toggle_access")
    def _ldap_utilities_toggle_access_function(self, event, *args, **kwargs):
        """Function: A function that allows an LDAP user, with the correct privileges to enable or disable another user given their DN"""

        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_toggle_access' running in workflow '{}'".format(wf_instance_id))

            # Validate that required fields are given
            validate_fields(["ldap_dn", "ldap_toggle_access"], kwargs)

            # Get function inputs
            ldap_domain_name = kwargs.get("ldap_domain_name", "") # text
            input_ldap_dn = kwargs.get("ldap_dn") # text (required)
            input_ldap_toggle_access = kwargs.get("ldap_toggle_access")["name"] # select, values: "Enable", "Disable" (required)

            LOG.info("LDAP Domain Name: %s", ldap_domain_name)
            LOG.info("LDAP DN: %s", input_ldap_dn)
            LOG.info("LDAP Toggle Access: %s", input_ldap_toggle_access)

            yield StatusMessage("Function Inputs OK")

            # Instansiate helper (which gets appconfigs from file)
            ldap = LDAPDomains(self.opts)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(ldap_domain_name, self.domains_list))
            yield StatusMessage("Appconfig Settings OK")

            if not helper.LDAP_IS_ACTIVE_DIRECTORY:
                raise FunctionError(
                    "This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

            # Set local vars
            ldap_user_account_control_attribute = "userAccountControl"

            if (input_ldap_toggle_access.lower() == 'enable'):
                ldap_user_accout_control_value = ldap_user_account_control_enabled

            elif (input_ldap_toggle_access.lower() == 'disable'):
                ldap_user_accout_control_value = ldap_user_account_control_disabled

            else:
                raise ValueError("ldap_toggle_access function input must be 'Enable' or 'Disable'")

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

            try:
                yield StatusMessage("Attempting to {} {}".format(input_ldap_toggle_access, input_ldap_dn))
                # Perform the Modify operation
                res = c.modify(input_ldap_dn, {ldap_user_account_control_attribute: [(MODIFY_REPLACE, [ldap_user_accout_control_value])]})

            except Exception as err:
                LOG.debug("Error: {}".format(err))
                raise ValueError("Could not toggle access for this user. Ensue ldap_dn is valid")

            finally:
                # Unbind connection
                c.unbind()

            # Initialize ResultPayload object
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            results = rp.done(res, None)
            results["user_dn"] = input_ldap_dn
            results["user_status"] = input_ldap_toggle_access

            yield StatusMessage("Finished 'ldap_utilities_toggle_access' running in workflow '{}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
