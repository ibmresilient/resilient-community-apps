# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_joe_sandbox_analysis
"""

import logging
import jbxapi
from resilient_lib import str_to_bool, validate_fields
from fn_joe_sandbox_analysis.util.helper import connect_to_joe_sandbox, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    ANALYSIS_URL, joesandbox = connect_to_joe_sandbox(opts, opts.get(PACKAGE_NAME, {}))

    if joesandbox.server_online().get("online"):
        return {"state": "success", "reason": "Server Online"}
    else:
        return { "state": "failure", "reason": "Server Offline"}
