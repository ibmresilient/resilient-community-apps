# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ldap_utilities"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""[fn_ldap_utilities]
# Ip address of the LDAP Server
ldap_server=xxx.xxx.xxx.xxx
# Use port 636 if using ssl or port 389 if not using ssl
ldap_port=389
ldap_use_ssl=False
# Can be ANONYMOUS, SIMPLE or NTLM
ldap_auth=SIMPLE
# DN of LDAP account
ldap_user_dn=CN=Username,CN=Users,DC=example,DC=com
# Password for the LDAP account
ldap_password=password
# Windows NTLM user
ldap_user_ntlm=Domain\\User
ldap_is_active_directory=False
ldap_connect_timeout=10
"""
