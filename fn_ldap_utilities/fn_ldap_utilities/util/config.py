# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
"""Generate a default configuration-file section for fn_ldap_utilities"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""
# V2.0.0+ have the option to have multiple servers configured.
# By default two examples of servers are given, example one is labeled `Domain1` and example two is labled `Domain2`.
# The label for a server is placed after `[fn_ldap_utilities:` and then followed by `]`.
# To add additional servers copy the below example server configuration from `[fn_ldap_utilities:Domain1]` to `ldap_connect_timeout=10`.
# Then paste it at the bottom on the app.config.
# Change the server label, `Domain1`, to a label helpful to define that server.
# Then change the setting to those of the server you wish to add.

[fn_ldap_utilities:Domain1]
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

[fn_ldap_utilities:Domain2]
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
