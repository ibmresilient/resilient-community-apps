# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_hibp
"""

from fn_hibp.lib.common import HAVE_I_BEEN_PWNED_BREACH_URL, Hibp
from resilient_lib import validate_fields, IntegrationError

TEST_EMAIL = "test&commat;example.com"

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        options = opts.get("fn_hibp", {})
        hibp = Hibp(options)

        test_url = "{0}/{1}".format(HAVE_I_BEEN_PWNED_BREACH_URL, TEST_EMAIL)

        err_msg = None
        try:
            _ = hibp.execute_call(test_url)
        except IntegrationError as err:
            err_msg = str(err)

        return {
            "state": "success" if not err_msg else "failed",
            "reason": err_msg
        }
    except Exception as err:
        return {
            "state": str(err),
            "reason": str(err)
        }
