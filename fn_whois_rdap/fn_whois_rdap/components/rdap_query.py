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
    """Component that implements Resilient function 'rdap_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_whois_rdap", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_whois_rdap", {})

    @function("rdap_query")
    def _rdap_query_function(self, event, *args, **kwargs):
        """Function: Using Ipwhois library to make general queries is RDAP format"""
        try:
            ip_from_domain = None
            internet_protocol_address_object = None
            rdap_depth = kwargs.get("rdap_depth")  # number
            rdap_query = kwargs.get("rdap_query")
            log = logging.getLogger(__name__)
            log.info("rdap_depth: %s", rdap_depth)
            log.info("rdap_query: %s", rdap_query)
            payload_object = ResultPayload("fn_whois_rdap", **kwargs)
            validate_fields(["rdap_depth", "rdap_query"], kwargs)
            try: 
                ext = tldextract.extract(rdap_query)
                if ext.registered_domain:
                    ip_from_domain = socket.gethostbyname(ext.registered_domain)                    
                    internet_protocol_address_object = IPWhois(ip_from_domain)
                    rdap_response = internet_protocol_address_object.lookup_rdap(depth=rdap_depth)
                    if internet_protocol_address_object.dns_zone:
                        rdap_response["dns_zone"] = internet_protocol_address_object.dns_zone
                results = payload_object.done(True, rdap_response)
            except Exception as rdap_error:
                yield StatusMessage("That was an IP address, searching now")
                internet_protocol_address_object = IPWhois(rdap_query)
                rdap_response = internet_protocol_address_object.lookup_rdap(depth=rdap_depth)
                if internet_protocol_address_object.dns_zone:
                    rdap_response["dns_zone"] = internet_protocol_address_object.dns_zone
                results = payload_object.done(True, rdap_response)
            log.info("RDAP Query complete, Threat Intelligence added to Artifact description")
            #import pprint
            #pprint.pprint(results)
            #results = None
            yield FunctionResult(results)
        except Exception as error:
            yield FunctionError(error)
