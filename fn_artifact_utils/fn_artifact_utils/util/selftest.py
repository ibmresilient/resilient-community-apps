# -*- coding: utf-8 -*-
# Generated with resilient-sdk v48.2.4321

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-artifact-utils
    resilient-circuits selftest --print-env -l fn-artifact-utils

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
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_artifact_utils", {})

    return {"state": "Success"}
