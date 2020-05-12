# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_hibp
"""

from fn_hibp.lib.common import HAVE_I_BEEN_PWNED_BREACH_URL, get_config_option, make_headers, get_proxies
from resilient_lib.components.resilient_common import validate_fields
import requests


TEST_EMAIL = "test&commat;example.com"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        options = opts.get("fn_hibp", {})
        hibp_api_key = options.get("hibp_api_key")
        validate_fields(["hibp_api_key"], options)

        headers= make_headers(hibp_api_key)
        proxies = get_proxies(options)

        test_url = "{0}/{1}".format(HAVE_I_BEEN_PWNED_BREACH_URL, hibp_api_key)
        breaches_response = requests.get(test_url, headers=headers, proxies=proxies)

        if breaches_response.status_code != 401:
            msg = None
        else:
            msg = "Have I Been Pwned API Key has not been found. Please add API Key to app.config"

        return {
            "state": "success" if not msg else msg,
            "reason": msg
        }
    except Exception as err:
        return {
            "state": str(err),
            "reason": str(err)
        }
