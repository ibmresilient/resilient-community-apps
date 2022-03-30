# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-shadowserver
    resilient-circuits selftest --print-env -l fn-shadowserver

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

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_shadowserver", {})
    try:
        # url = "https://api.shadowserver.org/malware/info?sample={}".format("")
        url = "https://api.shadowserver.org/malware/info?sample=15ec7258422772a04bf9641836eb44f7"
        rc = RequestsCommon(opts, app_configs)
        rc.execute('get', url)
        return {"state": "success"}
    except Exception as e:
        return {
            "state": "failure",
            "reason": e
        }