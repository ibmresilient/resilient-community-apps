# -*- coding: utf-8 -*-

import logging
from .helper import LDAPUtilitiesHelper, PACKAGE_NAME, get_domains_list
from fn_ldap_utilities.util.ldap_utils import LDAPDomains

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Selftest function will try to connect to the LDAP instance.
    Fail if any exceptions are raised.
    """

    domains_list = get_domains_list(opts)
    ldap = LDAPDomains(opts)

    state = "success"
    reason = "N/A"
    domain = "N/A"
    for domain_name in domains_list:
        try:
            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(domain_name, domains_list))

            # Instansiate LDAP Server and Connection
            conn = helper.get_ldap_connection()

            # Bind to the connection
            conn.bind()
        except Exception as err:
            domain = domain_name
            state = "failure"
            reason = err
            break

        finally:
            # Unbind connection
            conn.unbind()

    if state == "success":
        return {"state": state}

    return {
        "state": state,
        "reason": reason,
        "domain": domain
    }
