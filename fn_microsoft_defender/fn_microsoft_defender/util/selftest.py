# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
import logging
from resilient_lib import IntegrationError
from fn_microsoft_defender.lib.defender_common import DefenderAPI, PACKAGE_NAME
"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_microsoft_defender
"""

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get(PACKAGE_NAME, {})

    defender_api = DefenderAPI(options['tenant_id'],
                               options['client_id'],
                               options['app_secret'],
                               opts,
                               options)

    try:
        _access_token = defender_api.defender_authenticate()
        result = {
            "state": "success",
            "reason": None
        }
    except IntegrationError as err:
        result = {
            "state": "failure",
            "reason": str(err)
        }

    return result
