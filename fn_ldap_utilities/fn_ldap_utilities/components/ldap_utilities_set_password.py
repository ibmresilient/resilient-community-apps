# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
import json

from ldap3 import Server, Connection, ALL, MODIFY_REPLACE

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_set_password"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ldap_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ldap_utilities", {})

    @function("ldap_utilities_set_password")
    def _ldap_utilities_set_password_function(self, event, *args, **kwargs):
        """Function: A function that allows you to set a new password for an LDAP entry given the entry's DN"""
        log = logging.getLogger(__name__)

        try:
            yield StatusMessage("Starting ldap_utilities_set_password")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options)
            yield StatusMessage("Appconfig Settings OK")
            
            # Get function inputs
            input_ldap_dn = helper.get_function_input(kwargs, "ldap_dn") # text (required)
            input_ldap_new_password = helper.get_function_input(kwargs, "ldap_new_password") # text (required)
            yield StatusMessage("Function Inputs OK")

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
              yield StatusMessage("Attempting to change password")
              if helper.LDAP_IS_ACTIVE_DIRECTORY:
                res = c.extend.microsoft.modify_password(str(input_ldap_dn), input_ldap_new_password)
              else:
                res = c.modify(input_ldap_dn, {'userPassword': [(MODIFY_REPLACE, [input_ldap_new_password])]})

            except Exception:
              raise ValueError("Could not change password. Check input_ldap_dn and input_ldap_new_password are valid")

            finally:
              # Unbind connection
              c.unbind()

            results = {
                "success": res,
                "user_dn": input_ldap_dn
            }

            log.info("Completed")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
