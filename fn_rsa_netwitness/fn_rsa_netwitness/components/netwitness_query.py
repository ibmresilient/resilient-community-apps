# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
import base64
import tempfile
import shutil
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload, RequestsCommon


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'netwitness_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_rsa_netwitness", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_rsa_netwitness", {})

    @function("netwitness_query")
    def _netwitness_query_function(self, event, *args, **kwargs):
        """Function: Queries NetWitness and returns back a list of session IDs based on the provided query"""
        temp_d = None
        try:
            yield StatusMessage("starting...")
            # Initialize resilient_lib objects
            rp = ResultPayload("netwitness_query", **kwargs)
            req_common = RequestsCommon(self.opts)

            # Get the function parameters:
            incident_id = str(kwargs.get("incident_id"))  # number
            nw_query = kwargs.get("nw_query")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("nw_query: %s", nw_query)

            # Get Session IDs
            json_session_ids = query_netwitness(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
                                                self.options.get("nw_user"), self.options.get("nw_password"),
                                                self.options.get("cafile"), nw_query, req_common)
            log.info(json_session_ids)

            # Basing this off what I think, this might have to be updated
            session_id_list = []
            for session_id in json_session_ids["results"]["fields"]:
                session_id_list.append(str(session_id.get("group")))
            session_id_str = ", ".join(session_id_list)
            log.info(session_id_str)

            # Get pcap files from session ids
            pcap_file = get_nw_session_logs_file(self.options.get("nw_url"), str(int(self.options.get("nw_port")) + 100),
                                                 self.options.get("nw_user"), self.options.get("nw_password"),
                                                 self.options.get("cafile"), session_id_str, req_common)

            temp_d, temp_f = create_tmp_file(pcap_file)
            # Upload pcap file
            resilient_client = self.rest_client()
            resilient_client.post_attachment("/incidents/{}/attachments/".format(incident_id),
                                             pcap_file,
                                             filename="pcap file for session IDs: {}".format(session_id_list))
            yield StatusMessage("pcap file added to incident {} as Attachment".format(str(incident_id)))

            yield StatusMessage("done...")
            results = rp.done(True, {})
            results = {
                "list": session_id_str
            }

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


def query_netwitness(url, port, user, pw, cafile, query, req_common):
    login_string = "{}:{}".format(user, pw)
    base64_login = base64.b64encode(str.encode(login_string))

    headers = {
        "Authorization": "Basic {}".format(base64_login),
        "Content-Type": "application/x-www-form-urlencoded",
        "Cache-Control": "no-cache"
    }
    request_url = "{}:{}/sdk?msg=query&{}&render=application/json".format(url, port, query)

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
