# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from resilient_lib.components.resilient_common import validate_fields
from ipwhois import IPWhois
import socket

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
        """Function: Using ipwhois library to make general queries is RDAP format"""
        try:
            rdap_depth = kwargs.get("rdap_depth")  # number
            rdap_query = kwargs.get("rdap_query")
            log = logging.getLogger(__name__)
            log.info("rdap_depth: %s", rdap_depth)
            rp = ResultPayload("fn_whois_rdap", **kwargs)
            validate_fields(["rdap_depth","rdap_query"], kwargs)
            domain = " "
            IP = " "
            try:
                yield StatusMessage("Gathered Intelligence for {0} : with attached object depth of {1}".format(
                rdap_query, rdap_depth))
                IP = IPWhois(rdap_query)
                rdap_response = IP.lookup_rdap(depth=rdap_depth)
                if IP.dns_zone:
                    rdap_response["dns_zone"] = IP.dns_zone
                results = rp.done(True, IP.lookup_rdap(depth=rdap_depth))
            except Exception as er:
                log.warning("Error: {}".format(er))
                try:
                    log.info("Trying to convert URL or domain")
                    rdap_query = rdap_query.encode('utf-8')
                    rdap_query = rdap_query.replace("http://","").replace("https://","").replace("www.","")
                    if socket.gethostbyname(rdap_query):
                        domain = socket.gethostbyname(rdap_query)
                        obj = IPWhois(domain)
                        rdap_response = obj.lookup_rdap(depth=rdap_depth)
                        if obj.dns_zone:
                            rdap_response["dns_zone"] = obj.dns_zone
                        results = rp.done(True, rdap_response)
                except Exception as e:
                    yield FunctionError("The IP, URL or DNS you queried is not valid. Error: {}".format(e))
            yield StatusMessage("Query complete, Threat Intelligence added to artifact description")
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionError(err)