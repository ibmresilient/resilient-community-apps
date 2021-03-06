# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ldap_utilities"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_ldap_utilities when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_ldap_utilities]
# Config ldap_domain_name = domain1
domain1-ldap_server = xxx.xxx.xxx.xxx
domain1-ldap_port = 389
domain1-ldap_use_ssl = false
domain1-ldap_auth = simple
domain1-ldap_user_dn = cn=Username1,cn=Users,dc=example,dc=com,dc=ar
domain1-ldap_user_ntlm = domain\\user
domain1-ldap_password = password
domain1-ldap_is_active_directory = false
domain1-ldap_connect_timeout = 10

# Config ldap_domain_name = anotherdomain
anotherdomain-ldap_server = xxx.xxx.xxx.xxx
anotherdomain-ldap_port = 389
anotherdomain-ldap_use_ssl = false
anotherdomain-ldap_auth = simple
anotherdomain-ldap_user_dn = cn=Username,cn=Users,dc=example,dc=com,dc=ar
anotherdomain-ldap_user_ntlm = domain\\user
anotherdomain-ldap_password = password
anotherdomain-ldap_is_active_directory = false
anotherdomain-ldap_connect_timeout = 10
"""

    return config_data
