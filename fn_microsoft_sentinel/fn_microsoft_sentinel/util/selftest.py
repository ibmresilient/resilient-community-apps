# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_microsoft_sentinel
"""

import logging
from resilient_lib import validate_fields, IntegrationError
from fn_microsoft_sentinel.lib.sentinel_common import SentinelAPI, PACKAGE_NAME

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get(PACKAGE_NAME, {})

    validate_fields(
        ["tenant_id", "client_id", "app_secret"],
        app_configs
    )

    sentinel_api = SentinelAPI(app_configs['tenant_id'],
                               app_configs['client_id'],
                               app_configs['app_secret'],
                               opts, app_configs)

    reason = None
    try:
        state = "success" if sentinel_api._authenticate() else "failure"
    except IntegrationError as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }
