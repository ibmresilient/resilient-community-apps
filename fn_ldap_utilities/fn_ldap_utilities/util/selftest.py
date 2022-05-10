# -*- coding: utf-8 -*-

import logging
from .helper import LDAPUtilitiesHelper, get_domains_list
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
            domain = domain_name[domain_name.index(":")+1:] if ":" in domain_name else domain_name

            # Instansiate helper (which gets appconfigs from file)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(domain, domains_list))

            options = opts.get(domain_name, {})

            log.info("Verifying app.config values for {} config section".format(str(options.get("ldap_server"))))

            # Instansiate LDAP Server and Connection
            conn = helper.get_ldap_connection()

            # Bind to the connection
            log.info("Verifying LDAP connection...")
            conn.bind()

            log.info("Test was successful\n")
        except Exception as err:
            state = "failure"
            reason = err
            break

        finally:
            # Unbind connection
            if conn:
                conn.unbind()

    if state == "success":
        return {"state": state}

    return {
        "state": state,
        "reason": reason,
        "domain": domain
    }
