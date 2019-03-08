# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_rsa_netwitness.util.helper import get_headers

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'netwitness_query_event_session"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_rsa_netwitness", {})

        # Validate app.config fields
        validate_fields(["nw_url", "nw_user", "nw_password", "nw_port"], self.options)

        if self.options.get("cafile").lower() == "false":
            self.options["cafile"] = False
        elif self.options.get("cafile").lower() == "true":
            self.options["cafile"] = True

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})

    @function("netwitness_retrieve_session_data")
    def _netwitness_retrieve_log_data(self, event, *args, **kwargs):
        """Function: Returns back either a log or pcap file from Netwitness,
        attaches it to an incident if it is a pcap file."""
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            nw_event_session_ids = kwargs.get("nw_event_session_ids")  # text
            nw_data_format = self.get_select_param(kwargs.get("nw_data_format"))  # select
            incident_id = str(kwargs.get("incident_id"))  # number

            # Initialize resilient_lib objects (handles the select input)
            rp = ResultPayload("netwitness_retrieve_session_data", **{"nw_event_session_ids": nw_event_session_ids,
                                                                      "nw_data_format": nw_data_format,
                                                                      "incident_id": incident_id})
            req_common = RequestsCommon(self.opts)

            validate_fields(["nw_event_session_id", "nw_data_format", "incident_id"], **kwargs)

            log.info("nw_event_session_ids: %s", nw_event_session_ids)
            log.info("nw_data_format: %s", nw_data_format)
            log.info("incident_id: %s", incident_id)

            data_file = {}

            # Get all common variables from app.config
            url = self.options.get("nw_url")
            port = self.options.get("nw_port")
            username = self.options.get("nw_user")
            password = self.options.get("nw_password")
            nw_cafile = self.options.get("cafile")

            # Get log data as a line delimited text format
            if nw_data_format == "logs_text":
                data_file = get_nw_session_logs_file(url, port, username, password, nw_cafile, nw_event_session_ids,
                                                     req_common, render_format="logs")

            # Get log data in csv format
            elif nw_data_format == "logs_csv":
                data_file = get_nw_session_logs_file(url, port, username, password, nw_cafile, nw_event_session_ids,
                                                     req_common, render_format="text/csv")

            # Get log data in xml format
            elif nw_data_format == "logs_xml":
                data_file = get_nw_session_logs_file(url, port, username, password, nw_cafile, nw_event_session_ids,
                                                     req_common, render_format="text/xml")

            # Get log data in json format
            elif nw_data_format == "logs_json":
                data_file = get_nw_session_json_file(url, port, username, password, nw_cafile, nw_event_session_ids,
                                                     req_common)

            log.debug("data_file: {}".format(data_file))
            results = rp.done(True, data_file)
            yield StatusMessage("Done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


def get_nw_session_logs_file(url, port, user, pw, cafile, event_session_id, req_common, render_format):
    headers = get_headers(user, pw)
    request_url = "{}:{}/sdk/packets?sessions={}&render={}".format(url, port, event_session_id, render_format)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)


def get_nw_session_json_file(url, port, user, pw, cafile, event_session_id, req_common):
    headers = get_headers(user, pw)
    request_url = "{}:{}/sdk/packets?sessions={}&render=application/json".format(url, port, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)
