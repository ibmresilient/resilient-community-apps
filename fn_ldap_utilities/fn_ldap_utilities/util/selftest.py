# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

import logging
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper, get_domains_list
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
    conn = ""

    for domain_name in domains_list:
        try:
            """
            If labels are given to the servers in the app.config `domain_name` will start with 'fn_ldap_utilities:' else if
            labels are not given then `domain_name` will equal 'fn_ldap_utilities'.
            If `domain_name` contains ':' then a labels have been given to the servers and `domain` will be set to the label given to the server else
            if `domain_name` does not contain ':' then servers have not been labeled and `domain` will be set to `domain_name` which will equal 'fn_ldap_utilities'.
            """
            domain = domain_name[domain_name.index(":")+1:] if ":" in domain_name else domain_name

            # Instantiate helper (which gets app configs from file)
            helper = LDAPUtilitiesHelper(ldap.ldap_domain_name_test(domain, domains_list))

            options = opts.get(domain_name, {})

            log.info(f"Verifying app.config values for {str(options.get('ldap_server'))} config section")

            # Instantiate LDAP Server and Connection
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
