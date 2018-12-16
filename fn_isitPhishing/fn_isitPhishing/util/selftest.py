# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_isitPhishing
"""

import requests
import logging
from fn_isitPhishing.lib.isitphishing_util import get_license_key

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_isitPhishing", {})

    # Get the license key to access the API endpoint.
    auth_token = get_license_key(options["isitphishing_name"], options["isitphishing_license"])

    # Build the header and the data payload.
    headers = {
        "Authorization": u'Bearer {}'.format(auth_token),
        "Content-type": "application/json",
    }
    api_url = u"{0}/url".format(options['isitphishing_api_url'])

    payload = {"url": "http://www.thisisaphishingurl.com", "force": False, "smart": True, "timeout": 8000}

    state, reason = "", ""
    try:
        response = requests.post(api_url, headers=headers, json=payload)

        # Check the results
        if response.status_code == 200:
            state = "success"
        else:
            state = "failure"
            reason = response.error
    except Exception as ex:
        state = "failure"
        reason = str(ex)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result