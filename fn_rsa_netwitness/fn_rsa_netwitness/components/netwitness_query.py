# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# Copyright © IBM Corporation 2010, 2019
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon
from fn_rsa_netwitness.util.helper import get_headers


log = logging.getLogger(__name__)


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
        try:
            yield StatusMessage("Starting...")
            # Get the function parameters:
            nw_query = self.get_textarea_param(kwargs.get("nw_query"))  # textarea
            nw_results_size = str(kwargs.get("nw_results_size", ''))  # number

            # Initialize resilient_lib objects
            rp = ResultPayload("fn_rsa_netwitness", **{"nw_query": nw_query, "nw_results_size": nw_results_size})
            req_common = RequestsCommon(self.opts)

            log.info("nw_query: %s", nw_query)
            log.info("nw_results_size: %s", nw_results_size)

            # Query Netwitness
            nw_query_results = query_netwitness(self.options.get("nw_packet_server_url"),
                                                self.options.get("nw_packet_server_user"),
                                                self.options.get("nw_packet_server_password"),
                                                self.options.get("nw_packet_server_verify"),
                                                query=nw_query, req_common=req_common,
                                                size=nw_results_size)

            log.debug(nw_query_results)

            if nw_query_results:
                StatusMessage("Query results found")
            else:
                StatusMessage("No query results found")
            yield StatusMessage("Complete...")
            results = rp.done(True, nw_query_results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)


def query_netwitness(url, user, pw, cafile, query, req_common, size=""):
    headers = get_headers(user, pw)
    if size:
        size = "&size={}".format(size)
    request_url = "{}/sdk?msg=query&query={}&force-content-type=application/json{}".format(url, query, size)

    return req_common.execute_call("GET", request_url, verify_flag=cafile, headers=headers)
