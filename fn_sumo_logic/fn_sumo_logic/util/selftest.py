# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.2.2.1096

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-sumo-logic
    resilient-circuits selftest --print-env -l fn-sumo-logic

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
from fn_sumo_logic.lib.app_common import PACKAGE_NAME, AppCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """ Selftest function used to test connectivity to the Sumo Logic endpoint

    Args:
        opts (dict): app.config options

    Returns:
        dict: dictionary containing state: success or failure; and reason if failure
    """
    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        # If we can create an AppCommon object we are able to get an access token.
        app_common = AppCommon(PACKAGE_NAME, app_configs)
        _, reason = app_common.query_entities_since_ts(int(time.time()))
        state = "success" if not reason else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }
