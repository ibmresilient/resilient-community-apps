# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""

from logging import getLogger, INFO, StreamHandler
from resilient_lib import validate_fields
from fn_virustotal.lib.vt_common import VirusTotalClient

log = getLogger(__name__)
log.setLevel(INFO)
log.addHandler(StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    TEST_IP = "8.8.8.8"

    options = opts.get("fn_virustotal", {})
    validate_fields(['api_token', 'polling_interval_sec', 'max_polling_wait_sec'], options)
    reason = ""
    try:
        vt = VirusTotalClient(opts, options)
        response, code = vt.get_ip_report(TEST_IP)

        if response and type(response) is not dict:
            state = "failure"
            reason = "no response"
        else:
            if code == "success":
                state = "success"
            else:
                state = "failure"
                reason = code

    except Exception as err:
        state = "failure"
        reason = str(err)

    result = {
        "state": state,
        "reason": reason}

    log.info(result)

    return result
