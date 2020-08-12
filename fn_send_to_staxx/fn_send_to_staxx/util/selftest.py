# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_send_to_staxx
"""

import logging
from fn_send_to_staxx.lib.staxx_lib import StaxxClient
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("staxx", {})

    staxx_ip = app_configs.get('staxx_ip')
    staxx_port = app_configs.get('staxx_port')
    staxx_user = app_configs.get('staxx_user')
    staxx_password = app_configs.get('staxx_password')

    try:
        staxx = StaxxClient("https://{}:{}".format(staxx_ip, staxx_port),
                            staxx_user,
                            staxx_password,
                            RequestsCommon(opts, app_configs)
                            )
        state = "success"
        reason = None
    except Exception as err:
        state = "failure"
        reason = str(err)

    return {
        "state": state,
        "reason": reason
    }
