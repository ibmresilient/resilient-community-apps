# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

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

        def str_to_bool(str):
          """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
          if str.lower() == 'true':
              return True
          elif str.lower() == 'false':
              return False
          else:
              raise ValueError

        def get_config_option(option_name, optional=False):
          """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
          option = self.options.get(option_name)

          if option is None and optional is False:
            err = "'{0}' is mandatory and is not set in ~/.resilient/appconfig file. You must set this value to run this function".format(option_name)
            log.error(err)
            raise ValueError(err)
          else:
            return option
        
        def get_function_input(input_name, optional=False):
          """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""
          input = kwargs.get(input_name)

          if input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            log.error(err)
            raise ValueError(err)
          else:
            return input

        try:
            yield StatusMessage("Starting")

            # Get settings from appconfig file
            LDAP_SERVER = get_config_option("ldap_server")
            LDAP_PORT = int(get_config_option("ldap_port"))
            LDAP_USE_SSL = str_to_bool(get_config_option("ldap_use_ssl"))
            LDAP_AUTH = get_config_option("ldap_auth")
            LDAP_USER_DN = get_config_option("ldap_user_dn")
            LDAP_PASSWORD = get_config_option("ldap_password")
            LDAP_IS_ACTIVE_DIRECTORY = str_to_bool(get_config_option("ldap_is_active_directory"))
            LDAP_CONNECT_TIMEOUT = int(get_config_option("ldap_connect_timeout"))
            LDAP_DOMAIN = get_config_option("ldap_domain", True)
            yield StatusMessage("Appconfig Settings OK")
            
            # Get function inputs
            input_ldap_dn = get_function_input("ldap_dn") # text (required)
            input_ldap_new_password = get_function_input("ldap_new_password") # text (required)
            yield StatusMessage("Function Inputs OK")

            # Instansiate LDAP Server Object
            server = Server(LDAP_SERVER, port=LDAP_PORT, get_info=ALL, use_ssl=LDAP_USE_SSL, connect_timeout=LDAP_CONNECT_TIMEOUT)
            
            # Connect to the LDAP Server
            c = Connection(server, user=LDAP_USER_DN, password=LDAP_PASSWORD, authentication=LDAP_AUTH, return_empty_attributes=True, raise_exceptions=True)

            # Bind to the connection
            c.bind()
            
            # Inform user
            msg = ""
            if LDAP_IS_ACTIVE_DIRECTORY:
              msg = "Connected to {0}".format("Active Directory")
            else:
              msg = "Connected to {0}".format("LDAP Server")
            yield StatusMessage(msg)

            res = False
            
            try:
              yield StatusMessage("Attempting to change password")
              if LDAP_IS_ACTIVE_DIRECTORY:
                res = c.extend.microsoft.modify_password(str(input_ldap_dn), input_ldap_new_password)
              else:
                res = c.modify(input_ldap_dn, {'userPassword': [(MODIFY_REPLACE, [input_ldap_new_password])]})

            except Exception:
              raise FunctionError()

            results = {
                "success": res,
                "user_dn": input_ldap_dn
            }

            log.info("Completed")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
        
        finally:
          # Unbind connection
          c.unbind()