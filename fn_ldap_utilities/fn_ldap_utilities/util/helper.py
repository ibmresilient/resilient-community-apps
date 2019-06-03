# (c) Copyright IBM Corp. 2018. All Rights Reserved.
import logging
from ldap3 import Server, Connection, ALL, NTLM, MODIFY_REPLACE

class LDAPUtilitiesHelper:

    def str_to_bool(self, str):
        """Convert unicode string to equivalent boolean value. Converts a "true" or "false" string to a boolean value , string is case insensitive."""
        if str.lower() == 'true':
            return True
        elif str.lower() == 'false':
            return False
        else:
            raise ValueError("{} is not a boolean".format(str))

    @staticmethod
    def __get_config_option(app_configs, option_name, optional=False, placeholder=None):
        """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
        option = app_configs.get(option_name)
        err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(option_name)

        if not option and optional is False:
            raise ValueError(err)
        elif optional is False and placeholder is not None and option == placeholder:
            raise ValueError(err)
        else:
            return option

    @staticmethod
    def get_function_input(inputs, input_name, optional=False):
        """Given input_name, checks if it defined. Raises ValueError if a mandatory input is None"""

        log = logging.getLogger(__name__)
        log.debug("Trying to get function input: %s from %s. optional = %s", input_name, inputs, optional)

        the_input = inputs.get(input_name)

        if the_input is None and optional is False:
            err = "'{0}' is a mandatory function input".format(input_name)
            raise ValueError(err)
        else:
            log.debug("Got function input: %s", input_name)
            return the_input

    def get_ldap_connection(self):
        try:
            server = Server(self.LDAP_SERVER, port=self.LDAP_PORT, get_info=ALL, use_ssl=self.LDAP_USE_SSL, connect_timeout=self.LDAP_CONNECT_TIMEOUT)
        
            if self.LDAP_AUTH_TYPE == "NTLM":
                connection = Connection(
                    server=server,
                    user=self.LDAP_USER_NTLM,
                    password=self.LDAP_PASSWORD,
                    authentication=NTLM,
                    return_empty_attributes=True,
                    raise_exceptions=True)

            else:
                connection = Connection(
                    server=server,
                    user=self.LDAP_USER_DN,
                    password=self.LDAP_PASSWORD,
                    authentication=self.LDAP_AUTH_TYPE,
                    return_empty_attributes=True,
                    raise_exceptions=True)

            return connection

        except Exception as err:
            raise ValueError("Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {0}".format(err))
  
    def __init__(self, app_configs):
        SUPPORTED_LDAP_AUTH_TYPE_TYPES = ["ANONYMOUS", "SIMPLE", "NTLM"]

        self.LDAP_SERVER = self.__get_config_option(app_configs=app_configs, option_name="ldap_server", optional=False, placeholder="xxx.xxx.xxx.xxx")
        self.LDAP_PORT = int(self.__get_config_option(app_configs=app_configs, option_name="ldap_port", optional=False))
        self.LDAP_USE_SSL = self.str_to_bool(self.__get_config_option(app_configs=app_configs, option_name="ldap_use_ssl", optional=False))
        self.LDAP_AUTH_TYPE = self.__get_config_option(app_configs=app_configs, option_name="ldap_auth", optional=False).upper()
        self.LDAP_USER_DN = self.__get_config_option(app_configs=app_configs, option_name="ldap_user_dn", optional=True)
        self.LDAP_USER_NTLM = self.__get_config_option(app_configs=app_configs, option_name="ldap_user_ntlm", optional=True)
        self.LDAP_PASSWORD = self.__get_config_option(app_configs=app_configs, option_name="ldap_password", optional=True)
        self.LDAP_IS_ACTIVE_DIRECTORY = self.str_to_bool(self.__get_config_option(app_configs=app_configs, option_name="ldap_is_active_directory", optional=False))
        self.LDAP_CONNECT_TIMEOUT = int(self.__get_config_option(app_configs=app_configs, option_name="ldap_connect_timeout", optional=False))

        if self.LDAP_AUTH_TYPE not in SUPPORTED_LDAP_AUTH_TYPE_TYPES:
            raise ValueError("Invalid value for 'ldap_auth'. '{0}' is not a supported authentication method. Support methods are: {1}".format(self.LDAP_AUTH_TYPE, SUPPORTED_LDAP_AUTH_TYPE_TYPES))

        if self.LDAP_AUTH_TYPE == "SIMPLE":
            if not self.LDAP_USER_DN or not self.LDAP_PASSWORD:
                raise ValueError("'ldap_user_dn' and 'ldap_password' must be defined in the app.config file if using SIMPLE authentication to your LDAP Server")

        elif self.LDAP_AUTH_TYPE == "NTLM":
            if not self.LDAP_USER_NTLM or not self.LDAP_PASSWORD:
                raise ValueError("'ldap_user_ntlm' and 'ldap_password' must be defined in the app.config file if using NTLM  authentication to your LDAP Server")

        elif self.LDAP_AUTH_TYPE == "ANONYMOUS":
            if self.LDAP_USER_DN or self.LDAP_USER_NTLM or self.LDAP_PASSWORD:
                raise ValueError("'ldap_user_dn', 'ldap_user_ntlm' and 'ldap_password' must be left blank in the app.config file if using ANONYMOUS authentication to your LDAP Server")
