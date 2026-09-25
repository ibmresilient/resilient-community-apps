# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-darktrace
    resilient-circuits selftest --print-env -l fn-darktrace

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
from requests import HTTPError

from resilient_lib import RequestsCommon
from fn_darktrace.lib.app_common import AppCommon, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Tests connectivity to Darktrace API by hitting the /status
    endpoint. If can't successfully hit the endpoint, returns ``failure``
    """

    try:
        app_configs = opts.get(PACKAGE_NAME, {})

        rc = RequestsCommon(opts, app_configs)
        app_common = AppCommon(rc, app_configs, opts.get("integrations", {}))

        status = app_common.get_system_status()

        if "status" not in status:
            return {
                "state": "success",
                "reason": "Successfully connected to Darktrace endpoint"
            }
        else:
            # system status will return {"status": "<reason>"} if the system status can't be reached
            # it will not return a "status" value if it was successful
            reason = status.get("status")

    except HTTPError as http_err:
        reason = str(http_err)

    return {
        "state": "failure",
        "reason": reason
    }
