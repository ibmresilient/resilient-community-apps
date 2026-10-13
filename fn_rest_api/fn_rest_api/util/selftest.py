# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: 
    resilient-circuits selftest -l fn-rest-api
    resilient-circuits selftest --print-env -l fn-rest-api

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
from requests import JSONDecodeError
from fn_rest_api.components.funct_rest_api import make_rest_call

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

PACKAGE = "fn_rest_api"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    headers = {
        "Content-type": "application/json; charset=UTF-8"
    }

    app_config = opts.get(PACKAGE, {})

    # if missing, no url call is made
    test_url = app_config.get("selftest_url")

    reason = None
    state = True
    content = {}

    if test_url:
        try:
            # make_rest_call(opts, options, rest_method, rest_url, headers_dict, cookies_dict, rest_body, rest_verify)
            resp = make_rest_call(
                opts, opts.get(PACKAGE, {}),
                method="get",
                url=test_url,
                headers=headers,
                verify=False,
                timeout=600)

            state = "success"
            try:
                content = resp.json()
            except JSONDecodeError:
                content = resp.text
        except Exception as e:
            state = "failure"
            reason = e.args[0]

    result = {
        "state" : state,
        "reason": reason,
        "content": content
    }

    return result
