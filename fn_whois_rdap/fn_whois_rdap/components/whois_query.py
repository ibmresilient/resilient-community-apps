# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import socket

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from resilient_lib.components.resilient_common import validate_fields
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

            input_is_ip, registered_domain = helper.check_input_ip(whois_query)

            if not input_is_ip:
                ip_from_domain = socket.gethostbyname(registered_domain)
                whois_response = helper.get_whois_registry_info(ip_from_domain)
                results = payload_object.done(True, whois_response)
            else:
                whois_response = helper.get_whois_registry_info(whois_query)
                results = payload_object.done(True, whois_response)

            log.info("WHOIS Query complete, Threat Intelligence added to Artifact description")
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)
