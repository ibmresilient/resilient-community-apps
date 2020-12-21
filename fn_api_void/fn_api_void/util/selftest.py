# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_api_void
"""

import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_api_void", {})

    log = logging.getLogger(__name__)
    rp = ResultPayload("fn_api_void", **kwargs)

    # Add support for Requests Common
    req_common = RequestsCommon(self.opts, self.options)

    apivoid_base_url = self.options.get("apivoid_base_url")
    apivoid_sub_url = self.options.get("apivoid_sub_url")
    apivoid_api_key = self.options.get("apivoid_api_key")

    # Get the function parameters:
    artifact_value = kwargs.get("api_void_artifact_value")  # text
    validate_fields(["api_void_artifact_value"], kwargs)

    log.info("api_void_artifact_value: %s", artifact_value)

    urlencoded_url = urllib.parse.quote_plus(artifact_value)

    url = "/".join((apivoid_base_url, "urlrep", apivoid_sub_url))
    url = u"{0}/?key={1}&url={2}".format(url, apivoid_api_key, urlencoded_url)

    response = req_common.execute_call_v2(method="get", url=url)

    response_json = response.json()

    yield StatusMessage("APIVoid URL reputation function completed successfully...")
    results = rp.done(True, response_json)

    # Produce a FunctionResult with the results
    yield FunctionResult(results)

except Exception as e:
yield FunctionError(e)

    return {
        "state": "unimplemented",
        "reason": None
    }