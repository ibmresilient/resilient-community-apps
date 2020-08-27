# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_whois_rdap
"""

import logging
from .helper import get_whois_registry_info
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    proxies = RequestsCommon(None, opts).get_proxies()

    try:
        result = get_whois_registry_info("8.8.8.8", proxies=proxies)
        if result:
            success = True
            reason = None
        else:
            success = False
            reason = None
    except Exception as err:
        success = False
        reason = str(err)

    return {
        "state": success,
        "reason": reason
    }
