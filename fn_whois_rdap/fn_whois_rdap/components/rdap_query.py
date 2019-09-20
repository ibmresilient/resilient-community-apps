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
    """Component that implements Resilient function 'rdap_query"""

    @function("rdap_query")
    def _rdap_query_function(self, event, *args, **kwargs):
        """Function: Using ipwhois library to make general queries in RDAP format"""
        try:
            ip_from_domain = helper.ip_from_domain

            rdap_depth = kwargs.get("rdap_depth")  # number
            rdap_query = kwargs.get("rdap_query")

            log = logging.getLogger(__name__)
            log.info("rdap_depth: %s", rdap_depth)
            log.info("rdap_query: %s", rdap_query)

            validate_fields(["rdap_depth", "rdap_query"], kwargs)
            payload_object = ResultPayload("fn_whois_rdap", **kwargs)

            input_is_ip, registered_domain = helper.check_input_ip(rdap_query)

            if not input_is_ip:
                obj = socket.getaddrinfo(registered_domain, None)
                ip_from_domain = [x[4] for x in obj].pop()[0]
                rdap_response = helper.get_rdap_registry_info(ip_from_domain, rdap_depth)
                results = payload_object.done(True, rdap_response)
            else:
                rdap_response = helper.get_rdap_registry_info(rdap_query, rdap_depth)
                results = payload_object.done(True, rdap_response)

            log.info("RDAP Query complete, Threat Intelligence added to Artifact description")
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)
