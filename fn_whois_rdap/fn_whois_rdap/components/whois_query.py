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
    """Component that implements Resilient function 'whois_query"""

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

    @function("whois_rdap_query")
    def _whois_query_function(self, event, *args, **kwargs):
        """Function: Using ipwhois library to make general queries in WHOIS format"""
        try:
            whois_query = kwargs.get("whois_query")
            log = logging.getLogger(__name__)
            log.info("whois_query: %s", whois_query)

            validate_fields("whois_query", kwargs)
            payload_object = ResultPayload("fn_whois_rdap", **kwargs)

            whois_query = u"{}".format(whois_query)

            input_is_ip, registered_domain = helper.check_input_ip(whois_query)

            real_domain = helper.check_registered_domain(registered_domain)

            # get proxies
            proxies = RequestsCommon(self.opts, self.options).get_proxies()

            if not input_is_ip and real_domain:
                ip_from_domain = socket.getaddrinfo(registered_domain, None)[-1][4][0]
                whois_response = helper.get_whois_registry_info(u"{}".format(ip_from_domain), proxies=proxies)
                results = helper.check_response(whois_response, payload_object)
            else:
                try:
                    whois_response = helper.get_whois_registry_info(whois_query, proxies=proxies)
                    results = helper.check_response(whois_response, payload_object)
                except:
                    yield FunctionError("This may not a be valid IP, URL or domain, no registry information is currently accessible")

            timenow = helper.time_str()

            yield StatusMessage(u"WHOIS Query complete, Threat Intelligence added to Artifact '{}' at {}".format(whois_query, timenow))
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)
