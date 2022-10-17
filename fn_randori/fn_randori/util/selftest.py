# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-randori
    resilient-circuits selftest --print-env -l fn-randori

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
from resilient_lib import RequestsCommon, IntegrationError
from fn_randori.lib.app_common import AppCommon, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Call Randori validate endpoint to make sure we can access 
    the endpoint and it is configured properly.
    """

    try:
        app_configs = opts.get(PACKAGE_NAME, {})
        rc = RequestsCommon(opts, app_configs)

        app_common = AppCommon(rc, PACKAGE_NAME, app_configs)
        result = app_common.get_validate()
        reason = None
        # Get the list of permissions
        perms = result.get("perms")
        if perms and "authenticated" in perms:
            state = "success"
        else:
            state = "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }