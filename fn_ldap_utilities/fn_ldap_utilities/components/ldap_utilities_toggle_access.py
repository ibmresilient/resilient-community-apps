# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ldap3 import MODIFY_REPLACE

PACKAGE_NAME = "fn_ldap_utilities"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_toggle_access''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("ldap_utilities_toggle_access")
    def _ldap_utilities_toggle_access_function(self, event, *args, **kwargs):
        """Function: A function that allows an LDAP user, with the correct privileges to enable or disable another account given their DN"""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'ldap_utilities_toggle_access' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            ldap_domain_name = kwargs.get("ldap_domain_name")  # text
            ldap_toggle_access = self.get_select_param(kwargs.get("ldap_toggle_access"))  # select, values: "Enable", "Disable"
            ldap_dn = kwargs.get("ldap_dn")  # text

            log = logging.getLogger(__name__)
            log.info("ldap_domain_name: %s", ldap_domain_name)
            log.info("ldap_toggle_access: %s", ldap_toggle_access)
            log.info("ldap_dn: %s", ldap_dn)
            yield StatusMessage("Function Inputs OK")


            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options, ldap_domain_name)
            log.info("[app.config] -ldap_server: %s", helper.LDAP_SERVER)
            log.info("[app.config] -ldap_user_dn: %s", helper.LDAP_USER_DN)
            yield StatusMessage("Appconfig Settings OK")


            ##############################################

            if not helper.LDAP_IS_ACTIVE_DIRECTORY:
              raise FunctionError("This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

            # Set local vars
            ldap_user_account_control_attribute = "userAccountControl"

            if (ldap_toggle_access.lower() == 'enable'):
              ldap_user_accout_control_value = 512
              user_status = "Enabled"

            elif (ldap_toggle_access.lower() == 'disable'):
              ldap_user_accout_control_value = 514
              user_status = "Disabled"

            else:
              raise ValueError("ldap_toggle_access function input must be 'Enable' or 'Disable'")

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()
            
            try:
              # Bind to the connection
              c.bind()
            except Exception as err:
              raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {0}".format(err))

            # Inform user
            msg = ""
            if helper.LDAP_IS_ACTIVE_DIRECTORY:
              msg = "Connected to {0}".format("Active Directory")
            else:
              msg = "Connected to {0}".format("LDAP Server")
            yield StatusMessage(msg)

            res = False
            try:
              yield StatusMessage("Attempting to {0} {1}".format(ldap_toggle_access, ldap_dn))
              # perform the Modify operation
              res = c.modify(ldap_dn, {ldap_user_account_control_attribute: [(MODIFY_REPLACE, [ldap_user_accout_control_value])]})
              # Test: res = 'c.modify(' + str(ldap_dn) + ' , {' + str(ldap_user_account_control_attribute) + ': [(MODIFY_REPLACE, [' + str(ldap_user_accout_control_value) + '])]})'

            except Exception:
              raise ValueError("Could not toggle access for this user. Ensue ldap_dn is valid")

            finally:
              # Unbind connection
              c.unbind()

            ##############################################


            results = {
                "success": res,
                "domain_name": ldap_domain_name,
                "user_dn": ldap_dn,
                "user_status": user_status
            } 

            yield StatusMessage("Finished 'ldap_utilities_toggle_access' that was running in workflow '{0}'".format(wf_instance_id))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
