# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ldap_utilities"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ldap_utilities]
ldap_server=xxx.xxx.xxx.xxx
ldap_port=389
ldap_use_ssl=False
ldap_auth=SIMPLE
ldap_user_dn=CN=Username,CN=Users,DC=example,DC=com
ldap_password=password
ldap_is_active_directory=False
ldap_connect_timeout=10
# The domain setting must be set to a valid Windows domain if using NTLM authentication.
#ldap_domain=WORKGROUP 
"""
    return config_data
