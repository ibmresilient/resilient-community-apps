# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper
from ldap3 import MODIFY_REPLACE
from ast import literal_eval

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'ldap_utilities_update"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ldap_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ldap_utilities", {})

    @function("ldap_utilities_update")
    def _ldap_utilities_update_function(self, event, *args, **kwargs):
        """Function: A function that updates the attribute of a DN with a new value"""
        log = logging.getLogger(__name__)
        
        try:
            yield StatusMessage("Starting ldap_utilities_update")

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(self.options)
            yield StatusMessage("Appconfig Settings OK")

            # Get function inputs
            input_ldap_dn = helper.get_function_input(kwargs, "ldap_dn") # text (required)
            input_ldap_attribute_name = helper.get_function_input(kwargs, "ldap_attribute_name") # text (required)
            input_ldap_attribute_values_asString = helper.get_function_input(kwargs, "ldap_attribute_values") # text (required) [string repersentation of an array]
            yield StatusMessage("Function Inputs OK")

            try:
              # Try converting input to an array
              input_ldap_attribute_values = literal_eval(input_ldap_attribute_values_asString)
            except Exception:
              raise ValueError("""input_ldap_attribute_values must be a string repersenation of an array e.g. "['stringValue1, 1234, 'stringValue2']" """)

            # Instansiate LDAP Server and Connection
            c = helper.get_ldap_connection()

            try:
              # Bind to the connection
              c.bind()
            except:
              raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct")

            # Inform user
            msg = ""
            if helper.LDAP_IS_ACTIVE_DIRECTORY:
              msg = "Connected to {0}".format("Active Directory")
            else:
              msg = "Connected to {0}".format("LDAP Server")
            yield StatusMessage(msg)

            res = False
            
            try:
              yield StatusMessage("Attempting to update {0}".format(input_ldap_attribute_name))
              # perform the Modify operation
              res = c.modify(input_ldap_dn, {input_ldap_attribute_name: [(MODIFY_REPLACE, input_ldap_attribute_values)]})

            except Exception:
              raise ValueError("Failed to update. Ensure 'ldap_dn' is valid and the update meets your LDAP CONSTRAINTS")
          
            finally:
              # Unbind connection
              c.unbind()

            results = {
                "success": res,
                "attribute_name": input_ldap_attribute_name,
                "attribute_values": input_ldap_attribute_values,
                "user_dn": input_ldap_dn
            }

            log.info("Completed")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
