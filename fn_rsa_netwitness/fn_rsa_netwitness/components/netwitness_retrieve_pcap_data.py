# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon, str_to_bool
from fn_rsa_netwitness.util.helper import remove_dir, create_tmp_file, get_headers, convert_to_nw_time

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'netwitness_query_event_session"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_rsa_netwitness", {})

        # Validate app.config fields
        validate_fields(["nw_packet_server_url", "nw_packet_server_user", "nw_packet_server_password"], self.options)

        self.options["nw_packet_server_verify"] = str_to_bool(self.options.get("nw_packet_server_verify"))

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})

    @function("netwitness_retrieve_pcap_data")
    def _netwitness_retrieve_pcap_data(self, event, *args, **kwargs):
        """Function: Returns back either a pcap file from Netwitness,
        and attaches it to an incident."""
        temp_d = None
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            nw_event_session_ids = kwargs.get("nw_event_session_ids")  # text
            nw_start_time = kwargs.get("nw_start_time")  # text
            nw_end_time = kwargs.get("nw_end_time")  # text
            incident_id = str(kwargs.get("incident_id"))  # number

            # Initialize resilient_lib objects (handles the select input)
            rp = ResultPayload("fn_rsa_netwitness", **{"nw_event_session_ids": nw_event_session_ids,
                                                                      "incident_id": incident_id})
            req_common = RequestsCommon(self.opts)

            # Verify inputs are set correctly
            if nw_event_session_ids is None:
                if nw_start_time is None and nw_end_time is None:
                    raise FunctionError("Either nw_event_session_ids or nw_start_time and nw_end_time must be set for "
                                        "this function to run correctly.")
                elif nw_start_time is None or nw_end_time is None:
                    raise FunctionError("nw_start_time and nw_end_time must both be set in order to retrieve data "
                                        "based on time.")

            log.info("nw_event_session_ids: %s", nw_event_session_ids)
            log.info("nw_start_time: %s", nw_start_time)
            log.info("nw_end_time: %s", nw_end_time)
            log.info("incident_id: %s", incident_id)

            # Get all common variables from app.config
            url = self.options.get("nw_packet_server_url")
            username = self.options.get("nw_packet_server_user")
            password = self.options.get("nw_packet_server_password")
            nw_verify = self.options.get("nw_packet_server_verify")

            # User session id if avaiable
            if nw_event_session_ids:
                pcap_file = get_nw_session_pcap_file(url, username, password, nw_verify, nw_event_session_ids,
                                                     req_common)
                file_name = "PCAP file for session IDs: {}.pcap".format(nw_event_session_ids)
            else:
                nw_start = convert_to_nw_time(nw_start_time)
                nw_end = convert_to_nw_time(nw_end_time)

                pcap_file = get_nw_session_pcap_file_time(url, username, password, nw_verify, nw_start, nw_end,
                                                          req_common)
                file_name = "PCAP file between {} and {}.pcap".format(nw_start, nw_end)

            temp_d, temp_f = create_tmp_file(pcap_file)
            log.debug("pcap_file: {}".format(pcap_file))

            resilient_client = self.rest_client()
            resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                             temp_f, filename=file_name)
            yield StatusMessage("PCAP file added as attachment to Incident {}".format(str(incident_id)))

            results = rp.done(True, {})
            yield StatusMessage("Done...")
            log.debug("RESULTS: %s", results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
        finally:
            if temp_d:
                remove_dir(temp_d)


def get_nw_session_pcap_file(url, user, pw, cafile, event_session_id, req_common):
    headers = get_headers(user, pw)
    request_url = "{}/sdk/packets?sessions={}&render=pcap".format(url, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers, resp_type='bytes')


def get_nw_session_pcap_file_time(url, user, pw, cafile, start_time, end_time, req_common):
    headers = get_headers(user, pw)
    request_url = "{}/sdk/packets?time1={}&time2={}&render=pcap".format(url, start_time, end_time)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers, resp_type="bytes")
