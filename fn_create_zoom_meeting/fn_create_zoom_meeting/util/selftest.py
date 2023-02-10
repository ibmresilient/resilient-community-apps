# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-create-zoom-meeting
    resilient-circuits selftest --print-env -l fn-create-zoom-meeting

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
from fn_create_zoom_meeting.util.zoom_common import ZoomCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_create_zoom_meeting", {})

    zoom = ZoomCommon(opts, app_configs)
    request = zoom.zoom_request("/users?status=active&page_size=30&page_number=", "GET")
    if request.status_code == 200:
        return {"state": "success"}
    else:
        return {"state": "failure", "reason": "Get request failed"}
