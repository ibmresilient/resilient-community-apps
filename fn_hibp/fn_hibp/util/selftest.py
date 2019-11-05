# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_hibp
"""

import logging
from resilient_lib.components.resilient_common import validate_fields
import requests
from resilient_circuits import StatusMessage

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
        HAVE_I_BEEN_PWNED_API_KEY_URL: "https://haveibeenpwned.com/api/v3/"

        api_key_url = "{0}/{1}".format(HAVE_I_BEEN_PWNED_API_KEY_URL, hibp_api_key)
        breaches_response = requests.get(api_key_url)

        if breaches_response.status_code != 401:
            yield StatusMessage("Have I Been Pwned API Key has been found")
        else:
            yield StatusMessage("Have I Been Pwned API Key has not been found. Please add API Key to app.config")

        return {"state": "success"}
    except Exception:
        return {"state": "failed"}
