# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

import logging
from pdpyras import APISession

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("pagerduty", {})

    try:
        session = APISession(app_configs.get('api_token'))
        session.get('users')

        return {"state": "Success"}

    except Exception as err:
        log.info("Failed Connection to PagerDuty Error - {}".format(err))
        return {
            "state": "Failed",
            "reason": str(err)
        }
