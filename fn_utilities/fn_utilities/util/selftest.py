# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_utilities.components.utilities_call_rest_api import make_rest_call

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

HTTP_OK = 200

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    TEST_IP = "https://postman-echo.com"

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    payload = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }

    reason = None
    try:
        # make_rest_call(opts, options, rest_method, rest_url, headers_dict, cookies_dict, rest_body, rest_verify)
        resp = make_rest_call(opts, opts.get("fn_utilities", {}),
                              "POST", "/".join((TEST_IP, "post")), headers, None, payload, False)

        state = "success"
    except Exception as e:
        state = "failure"
        reason = e.args[0]

    result = {
        "state": state,
        "reason": reason
    }

    return result
