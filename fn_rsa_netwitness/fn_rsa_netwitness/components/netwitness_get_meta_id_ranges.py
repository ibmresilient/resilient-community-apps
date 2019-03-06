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
    """Component that implements Resilient function 'netwitness_get_meta_id_ranges"""

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

    @function("netwitness_get_meta_id_ranges")
    def _netwitness_get_meta_id_ranges(self, event, *args, **kwargs):
        """Function: Returns back the meta id ranges for a single session or consecutive sessions"""
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            nw_event_session_ids = self.get_textarea_param(kwargs.get("nw_event_session_ids"))  # text
            nw_results_size = str(kwargs.get("nw_results_size"))  # number

            # Initialize resilient_lib objects
            rp = ResultPayload("netwitness_get_meta_id_ranges", **kwargs)
            req_common = RequestsCommon(self.opts)

            log.info("nw_event_session_ids: %s", nw_event_session_ids)
            log.info("nw_results_size: %s", nw_results_size)

            # Query Netwitness
            nw_query_metadata = get_meta_id_ranges(self.options.get("nw_url"), self.options.get("nw_port"),
                                                   self.options.get("nw_user"), self.options.get("nw_password"),
                                                   self.options.get("cafile"), nw_event_session_ids, req_common,
                                                   size=nw_results_size)

            log.debug(nw_query_metadata)

            if nw_query_metadata:
                StatusMessage("Meta ID ranges found")
            else:
                StatusMessage("No meta ID ranges found")
            yield StatusMessage("Complete...")
            results = rp.done(True, nw_query_metadata)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


def get_meta_id_ranges(url, port, user, pw, cafile, event_session_id, req_common, size=""):
    headers = get_headers(user, pw)
    if size:
        size = "&size={}".format(size)
    request_url = "{}:{}/sdk/packets?sessions={}&render=application/json{}".format(url, port, event_session_id, size)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)
