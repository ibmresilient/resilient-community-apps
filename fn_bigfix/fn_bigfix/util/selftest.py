# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-bigfix
"""

import logging
from fn_bigfix.lib.bigfix_client import BigFixClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple test to verify Bigfix connectivity.
    """
    options = opts.get("fn_bigfix", {})
    try:
        bigfix_client = BigFixClient(options)
        r = bigfix_client.test_connectivity()
        if r.status_code == 200:
            return {"state": "success", "status_code": r.status_code }
        else:
            return {"state": "failure", "status_code": r.status_code }

    except Exception as e:
        return {"state": "failure", "status_code": str(e)}