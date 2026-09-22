# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import sys
import json
import logging
from io import BytesIO, StringIO
from resilient_circuits import ResilientComponent, function, \
    handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, \
    ResultPayload, RequestsCommon, str_to_bool, write_file_attachment
from fn_rsa_netwitness.util.helper import get_headers, convert_to_nw_time

log = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'netwitness_query_event_session"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_rsa_netwitness", {})

        # Validate app.config fields
        validate_fields(["nw_log_server_url", "nw_log_server_user", \
            "nw_log_server_password"], self.options)

        self.options["nw_log_server_verify"] = str_to_bool(self.options.get("nw_log_server_verify"))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})
        # Validate app.config fields
        validate_fields(["nw_log_server_url", "nw_log_server_user", \
            "nw_log_server_password"], self.options)

    @function("netwitness_retrieve_log_data")
    def _netwitness_retrieve_log_data(self, event, *args, **kwargs):
        """Function: Returns back either a log file from Netwitness."""
        try:
            # Get the function parameters:
            nw_data_format = self.get_select_param(kwargs.get("nw_data_format"))  # select

            yield StatusMessage("Retrieving {} logs...".format(nw_data_format))

            nw_start_time = kwargs.get("nw_start_time")  # int
            if nw_start_time is None:
                raise FunctionError("nw_start_time must be set in order to run this function.")

            nw_end_time = kwargs.get("nw_end_time")  # int
            if nw_end_time is None:
                raise FunctionError("nw_end_time must be set in order to run this function.")

            incident_id = kwargs.get("incident_id")     # number

            # Initialize resilient_lib objects (handles the select input)
            results_payload = ResultPayload("fn_rsa_netwitness", **kwargs)
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

            # Dict lookup for render format
            render_format_dict = {
                "logs_text": "logs",
                "logs_csv": "text/csv",
                "logs_xml": "text/xml",
                "logs_json": "application/json"
            }

            # Make sure format is a supported case
            if nw_data_format not in render_format_dict:
                raise FunctionError("{} is not a supported format to retrieve logs"\
                    .format(nw_data_format))

            # Return log data in json format
            if nw_data_format == "logs_json":
                data_file = get_nw_session_logs_file(url, username, password, nw_verify, \
                    start_time, end_time, req_common, render_format=render_format_dict[nw_data_format], resp_type="json")

            # Return log data in text format
            else:
                data_file = get_nw_session_logs_file(url, username, password, nw_verify, \
                    start_time, end_time, req_common, render_format=render_format_dict[nw_data_format])

            log.debug("data_file: %s", data_file)
            results = results_payload.done(True, data_file)
            log.debug("RESULTS: %s", results)

            # Check for empty log files
            # (if empty, no log file will be attached and a note will
            # be added in the workflow post-process)
            if results["content"]:
                yield StatusMessage("Logs found, creating attachment...")
                # Get client, attachment name, and content of log files from netwitness
                rest_client = self.rest_client()

                # Determine the proper extension for the attachment name
                if nw_data_format == "logs_text":
                    ext = "txt"
                else:
                    ext = nw_data_format[5:]    # for csv, xml, json

                attachment_name = u"Log file for {} - {}.{}".format(nw_start_time, nw_end_time, ext)

                if nw_data_format == "logs_json":
                    datastream = BytesIO(json.dumps(results['content'], indent = 4).encode('utf-8'))
                elif sys.version_info.major < 3:
                    datastream = StringIO(results["content"])
                else:
                    datastream = BytesIO(results["content"].encode("utf-8"))

                write_file_attachment(rest_client, attachment_name,\
                    datastream, incident_id, None)

            yield StatusMessage("Done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)

def get_nw_session_logs_file(url, user, passw, cafile, time1, time2,
                             req_common, render_format, resp_type="text"):

    headers = get_headers(user, passw)
    request_url = "{}/sdk/packets?time1={}&time2={}&render={}"\
        .format(url, time1, time2, render_format)

    resp = req_common.execute_call_v2("GET", request_url, verify=cafile, headers=headers)

    if resp.text == '</Logs>\n' or resp.text == '\n]}\n':
        resp = ''
    elif resp_type == "json" and '"logs":' in resp.text:
        resp = resp.json()
    else:
        resp = resp.text

    return resp
