# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_api_void
"""

import logging

LOG = logging.getLogger(__name__)
from resilient_lib import RequestsCommon, validate_fields
from fn_api_void.lib.apivoid_helper import make_apivoid_api_call
PACKAGE_NAME = "fn_api_void"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get(PACKAGE_NAME, {})
    rc = RequestsCommon(opts, options)
    reason = "Test was successful!"

    try:
        # Get and validate app configs
        valid_app_configs = validate_fields(["apivoid_base_url", "apivoid_sub_url", "apivoid_api_key"], options)

        # Execute api call
        res = make_apivoid_api_call(
            base_url=valid_app_configs.get("apivoid_base_url"),
            sub_url=valid_app_configs.get("apivoid_sub_url"),
            query_type="selftest",
            value=True,
            api_key=valid_app_configs.get("apivoid_api_key"),
            rc=rc
        )

        res = res.json()

        if res.get("success"):
            LOG.info("%s\nCredits Remaining:\t%s\nEstimated Queries:\t%s", reason, res.get("credits_remained", "Unknown"), res.get("estimated_queries", "Unknown"))
            return {"state": "success"}

        elif res.get("error"):
            reason = res.get("error")
            LOG.error(reason)
            return {"state": "failure", "reason": reason}

        reason = "Test was not successful. An unknown error occurred"
        LOG.error(reason)
        return {"state": "failure", "reason": reason}

    except Exception as err:
        LOG.error(err)
        return {"state": "failure", "reason": err}