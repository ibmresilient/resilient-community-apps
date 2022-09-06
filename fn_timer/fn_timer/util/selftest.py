# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-timer
    resilient-circuits selftest --print-env -l fn-timer

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
from resilient_lib import RequestsCommon

CONTENT_TYPE = "Content-type"
CONTENT_TYPE_JSON = "application/json"

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_timer", {})

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
                              "POST", "/".join((TEST_IP, "post")), headers, None, payload, False, 600)

        state = "success"
    except Exception as e:
        state = "failure"
        reason = e.args[0]

    result = {
        "state": state,
        "reason": reason
    }

    return result

def make_rest_call(opts, options, rest_method, rest_url, headers_dict, cookies_dict, rest_body, rest_verify, rest_timeout):
    rc = RequestsCommon(opts, options)

    if CONTENT_TYPE in headers_dict and CONTENT_TYPE_JSON in headers_dict[CONTENT_TYPE]:
        return rc.execute_call_v2(rest_method, rest_url,
                                  headers=headers_dict,
                                  cookies=cookies_dict,
                                  json=rest_body,
                                  verify=rest_verify,
                                  timeout=rest_timeout)

    return rc.execute_call_v2(rest_method, rest_url,
                              headers=headers_dict,
                              cookies=cookies_dict,
                              data=rest_body,
                              verify=rest_verify,
                              timeout=rest_timeout)