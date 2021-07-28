# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long

from resilient import get_client

"""
Function implementation test.
Usage:
    resilient-circuits selftest -l fn_playbook_utils
    resilient-circuits selftest --print-env -l fn_playbook_utils

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

def selftest_function(opts):
    """
    Test connectivity back to SOAR
    """
    try:
        rest_client = get_client(opts)

        return {
            "state": "success",
            "reason": None
        }
    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
