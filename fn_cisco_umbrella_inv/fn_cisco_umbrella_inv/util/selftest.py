# -*- coding: utf-8 -*-
"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_cisco_umbrella_inv
"""

import logging
from fn_cisco_umbrella_inv.util.helpers import investigateClient, URIs
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Simple test to confirm access to Cisco Umbrella Investigate for API connectivity.
    """
    options = opts.get("fn_cisco_umbrella_inv", {})
    try:
        invClient = investigateClient(options, RequestsCommon(opts, options))
        r = invClient.make_api_call("GET", f"{URIs.get('categorization')}/ibm.com")
        return {"state": "success"}

    except Exception as e:
        return {"state": "failure", "reason": str(e)}
