# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from virus_total_apis import PublicApi as VirusTotal

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

HTTP_OK = 200

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    TEST_IP = "8.8.8.8"

    options = opts.get("fn_virustotal", {})

    reason = ""
    try:
        vt = VirusTotal(options['api_token'], options['proxies'])
        response = vt.get_ip_report(TEST_IP)

        if response and type(response) is not dict:
            state = "failure"
            reason = "no response"
        else:
            status = response.get('response_code', -1)

            if status != HTTP_OK:
                state = "failure"
                reason = state
            else:
                state = "success"
    except Exception as err:
        state = "failure"
        reason = str(err)

    result = {"state": state,
            "reason": reason
           }

    log.info(result)

    return result