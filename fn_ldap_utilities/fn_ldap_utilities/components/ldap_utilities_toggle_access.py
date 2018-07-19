# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ldap3 import MODIFY_REPLACE

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_toggle_access"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ldap_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ldap_utilities", {})

    @function("ldap_utilities_toggle_access")
    def _ldap_utilities_toggle_access_function(self, event, *args, **kwargs):
        """Function: A function that allows an LDAP user, with the correct privileges to enable or disable another user given their DN"""
        log = logging.getLogger(__name__)
        
        try:
            yield StatusMessage("Starting ldap_utilities_toggle_access")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options)
            yield StatusMessage("Appconfig Settings OK")

            # Get function inputs
            input_ldap_dn = helper.get_function_input(kwargs, "ldap_dn") # text (required)
            input_ldap_toggle_access = helper.get_function_input(kwargs, "ldap_toggle_access")["name"] # select, values: "Enable", "Disable" (required)
            yield StatusMessage("Function Inputs OK")

            if not helper.LDAP_IS_ACTIVE_DIRECTORY:
              raise FunctionError("This function only supports an Active Directory connection. Make sure ldap_is_active_directory is set to True in the app.config file")

            # Set local vars
            ldap_user_account_control_attribute = "userAccountControl"

            if (input_ldap_toggle_access.lower() == 'enable'):
              ldap_user_accout_control_value = 512
              user_status = "Enabled"

            elif (input_ldap_toggle_access.lower() == 'disable'):
              ldap_user_accout_control_value = 514
              user_status = "Disabled"

            else:
              raise ValueError("ldap_toggle_access function input must be 'Enable' or 'Disable'")

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()
            
            # Bind to the connection
            c.bind()
            
            # Inform user
            msg = ""
            if helper.LDAP_IS_ACTIVE_DIRECTORY:
              msg = "Connected to {0}".format("Active Directory")
            else:
              msg = "Connected to {0}".format("LDAP Server")
            yield StatusMessage(msg)

            res = False

            try:
              yield StatusMessage("Attempting to {0} {1}".format(input_ldap_toggle_access, input_ldap_dn))
              # perform the Modify operation
              res = c.modify(input_ldap_dn, {ldap_user_account_control_attribute: [(MODIFY_REPLACE, [ldap_user_accout_control_value])]})

            except Exception:
              raise FunctionError()

            results = {
                "success": res,
                "user_dn": input_ldap_dn,
                "user_status": user_status
            }

            log.info("Completed")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
        
        finally:
          # Unbind connection
          c.unbind()