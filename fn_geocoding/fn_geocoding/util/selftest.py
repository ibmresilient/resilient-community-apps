# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from fn_geocoding.util.request_common import execute_call

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple api test to confirm access
    """
    options = opts.get("fn_geocoding", {})

    url = options['url']
    payload = { "key": options['api_key'],
                "latlng": "42.3656119,-71.0805841"
                }

    response = execute_call(log, "get", url, None, None, payload, True, None, None)

    if response and response['status'] == "OK":
        return {
            "state": "success",
            "response": response
        }
    else:
        log.error(response)
        return {
            "state": "failure"
        }