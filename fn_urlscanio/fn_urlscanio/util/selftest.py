# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_urlscanio
"""

import logging
import json
from resilient_lib import validate_fields, RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    # Read option from app.config
    options = opts.get("urlscanio", {})

    # check that an API key and URLs are provided
    validate_fields(['urlscanio_api_key', 'urlscanio_report_url', 'urlscanio_screenshot_url'], options)

    # set API key and report URL
    urlscanio_api_key = options['urlscanio_api_key']
    urlscanio_report_url = options['urlscanio_report_url']

    # Construct the parameters to send to urlscan.io
    urlscanio_headers = {'Content-Type': 'application/json', 'API-Key': urlscanio_api_key}
    urlscanio_data = {
        "url": "https://www.ibm.com"
    }

    # Set URL to make a request to
    urlscanio_scan_url = "{}/scan/".format(urlscanio_report_url)

    # Initialize RequestsCommon
    req_common = RequestsCommon()

    # Attempt the request
    state, reason = "", ""
    try:
        resp = req_common.execute_call_v2("POST", urlscanio_scan_url,
                                          headers=urlscanio_headers,
                                          data=json.dumps(urlscanio_data))
        if resp.status_code == 200:
            state = "success"
            reason = "Connected to urlscanio API"
        else:
            state = "failure"
            reason = "Test failed with http status code {}".format(resp.status_code)

    except Exception as e:
        state = "failure"
        reason = str(e)

    result = {
        "state": state,
        "reason": reason
    }

    log.info(result)

    return result
