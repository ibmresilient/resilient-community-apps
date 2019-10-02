# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_sep
"""
import logging
import datetime
from fn_proofpoint_trap.lib.pptr_client import PPTRClient

lastupdate = 60
log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Simple test to verify ProofPoint Trap connectivity.
    """
    options = opts.get("fn_proofpoint_trap", {})
    try:
        pptr = PPTRClient(opts, options)
        r = pptr.get_incidents(lastupdate)

        if isinstance(r, list):
            return {"state": "success"}
        else:
            return {"state": "failure"}

    except Exception as e:
        return {"state": "failure", "status_code": e}