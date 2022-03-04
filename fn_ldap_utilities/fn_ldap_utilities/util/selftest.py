# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use, line-too-long

"""
Function implementation test.
Usage:
    resilient-circuits selftest -l fn-ldap-utilities
    resilient-circuits selftest --print-env -l fn-ldap-utilities

Return examples:
    return {
        "state": "success",
        "reason": "Successful connection to third party endpoint"
    }

    return {
        "state": "failure",
        "reason": "Failed to connect to third party endpoint"
    }
"""

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())
from fn_ldap_utilities.util.helper import LDAPUtilitiesHelper


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_ldap_utilities", {})

    helper = LDAPUtilitiesHelper(app_configs)

    status = "success"
    reason = None
    try:
        c = helper.get_ldap_connection()
        # Bind to the connection
        c.bind()
    except Exception as err:
        status = "failure"
        reason = str(err)
    finally:
        # Unbind connection
        c.unbind()

    return {
        "state": status,
        "reason": reason
    }
