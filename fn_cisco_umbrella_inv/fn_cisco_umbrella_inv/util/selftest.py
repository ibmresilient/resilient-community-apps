# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_cisco_umbrella_inv
"""

import logging
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import get_proxies

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to confirm access to Cisco Umbrella Investigate for API connectivity.
    """
    options = opts.get("fn_cisco_umbrella_inv", {})
    api_token = options.get("api_token")
    base_url = options.get("base_url")
    proxies = get_proxies(opts, options)
    try:

        rinv = ResilientInv(api_token, base_url, proxies=proxies)

        r = rinv.test_connectivity()

        if r.status_code == 200:
            return {"state": "success", "status_code": r.status_code }
        else:
            return {"state": "failure", "status_code": r.status_code }

    except Exception as e:
        return {"state": "failure", "status_code": e}