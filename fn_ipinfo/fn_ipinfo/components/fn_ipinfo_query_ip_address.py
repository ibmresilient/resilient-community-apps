# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
import ipinfo
from fn_ipinfo.util.helper import IpInfoHelper
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError



class FunctionPayload:
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.inputs = inputs
        self.query_result = None



    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_ipinfo_query_ip_address"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_ipinfo", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_ipinfo", {})

    @function("fn_ipinfo_query_ip_address")
    def _fn_ipinfo_query_ip_address_function(self, event, *args, **kwargs):
        """Function: Submits a query to IP Info for enrichment information on a given IP address.
Takes in a String input representing an IP Address."""



        """ Function Code """
        try:
            # Get the function parameters:
            ipinfo_query_ip = kwargs.get("ipinfo_query_ip")  # text

            log = logging.getLogger(__name__)
            log.info("ipinfo_query_ip: %s", ipinfo_query_ip)

            if not ipinfo_query_ip:
                raise ValueError("An IP to query is mandatory, check your provided input.")

            helper = IpInfoHelper()
            # Prepare the function payload
            payload = FunctionPayload({
                "ipinfo_query_ip": ipinfo_query_ip
            })
            """Validate the input is a IP Address
            
            On Py2 the ipaddress package expects unicode 
            This is a problem as when we do a input.encode('utf-8')
            on python the type resolves as str and not unicode 
            """
            if not helper.is_valid_ipv4_addr(helper.get_ipinfo_qry_ip(ip=ipinfo_query_ip)) \
                    and not helper.is_valid_ipv6_addr(helper.get_ipinfo_qry_ip(ip=ipinfo_query_ip)):

                    payload.success = False
                    raise ValueError("Could not validate the IP as a IPV4 or IPV6 IP Address.")
            else:
                yield StatusMessage("Input IP has passed validation, querying for information")

            access_token = helper.get_config_option(option_name='ipinfo_access_token', options=self.options)
            # Setup the IpInfo API Class
            ipinfo_handler = ipinfo.getHandler(access_token)

            try:
                # Submit query
                details = ipinfo_handler.getDetails(ipinfo_query_ip)

                # Take all the results into our payload for enrichment
                payload.query_result = details.all
                # If key is not present in dictionary, then del can throw KeyError, need to catch this
                try:
                    """Part of the payload is a field called 'ip_address' of type IPV4Address
                    This classtype isin't JSON compat and the string representation
                    of 'ip_address' is already present in attribute 'ip'
                    In this case, remove 'ip_address' from payload'"""
                    del payload.query_result["ip_address"]
                except KeyError:
                    log.debug("Encounted issue trying to remove ip_address attribute")
                # Query result is a dict, if it is falsey (None, empty dict) set success to false
                if not payload.query_result:
                    payload.success = False

            except Exception as e:
                payload.success = False
                if '404 Client Error' in e.args[0]:
                    yield StatusMessage(
                        "Encountered Not Found Error. Provided Message {0}".format(e.args[0]))
                else:
                    yield StatusMessage(
                        "Encountered error when querying Ip Info. Provided Message {0}".format(e.args[0]))
            log.info("Complete")
            # Produce a FunctionResult with the results
            yield FunctionResult(payload.as_dict())
        except Exception:
            yield FunctionError()