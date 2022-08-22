# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_mcafee_epo
"""

import logging
from fn_mcafee_epo.lib.epo_helper import init_client

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_mcafee_epo", {})

    reason = None
    try:
        client = init_client(opts, options)
        response = client.request("epo.getVersion", None)

        status = True if response else False
        reason = None
    except Exception as err:
        status = False
        reason = str(err)

    return {
        "state": "success" if status else "failure",
        "reason": reason
    }