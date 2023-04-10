# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

from logging import getLogger
from ldap3 import Server, Connection, ALL, NTLM
from enum import Enum
import fn_ldap_utilities.util.ldap_utils as ldap_utils
from resilient_lib import str_to_bool, validate_fields

PACKAGE_NAME = "fn_ldap_utilities"
LOG = getLogger(__name__)

class LDAPUtilitiesHelper():

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
            raise ValueError(f"Cannot connect to LDAP Server. Ensure credentials are correct\n Error: {err}")

    def __init__(self, app_configs):

        class SUPPORTED_LDAP_AUTH_TYPE_TYPES(Enum):
            ANONYMOUS = "ANONYMOUS"
            SIMPLE = "SIMPLE"
            NTLM = "NTLM"

        validate_fields([
            {"name": "ldap_server", "placeholder": "xxx.xxx.xxx.xxx"},
            {"name": "ldap_port"},
            {"name": "ldap_use_ssl"},
            {"name": "ldap_auth"},
            {"name": "ldap_is_active_directory"},
        ], app_configs)

        self.LDAP_SERVER = app_configs.get("ldap_server")
        self.LDAP_PORT = int(app_configs.get("ldap_port"))
        self.LDAP_USE_SSL = str_to_bool(app_configs.get("ldap_use_ssl"))
        self.LDAP_AUTH_TYPE = app_configs.get("ldap_auth").upper()
        self.LDAP_USER_DN = app_configs.get("ldap_user_dn")
        self.LDAP_USER_NTLM = app_configs.get("ldap_user_ntlm")
        self.LDAP_PASSWORD = app_configs.get("ldap_password")
        self.LDAP_IS_ACTIVE_DIRECTORY = str_to_bool(app_configs.get("ldap_is_active_directory"))
        self.LDAP_CONNECT_TIMEOUT = int(app_configs.get("ldap_connect_timeout", 30))

        if self.LDAP_AUTH_TYPE not in [v.value for v in SUPPORTED_LDAP_AUTH_TYPE_TYPES]:
            raise ValueError(f"Invalid value for 'ldap_auth'. '{self.LDAP_AUTH_TYPE}' is not a supported authentication method. Support methods are: {[v.value for v in SUPPORTED_LDAP_AUTH_TYPE_TYPES]}")

        if self.LDAP_AUTH_TYPE == SUPPORTED_LDAP_AUTH_TYPE_TYPES.SIMPLE.value: # "SIMPLE"
            if not self.LDAP_USER_DN or not self.LDAP_PASSWORD:
                raise ValueError(
                    "'ldap_user_dn' and 'ldap_password' must be defined in the app.config file if using SIMPLE authentication to your LDAP Server")

        elif self.LDAP_AUTH_TYPE == SUPPORTED_LDAP_AUTH_TYPE_TYPES.NTLM.value: # "NTLM"
            if not self.LDAP_USER_NTLM or not self.LDAP_PASSWORD:
                raise ValueError(
                    "'ldap_user_ntlm' and 'ldap_password' must be defined in the app.config file if using NTLM authentication to your LDAP Server")

        elif self.LDAP_AUTH_TYPE == SUPPORTED_LDAP_AUTH_TYPE_TYPES.ANONYMOUS.value: # "ANONYMOUS"
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
