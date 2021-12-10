# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage:
    resilient-circuits selftest -l fn-siemplify
    resilient-circuits selftest --print-env -l fn-siemplify

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
from fn_siemplify.lib.siemplify_common import SiemplifyCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_siemplify", {})

    rc = RequestsCommon(opts, app_configs)

    try:
        sc = SiemplifyCommon(rc, app_configs)
        result = sc.get_blocklist()

        return {
            "state": "success",
            "reason": None
        }
    except Exception as err:
        return {
            "state": "failure",
            "reason": str(err)
        }
