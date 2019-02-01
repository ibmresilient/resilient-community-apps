# Copyright © IBM Corporation 2010, 2019
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import base64
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon


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
        else:
            self.options["cafile"] = True


    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})

    @function("netwitness_query_event_session")
    def _netwitness_query_event_session_function(self, event, *args, **kwargs):
        """Function: """
        try:
            yield StatusMessage("Starting...")
            # Initialize resilient_lib objects
            rp = ResultPayload("netwitness_query_event_session", **kwargs)
            req_common = RequestsCommon(self.opts)

            # Get the function parameters:
            nw_event_session_id = str(kwargs.get("nw_event_session_id"))  # number
            incident_id = str(kwargs.get("incident_id"))

#            validate_fields(["nw_event_session_id"], **kwargs)

            log = logging.getLogger(__name__)
            log.info("nw_event_session_id: %s", nw_event_session_id)
            log.info("incident_id: %s", incident_id)

            try:
                pcap_file = get_nw_session_logs_file(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
                                                     self.options.get("nw_user"), self.options.get("nw_password"),
                                                     self.options.get("cafile"), nw_event_session_id, req_common)

                resilient_client = self.rest_client()
                resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                                 pcap_file, filename="pcap file for session IDs: {}".format(nw_event_session_id))
                yield StatusMessage("pcap file added to incident {} as Attachment".format(str(incident_id)))
            except Exception:
                log.info("Failed gathering or posting the attachment to the incident. Here just to not break the whole function")

            json_response = get_nw_session_logs_json(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
                                                     self.options.get("nw_user"), self.options.get("nw_password"),
                                                     self.options.get("cafile"), nw_event_session_id, req_common)

            log.info(json.dumps(json_response), sort_keys=True, indent=4, separators=(',', ': '))

            results = rp.done(True, json_response)

            yield StatusMessage("Done...")
            results = json_response

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()


def get_nw_session_logs_json(url, port, user, pw, cafile, event_session_id, req_common):
    login_string = "{}:{}".format(user, pw)
    base64_login = base64.b64encode(str.encode(login_string))

    headers = {
        "Authorization": "Basic {}".format(base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request_url = "{}:{}/sdk/packets?sessions={}&render=application/json".format(url, port, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers, resp_type='bytes')


def get_nw_session_logs_file(url, port, user, pw, cafile, event_session_id, req_common):
    login_string = "{}:{}".format(user, pw)
    base64_login = base64.b64encode(str.encode(login_string))

    headers = {
        "Authorization": "Basic {}".format(base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request_url = "{}:{}/sdk/packets?sessions={}".format(url, port, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)
