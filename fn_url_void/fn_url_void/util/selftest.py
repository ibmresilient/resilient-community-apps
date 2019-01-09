# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-url-void
"""

import logging
from resilient_lib import RequestsCommon
from resilient_lib.components.resilient_common import validate_fields

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        function_options = opts.get("fn_url_void", {})
        identifier = function_options.get("identifier")
        api_key = function_options.get("api_key", "api1000")
        validate_fields(["api_key"], function_options)
        req_common = RequestsCommon(opts, function_options)

        url = "https://api.urlvoid.com/{}/{}/host/{}/{}".format(identifier, api_key, "urlvoid.com", "")
        req_common.execute_call("get", url, payload={}, log=log, resp_type="text")

        return {"state": "success"}
    except Exception:
        return {"state": "failed"}
