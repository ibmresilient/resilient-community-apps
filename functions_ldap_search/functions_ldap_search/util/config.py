# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for functions_ldap_search"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[functions_ldap_search]
# LDAP server ip or fully qualified hostname
server=localhost
port=389
#port 636 - LDAP server port set to 636 for encrypted communications
user=cn=admin,dc=example,dc=com
password=admin
auth=SIMPLE
use_ssl=False
    """
    return config_data