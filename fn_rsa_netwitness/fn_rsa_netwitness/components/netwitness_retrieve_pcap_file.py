# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_rsa_netwitness.util.helper import remove_dir, create_tmp_file, get_headers

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
    def _netwitness_retrieve_session_data(self, event, *args, **kwargs):
        """Function: Returns back either a log or pcap file from Netwitness,
        attaches it to an incident if it is a pcap file."""
        temp_d = None
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

            # Get all common variables from app.config
            url = self.options.get("nw_url")
            port = self.options.get("nw_port")
            username = self.options.get("nw_user")
            password = self.options.get("nw_password")
            nw_cafile = self.options.get("cafile")

            pcap_file = get_nw_session_pcap_file(url, port, username, password, nw_cafile, nw_event_session_ids,
                                                 req_common)
            temp_d, temp_f = create_tmp_file(pcap_file)
            log.debug("pcap_file: {}".format(pcap_file))

            resilient_client = self.rest_client()
            resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                             temp_f, filename="pcap file for session IDs: {}.pcap".format(
                                             nw_event_session_ids))

            results = rp.done(True, {})
            yield StatusMessage("Done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
        finally:
            if temp_d:
                remove_dir(temp_d)


def get_nw_session_pcap_file(url, port, user, pw, cafile, event_session_id, req_common):
    headers = get_headers(user, pw)
    request_url = "{}:{}/sdk/packets?sessions={}&render=pcap".format(url, port, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers, resp_type='bytes')
