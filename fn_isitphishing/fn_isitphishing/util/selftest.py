# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2020. All Rights Reserved.

"""Function implementation
   test with: resilient-circuits selftest -l fn_isitphishing
"""

import logging
import requests
from resilient_lib import RequestsCommon, validate_fields
from fn_isitphishing.lib.isitphishing_helper import IsItPhishingHelper

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

TIME_OUT = 500   # seconds

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_isitphishing", {})

    validate_fields(['isitphishing_api_url', 'isitphishing_id', 'isitphishing_secret'], options)

    # Get the license key to access the API endpoint.
    api_endpoint_url = options.get("isitphishing_api_url")
    auth_url = options.get("authentication_url")
    client_id = options.get("isitphishing_id")
    client_secret = options.get("isitphishing_secret")

    api_url = f"{api_endpoint_url}/url"

    payload = {"url": "http://www.thisisaphishingurl.com", "force": False, "smart": True, "timeout": TIME_OUT}

    state = ""
    reason = None

    try:
        # Create IsItPhishingHelper class object
        isitphishing_helper = IsItPhishingHelper(api_url,
                                                 auth_url,
                                                 client_id,
                                                 client_secret,
                                                 RequestsCommon(opts, options).get_proxies())

        # Get a session token
        session_token = isitphishing_helper.authenticate(client_id, client_secret)

        if isitphishing_helper and session_token:

            try:
                # Build the header and the data payload.
                headers = {
                    "Authorization": f"Bearer {session_token}",
                    "Content-type": "application/json",
                }

                response = requests.post(api_url, headers=headers, json=payload, timeout=50)

                # Check the results
                if response.status_code == 200:
                    state = "success"
                else:
                    state = "failure"
                    reason = response.status_code
            except requests.exceptions.RequestException as ex:
                state = "failure"
                reason = str(ex)

    except ConnectionError:
        state = "failure"
        reason = "authentication failure"

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)
    return result
