# -*- coding: utf-8 -*-

import logging
from .helper import LDAPUtilitiesHelper, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Selftest function will try to connect to the LDAP instance.
    Fail if any exceptions are raised.
    """

    options = opts.get(PACKAGE_NAME, {})
    state = "success"
    reason = "N/A"
    try:
        # Instansiate helper (which gets appconfigs from file)
        helper = LDAPUtilitiesHelper(options)

        # Instansiate LDAP Server and Connection
        conn = helper.get_ldap_connection()

        # Bind to the connection
        conn.bind()
    except Exception as err:
        state = "failure"
        reason = err
    
    finally:
        # Unbind connection
        conn.unbind()

    return {
        "state": state,
        "reason": reason
    }