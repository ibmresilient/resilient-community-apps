# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation
   test with: resilient-circuits selftest -l fn_rsa_netwitness
"""

import logging
import time
from resilient_lib import str_to_bool, RequestsCommon
from fn_rsa_netwitness.util.helper import get_headers

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_rsa_netwitness", {})
    nw_packet_server_url = options.get("nw_packet_server_url")
    nw_packet_server_user = options.get("nw_packet_server_user")
    nw_packet_server_password = options.get("nw_packet_server_password")
    nw_packet_server_verify = str_to_bool(options.get("nw_packet_server_verify"))

    nw_log_server_url = options.get("nw_log_server_url")
    nw_log_server_user = options.get("nw_log_server_user")
    nw_log_server_password = options.get("nw_log_server_password")
    nw_log_server_verify = str_to_bool(options.get("nw_log_server_verify"))

    try:
        rc = RequestsCommon(options, opts)

        # Test PCAP server connection
        headers = get_headers(nw_packet_server_user, nw_packet_server_password)
        request_url = "{}/sdk/packets?sessions={}&render=pcap".format(nw_packet_server_url, "100")
        rc.execute_call("GET", request_url, verify_flag=nw_packet_server_verify, headers=headers, resp_type='bytes')

        # Test Logger server connection
        time1 = int(time.time()) * 1000
        time2 = int(time.time()) * 1000
        headers = get_headers(nw_log_server_user, nw_log_server_password)
        request_url = "{}/sdk/packets?time1={}&time2={}&render={}".format(nw_log_server_url, time1, time2, "logs")
        rc.execute_call("GET", request_url, verify_flag=nw_log_server_verify, headers=headers, resp_type="text")

        return {"state": "success"}
    except Exception as err:
        err_reason_msg = """Could not connect to NetWitness.
                    error: {0}
                    ---------
                    Current Configs in app.config file::
                    ---------
                    nw_packet_server_url: {1}
                    nw_packet_server_user: {2}
                    nw_packet_server_verify: {3}
                    nw_log_server_url: {4}
                    nw_log_server_user: {5}
                    nw_log_server_verify: {6}\n""".format(
            err,
            nw_packet_server_url,
            nw_packet_server_user,
            nw_packet_server_verify,
            nw_log_server_url,
            nw_log_server_user,
            nw_log_server_verify)

        log.error(err_reason_msg)

        return {"state": "failed"}
