# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""
Function implementation test.
Usage:
    resilient-circuits selftest -l fn-reaqta
    resilient-circuits selftest --print-env -l fn-reaqta

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
from resilient_lib import RequestsCommon
from fn_reaqta.lib.app_common import AppCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        app_configs = opts.get("fn_reaqta", {})
        rc = RequestsCommon(opts, app_configs)
        app_common = AppCommon(rc, app_configs)

        _token = app_common.authenticate()

        return {
            "state": "success",
            "reason": None
        }
    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
