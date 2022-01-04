# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# # -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-sentinelone
    resilient-circuits selftest --print-env -l fn-sentinelone

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
from resilient_lib import validate_fields, IntegrationError, RequestsCommon
from fn_sentinelone.lib.sentinelone_common import SentinelOneClient

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_sentinelone", {})

    required_fields = ["sentinelone_server", "api_token", "api_version"]
    validate_fields(required_fields, app_configs)

    # Create api client
    rc = RequestsCommon(opts, app_configs)
    sentinelone_client = SentinelOneClient(opts, app_configs)

    reason = None
    try:
        state = "success" if sentinelone_client.get_system_info() else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }
