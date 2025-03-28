# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, line-too-long
"""Function implementation"""

import logging
import socket

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import RequestsCommon, ResultPayload, validate_fields
from fn_whois_rdap.util import helper

SECTION_HDR = "fn_whois_rdap"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'rdap_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.options = opts.get(SECTION_HDR, {})

    @function("rdap_query")
    def _rdap_query_function(self, event, *args, **kwargs):
        """Function: Using ipwhois library to make general queries in RDAP format"""
        try:
            rdap_depth = kwargs.get("rdap_depth")  # number
            rdap_query = kwargs.get("rdap_query")

            log = logging.getLogger(__name__)
            log.info("rdap_depth: %s", rdap_depth)
            log.info("rdap_query: %s", rdap_query)

            validate_fields(["rdap_depth", "rdap_query"], kwargs)
            payload_object = ResultPayload("fn_whois_rdap", **kwargs)

            rdap_query = u"{}".format(rdap_query)

            input_is_ip, registered_domain = helper.check_input_ip(rdap_query)

            real_domain = helper.check_registered_domain(registered_domain)

            # get proxies
            proxies = RequestsCommon(self.opts, self.options).get_proxies()

            if not input_is_ip and real_domain:
                ip_from_domain = socket.getaddrinfo(registered_domain, None)[-1][4][0]
                rdap_response = helper.get_rdap_registry_info(u"{}".format(ip_from_domain), rdap_depth, proxies=proxies)
                results = helper.check_response(rdap_response, payload_object)
            else:
                try:
                    rdap_response = helper.get_rdap_registry_info(rdap_query, rdap_depth, proxies=proxies)
                    results = helper.check_response(rdap_response, payload_object)
                except:
                    yield FunctionError("This may not a be valid IP, URL or domain, no registry information is currently accessible")

            timenow = helper.time_str()

            yield StatusMessage(u"RDAP Query complete, Threat Intelligence added to Artifact '{}' at {}".format(rdap_query, timenow))
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)
