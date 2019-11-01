# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_hibp
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
        options = opts.get("fn_hibp", {})
        hibp_api_key = options.get("hibp_api_key")
        validate_fields(["[hibp_api_key]"], options)

        url = "https://haveibeenpwned.com/api/v3/{}/{}/host/{}/{}".format(hibp_api_key, "haveibeenpwned.com", "")
        req_common = RequestsCommon(opts, options)

        req_common.execute_call("get", url, payload={}, log=log, resp_type="text")

        return {"state": "success"}
    except Exception:
        return {"state": "failed"}
