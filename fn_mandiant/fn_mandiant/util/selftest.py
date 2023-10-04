# -*- coding: utf-8 -*-
# <<PUT YOUR COPYRIGHT TEXT HERE>>
# Generated with resilient-sdk v50.0.108

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-mandiant
    resilient-circuits selftest --print-env -l fn-mandiant

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

from fn_mandiant.lib.mandiant_client import MandiantClient
from resilient_lib.components.requests_common import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    
    app_rc       = RequestsCommon(opts)
    app_configs  = opts.get("fn_mandiant", {})
    mandiant_cli = MandiantClient(app_rc, app_configs)
    
    mandiant_cli.authenticate()
    
    if mandiant_cli.check_authenticated():

        return {
            "state": "success",
            "reason": "Passed!"}

    return {
        "state": "failure",
        "reason": "Failed to connect to Mandiant!"}

