# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ldap_search"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ldap_search]
# LDAP server ip or fully qualified hostname
server=ldap.forumsys.com
port=389
# The domain setting must be set to a valid Windows domain if using NTLM authentication.
#domain=WORKGROUP 
user=cn=read-only-admin,dc=example,dc=com
password=password
auth=SIMPLE
use_ssl=False
connect_timeout=10
    """
    return config_data
