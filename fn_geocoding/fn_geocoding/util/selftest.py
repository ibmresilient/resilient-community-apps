# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Simple api test to confirm access
    """
    options = opts.get("fn_geocoding", {})

    url = options['url']
    payload = {
        "key": options['api_key'],
        "latlng": "42.3656119,-71.0805841"
    }

    rc = RequestsCommon(opts, options)
    response = rc.execute_call_v2("get", url, params=payload)
    if response and response.json()['status'] == "OK":
        return {
            "state": "success",
            "response": response.json()
        }
    else:
        log.error(response)
        return {
            "state": "failure",
            "reason": str(response.text)
        }