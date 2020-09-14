# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_xforce
"""

import logging
from resilient_lib import validate_fields, RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    # read options from app.config
    options = opts.get("fn_xforce", {})

    # check that an API key, password, and base URL are provided
    validate_fields([{'name': 'xforce_apikey', 'placeholder': ' <YOUR_API_KEY>'}, {'name': 'xforce_password', 'placeholder': '<YOUR_API_PASSWORD>'}, 'xforce_baseurl'], options)

    # set API key, password, and base URL
    XFORCE_API_KEY = options['xforce_apikey']
    XFORCE_PASSWORD = options['xforce_password']
    BASE_URL = options['xforce_baseurl']

    # construct the URL
    testID = "e7dd02a139820860866a4fdd82cf9d8e"
    request_string = '{}/casefiles/{}'.format(BASE_URL, testID)

    # make the request
    state = reason = ""
    try:
        rc = RequestsCommon()
        res = rc.execute_call_v2(
                        "get", request_string, auth=(XFORCE_API_KEY, XFORCE_PASSWORD))
        if (res.status_code / 100) == 2:
            state = "success"
            reason = "Connected to the X-Force API"
        else:
            state = "failure"
            reason = "Test failed with http status code {}".format(res.status_code)
    except Exception as e:
        state = "failure"
        reason = str(e)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)

    return result
