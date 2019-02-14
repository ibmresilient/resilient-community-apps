# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
import base64
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon
from fn_rsa_netwitness.util.helper import remove_dir, create_tmp_file

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
        else:
            self.options["cafile"] = True

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})

    @function("netwitness_retrieve_session_data")
    def _netwitness_retrieve_session_data(self, event, *args, **kwargs):
        """Function: """
#        temp_d = None
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            nw_event_session_ids = kwargs.get("nw_event_session_ids")  # text
            nw_data_format = self.get_select_param(kwargs.get("nw_data_format"))  # select

            # Initialize resilient_lib objects (handles the select input)
            rp = ResultPayload("netwitness_retrieve_session_data", **{"nw_event_session_ids": nw_event_session_ids,
                                                                      "nw_data_format": nw_data_format})
            req_common = RequestsCommon(self.opts)

#            validate_fields(["nw_event_session_id"], **kwargs)

            log.info("nw_event_session_ids: %s", nw_event_session_ids)

            session_data = None
            if nw_data_format == "pcap":
                session_data = """d4c3 b2a1 0200 0400 0000 0000 0000 0000
0010 0000 0100 0000 fc6b 634f d0bf 0b00
4000 0000 4000 0000 000c 2918 b667 0016
479d f2c2 8100 0078 0800 4500 0028 01c5
4000 7f06 954c c0a8 1964 c0a8 ca09 0406
1f90 8beb 9d6b de51 df8b 5010 ffff 404b
0000 0000 0000 0000 fc6b 634f d0bf 0b00
4000 0000 4000 0000 000c 2918 b667 0016
479d f2c2 8100 0078 0800 4500 0028 01c6
4000 7f06 950f c0a8 1964 c0a8 ca45 0405
01bb e881 aa3d 6d79 7c9a 5010 ffff c846
0000 0000 0000 0000 fc6b 634f d0bf 0b00
4000 0000 4000 0000 000c 2918 b667 0016
479d f2c2 8100 0078 0800 4500 0028 01c7
4000 7f06 950e c0a8 1964 c0a8 ca45 0405
01bb e881 aa3d 6d79 8762 5010 ffff bd7e
0000 0000 0000 0000 fc6b 634f d0bf 0b00
4000 0000 4000 0000 000c 2993 571e 0016
479d f2c2 8100 0078 0800 4500 0028 01c8
4000 7f06 94f4 c0a8 1964 c0a8 ca5e 0407
01bb 588b b16d 40d4 58e3 5010 ffff a14e
0000 0000 0000 0000 fc6b 634f e0e6 0b00
9e05 0000 9e05 0000 0016 479d f2c2 000c
2918 b667 8100 0078 0800 4500 058c ba2c
4000 4006 1645 c0a8 ca45 c0a8 1964 01bb
0405 6d7a 0e26 e881 aa3d 5010 3908 a763
0000 0a00 0000 8806 4683 f80a 7404 85ff
75e4 6af6 c606 00ff 1550 8007 1050 ff15
7880 0710 8bc3 5f8d 5001 5e8a 0840 84c9
75f9 2bc2 c3cc 6800 8005 106a 16e8 74ea
0000 6800 8005 106a 08a3 f021 0b10 e863
ea00 0068 0080 0510 6a04 a3b8 210b 10e8
52ea 0000 6800 8005 106a 02a3 a821 0b10
e841 ea00 0068 0080 0510 6a0b a3a0 210b
10e8 30ea 0000 6800 8005 106a 0fa3 c421"""
                # session_data = get_nw_session_logs_file(self.options.get("nw_url"), str(self.options.get("nw_port")),
                #                                         self.options.get("nw_user"), self.options.get("nw_password"),
                #                                         self.options.get("cafile"), nw_event_session_ids, req_common)
            elif nw_data_format == "logs_json":
                session_data = get_nw_session_logs_json(self.options.get("nw_url"), str(self.options.get("nw_port")),
                                                        self.options.get("nw_user"), self.options.get("nw_password"),
                                                        self.options.get("cafile"), nw_event_session_ids, req_common)
#            try:
#                pcap_file = get_nw_session_logs_file(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
#                                                     self.options.get("nw_user"), self.options.get("nw_password"),
#                                                     self.options.get("cafile"), nw_event_session_ids, req_common)

#                temp_d, temp_f = create_tmp_file(pcap_file)

#                resilient_client = self.rest_client()
#                resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
#                                                 temp_f, filename="pcap file for session IDs: {}".format(nw_event_session_ids))
#                yield StatusMessage("pcap file added to incident {} as Attachment".format(str(incident_id)))
#            except Exception:
#                log.info("Failed gathering or posting the attachment to the incident. Here just to not break the whole function")

#            json_response = get_nw_session_logs_json(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
#                                                     self.options.get("nw_user"), self.options.get("nw_password"),
#                                                     self.options.get("cafile"), nw_event_session_ids, req_common)

            log.debug(session_data)
            results = rp.done(True, session_data)
            yield StatusMessage("Done...")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
#        finally:
#            if temp_d:
#                remove_dir(temp_d)


def get_nw_session_logs_json(url, port, user, pw, cafile, event_session_id, req_common):
    login_string = "{}:{}".format(user, pw)
    base64_login = base64.b64encode(str.encode(login_string))

    headers = {
        "Authorization": "Basic {}".format(base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request_url = "{}:{}/sdk/packets?sessions={}&render=application/json".format(url, port, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)


def get_nw_session_logs_file(url, port, user, pw, cafile, event_session_id, req_common):
    login_string = "{}:{}".format(user, pw)
    base64_login = base64.b64encode(str.encode(login_string))

    headers = {
        "Authorization": "Basic {}".format(base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request_url = "{}:{}/sdk/packets?sessions={}".format(url, port, event_session_id)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers, resp_type='bytes')
