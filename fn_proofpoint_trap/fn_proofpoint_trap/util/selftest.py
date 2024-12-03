# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_sep
"""
import logging
from fn_proofpoint_trap.lib.pptr_client import PPTRClient

LASTUPDATE = 60
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Simple test to verify ProofPoint Trap connectivity.
    """
    options = opts.get("fn_proofpoint_trap", {})
    try:
        pptr = PPTRClient(opts, options)
        res = pptr.get_incidents(LASTUPDATE)

        if isinstance(res, list):
            return {"state": "success"}
        return {"state": "failure"}

    except Exception as excp:
        return {"state": "failure", "status_code": excp}
