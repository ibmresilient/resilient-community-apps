# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.

from logging import getLogger
from ldap3 import Server, Connection, ALL, NTLM
import fn_ldap_utilities.util.ldap_utils as ldap_utils 

PACKAGE_NAME = "fn_ldap_utilities"
LOG = getLogger(__name__)

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
        err = "'{}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
            option_name)

        if (not option or (placeholder and option == placeholder)) and not optional:
            raise ValueError(err)
        else:
            return option

    def get_ldap_connection(self):
        NTLM_string = "NTLM"
        try:
            server = Server(self.LDAP_SERVER, port=self.LDAP_PORT, get_info=ALL,
                            use_ssl=self.LDAP_USE_SSL, connect_timeout=self.LDAP_CONNECT_TIMEOUT)

            return Connection(
                server=server,
                user=self.LDAP_USER_NTLM if self.LDAP_AUTH_TYPE == NTLM_string else self.LDAP_USER_DN,
                password=self.LDAP_PASSWORD,
                authentication=NTLM if self.LDAP_AUTH_TYPE == NTLM_string else self.LDAP_AUTH_TYPE,
                return_empty_attributes=True,
                raise_exceptions=True)

        except Exception as err:
            raise ValueError(
                "Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {}".format(err))

    def __init__(self, app_configs):
        SUPPORTED_LDAP_AUTH_TYPE_TYPES = ["ANONYMOUS", "SIMPLE", "NTLM"]

        self.LDAP_SERVER = self.__get_config_option(
            app_configs=app_configs, option_name="ldap_server", placeholder="xxx.xxx.xxx.xxx")
        self.LDAP_PORT = int(self.__get_config_option(
            app_configs=app_configs, option_name="ldap_port"))
        self.LDAP_USE_SSL = self.str_to_bool(self.__get_config_option(
            app_configs=app_configs, option_name="ldap_use_ssl"))
        self.LDAP_AUTH_TYPE = self.__get_config_option(
            app_configs=app_configs, option_name="ldap_auth").upper()
        self.LDAP_USER_DN = self.__get_config_option(
            app_configs=app_configs, option_name="ldap_user_dn", optional=True)
        self.LDAP_USER_NTLM = self.__get_config_option(
            app_configs=app_configs, option_name="ldap_user_ntlm", optional=True)
        self.LDAP_PASSWORD = self.__get_config_option(
            app_configs=app_configs, option_name="ldap_password", optional=True)
        self.LDAP_IS_ACTIVE_DIRECTORY = self.str_to_bool(self.__get_config_option(
            app_configs=app_configs, option_name="ldap_is_active_directory"))
        self.LDAP_CONNECT_TIMEOUT = int(self.__get_config_option(
            app_configs=app_configs, option_name="ldap_connect_timeout"))

        if self.LDAP_AUTH_TYPE not in SUPPORTED_LDAP_AUTH_TYPE_TYPES:
            raise ValueError("Invalid value for 'ldap_auth'. '{}' is not a supported authentication method. Support methods are: {}".format(
                self.LDAP_AUTH_TYPE, SUPPORTED_LDAP_AUTH_TYPE_TYPES))

        if self.LDAP_AUTH_TYPE == SUPPORTED_LDAP_AUTH_TYPE_TYPES[1]: # "SIMPLE"
            if not self.LDAP_USER_DN or not self.LDAP_PASSWORD:
                raise ValueError(
                    "'ldap_user_dn' and 'ldap_password' must be defined in the app.config file if using SIMPLE authentication to your LDAP Server")

        elif self.LDAP_AUTH_TYPE == SUPPORTED_LDAP_AUTH_TYPE_TYPES[2]: # "NTLM"
            if not self.LDAP_USER_NTLM or not self.LDAP_PASSWORD:
                raise ValueError(
                    "'ldap_user_ntlm' and 'ldap_password' must be defined in the app.config file if using NTLM  authentication to your LDAP Server")

        elif self.LDAP_AUTH_TYPE == SUPPORTED_LDAP_AUTH_TYPE_TYPES[0]: # "ANONYMOUS"
            if self.LDAP_USER_DN or self.LDAP_USER_NTLM or self.LDAP_PASSWORD:
                raise ValueError(
                    "'ldap_user_dn', 'ldap_user_ntlm' and 'ldap_password' must be left blank in the app.config file if using ANONYMOUS authentication to your LDAP Server")

def get_domains_list(opts):
    """
    Used for initilizing or reloading the options variable
    :param opts: list of options
    :return: list of ldap domains
    """
    domains_list = {}

    if opts.get(PACKAGE_NAME, {}): # If no domains given [fn_ldap_utilities]
        domain_list = {PACKAGE_NAME}
    else: # If domains given [fn_ldap_utilities:domain]
        domains = ldap_utils.LDAPDomains(opts)
        domain_list = domains.get_domain_name_list()

    # Creates a dictionary that is filled with the LDAP domains
    # and there configurations
    for domain_name in domain_list:
        domains_list[domain_name] = opts.get(domain_name, {})

    return domains_list
