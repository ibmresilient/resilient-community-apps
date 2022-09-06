# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_xforce
"""

import logging
from fn_cloud_foundry.util.cloud_foundry_api import IBMCloudFoundryAPI
from fn_cloud_foundry.util.authentication.ibm_cf_bearer import IBMCloudFoundryAuthenticator

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    # read options from app.config
    options = opts.get("fn_cloud_foundry", {})

    base_url = options.get("cf_api_base")

    authenticator = IBMCloudFoundryAuthenticator(opts, options, base_url)
    log.info("Authenticated into Cloud Foundry")
    cf_service = IBMCloudFoundryAPI(opts, options, base_url, authenticator)

    # make the request
    try:
        response = cf_service.get_apps()
        if int(response.status_code / 100) == 2:
            state = "success"
            reason = "Connected to the Cloud Foundry API"
        else:
            state = "failure"
            reason = "Test failed with http status code {}".format(response.status_code)
    except Exception as e:
        state = "failure"
        reason = str(e)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)

    return result
