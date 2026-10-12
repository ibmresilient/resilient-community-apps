# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.0.0.430

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-rapid7-insight-idr
    resilient-circuits selftest --print-env -l fn-rapid7-insight-idr

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
import time
import logging
from resilient_lib import IntegrationError, RequestsCommon
from fn_rapid7_insight_idr.lib.app_common import PACKAGE_NAME, AppCommon, IntegrationError


log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        rc = RequestsCommon(opts, app_configs)
        # If we can create an AppCommon object we are able to get an access token.
        app_common = AppCommon(rc, PACKAGE_NAME, app_configs)
        data_list, err_msg = app_common.query_entities_since_ts(int(time.time()))
        reason = err_msg
        state = "success" if not err_msg else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }