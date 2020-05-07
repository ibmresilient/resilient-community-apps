# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_cve_search
"""

import logging
from pdpyras import APISession

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)
LOG.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    # Reading configuration variables from app.config file
    options = opts.get("pagerduty", {})

    try:
        session = APISession(options['api_token'])
        session.get('users')

        return {"state": "Success"}

    except Exception as err:
        LOG.info("Failed Connection to PagerDuty Error - {}".format(err))
        return {
            "state": "Failed",
            "reason": str(err)
        }
