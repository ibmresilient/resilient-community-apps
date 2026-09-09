# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_whois
"""

import logging
from fn_whois.lib.whois_common import whois_query, get_config_option

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_whois", {})

    try:
        whois_query("8.8.8.8", get_config_option(app_configs, "whois_https_proxy", True))
        success = True
        reason = None
    except Exception as err:
        success = False
        reason = str(err)

    return {
        "state": success,
        "reason": reason
    }