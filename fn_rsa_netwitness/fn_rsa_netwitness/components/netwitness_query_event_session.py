# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
import base64
import json
import tempfile
import shutil
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon


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

    @function("netwitness_query_event_session")
    def _netwitness_query_event_session_function(self, event, *args, **kwargs):
        """Function: """
        temp_d = None
        try:
            yield StatusMessage("Starting...")
            # Initialize resilient_lib objects
            rp = ResultPayload("netwitness_query_event_session", **kwargs)
            req_common = RequestsCommon(self.opts)

            # Get the function parameters:
            nw_event_session_id = str(kwargs.get("nw_event_session_id"))  # number
            incident_id = str(kwargs.get("incident_id"))

#            validate_fields(["nw_event_session_id"], **kwargs)

            log.info("nw_event_session_id: %s", nw_event_session_id)
            log.info("incident_id: %s", incident_id)

            try:
                pcap_file = get_nw_session_logs_file(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
                                                     self.options.get("nw_user"), self.options.get("nw_password"),
                                                     self.options.get("cafile"), nw_event_session_id, req_common)

                temp_d, temp_f = create_tmp_file(pcap_file)

                resilient_client = self.rest_client()
                resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                                 temp_f, filename="pcap file for session IDs: {}".format(nw_event_session_id))
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
        finally:
            if temp_d:
                remove_dir(temp_d)


def create_tmp_file(contents):
    temp_d = tempfile.mkdtemp("tmp")
    temp_f = tempfile.mkstemp(dir=temp_d)
    report_file = temp_f[1]

    with open(report_file, 'wb') as f:
        f.write(contents)
#        log.info("Saved ATD report")

    return temp_d, report_file


def remove_dir(dir):
    shutil.rmtree(dir)
#    log.debug("Tmp directory removed")


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
