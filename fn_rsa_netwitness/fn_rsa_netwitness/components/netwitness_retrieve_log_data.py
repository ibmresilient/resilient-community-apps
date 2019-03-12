# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_rsa_netwitness.util.helper import get_headers, convert_to_nw_time

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'netwitness_query_event_session"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_rsa_netwitness", {})

        # Validate app.config fields
        validate_fields(["nw_log_server_url", "nw_log_server_user", "nw_log_server_password"], self.options)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})

    @function("netwitness_retrieve_log_data")
    def _netwitness_retrieve_log_data(self, event, *args, **kwargs):
        """Function: Returns back either a log or pcap file from Netwitness,
        attaches it to an incident if it is a pcap file."""
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            nw_data_format = self.get_select_param(kwargs.get("nw_data_format"))  # select
            nw_start_time = kwargs.get("nw_start_time")  # text
            nw_end_time = kwargs.get("nw_end_time")  # text

            # Initialize resilient_lib objects (handles the select input)
            rp = ResultPayload("netwitness_retrieve_session_data", **kwargs)
            req_common = RequestsCommon(self.opts)

            log.info("nw_data_format: %s", nw_data_format)
            log.info("nw_start_time: %s", nw_start_time)
            log.info("nw_end_time: %s", nw_end_time)

            data_file = {}
            start_time = convert_to_nw_time(nw_start_time)
            end_time = convert_to_nw_time(nw_end_time)

            # Get all common variables from app.config
            url = self.options.get("nw_log_server_url")
            username = self.options.get("nw_log_server_user")
            password = self.options.get("nw_log_server_password")
            nw_verify = self.options.get("nw_log_server_verify")

            # Get log data as a line delimited text format
            if nw_data_format == "logs_text":
                data_file = get_nw_session_logs_file(url, username, password, nw_verify, start_time, end_time,
                                                     req_common, render_format="logs")

            # Get log data in csv format
            elif nw_data_format == "logs_csv":
                data_file = get_nw_session_logs_file(url, username, password, nw_verify, start_time, end_time,
                                                     req_common, render_format="text/csv")

            # Get log data in xml format
            elif nw_data_format == "logs_xml":
                data_file = get_nw_session_logs_file(url, username, password, nw_verify, start_time, end_time,
                                                     req_common, render_format="text/xml")

            # Get log data in json format
            elif nw_data_format == "logs_json":
                data_file = get_nw_session_json_file(url, username, password, nw_verify, start_time, end_time,
                                                     req_common)

            log.debug("data_file: {}".format(data_file))
            results = rp.done(True, data_file)
            yield StatusMessage("Done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


def get_nw_session_logs_file(url, user, pw, cafile, time1, time2, req_common, render_format):
    headers = get_headers(user, pw)
    request_url = "{}/sdk/packets?time1={}&time2={}&render={}".format(url, time1, time2, render_format)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers, resp_type="text")


def get_nw_session_json_file(url, user, pw, cafile, time1, time2, req_common):
    headers = get_headers(user, pw)
    request_url = "{}/sdk/packets?time1={}&time2={}&render=application/json".format(url, time1, time2)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)
