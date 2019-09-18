# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import socket
from ipwhois import IPWhois
import tldextract
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from resilient_lib.components.resilient_common import validate_fields

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'whois_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_whois_rdap", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_whois_rdap", {})

    @function("whois_query")
    def _whois_query_function(self, event, *args, **kwargs):
        """Function: Using ipwhois library to make general queries in whois format"""
        try:
            ip_from_domain = None
            internet_protocol_address_object = None
            whois_query = kwargs.get("whois_query")
            log = logging.getLogger(__name__)
            log.info("whois_query: %s", whois_query)
            payload_object = ResultPayload("fn_whois_rdap", **kwargs)
            validate_fields("whois_query", kwargs)
            try: 
                ext = tldextract.extract(whois_query)
                if ext.registered_domain:
                    ip_from_domain = socket.gethostbyname(ext.registered_domain)                    
                    internet_protocol_address_object = IPWhois(ip_from_domain)
                    whois_response = internet_protocol_address_object.lookup_whois()
                    if internet_protocol_address_object.dns_zone:
                        whois_response["dns_zone"] = internet_protocol_address_object.dns_zone
                results = payload_object.done(True, whois_response)
            except Exception as whois_error:
                yield StatusMessage("That was an IP address, searching now")
                internet_protocol_address_object = IPWhois(whois_query)
                whois_response = internet_protocol_address_object.lookup_whois()
                if internet_protocol_address_object.dns_zone:
                    whois_response["dns_zone"] = internet_protocol_address_object.dns_zone
                results = payload_object.done(True, whois_response)
            log.info("WHOIS Query complete, Threat Intelligence added to Artifact description")
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)