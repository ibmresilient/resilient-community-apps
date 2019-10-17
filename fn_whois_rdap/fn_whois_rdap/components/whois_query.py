# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import socket

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_whois_rdap.util import helper

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'whois_query"""

    @function("whois_query")
    def _whois_query_function(self, event, *args, **kwargs):
        """Function: Using ipwhois library to make general queries in WHOIS format"""
        try:
            ip_from_domain = helper.ip_from_domain

            whois_query = kwargs.get("whois_query")
            log = logging.getLogger(__name__)
            log.info("whois_query: %s", whois_query)

            validate_fields("whois_query", kwargs)
            payload_object = ResultPayload("fn_whois_rdap", **kwargs)

            whois_query = u"{}".format(whois_query)

            input_is_ip, registered_domain = helper.check_input_ip(whois_query)

            real_domain = helper.check_registered_domain(registered_domain)
            
            if not input_is_ip and real_domain:
                ip_from_domain = socket.getaddrinfo(registered_domain, None)[-1][4][0]
                whois_response = helper.get_whois_registry_info(u"{}".format(ip_from_domain))
                results = helper.check_response(whois_response, payload_object)
            else:
                try:
                    whois_response = helper.get_whois_registry_info(whois_query)
                    results = helper.check_response(whois_response, payload_object)
                except:
                    yield FunctionError("This may not a be valid IP, URL or domain, no registry information is currently accessible")
            
            timenow = helper.time_str()

            yield StatusMessage(u"WHOIS Query complete, Threat Intelligence added to Artifact '{}' at {}".format(whois_query, timenow))
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)
