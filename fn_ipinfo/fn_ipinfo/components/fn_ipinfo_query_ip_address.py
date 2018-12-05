# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
import ipinfo
import ipaddress
import sys

class FunctionPayload:
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.inputs = {}
        self.query_result = None

        for input in inputs:
            self.inputs[input] = inputs[input]

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

        """Helper Functions """

        def is_valid_ipv4_addr(ip):
            """ A custom Jinja filter function which determines if input is an IPV4 Address"""
            try:
                return isinstance(ipaddress.ip_address(ip), ipaddress.IPv4Address)
            except Exception as e:
                return False

        def is_valid_ipv6_addr(ip):
            """ A custom Jinja filter function which determines if input is an IPV6 Address"""
            try:
                return isinstance(ipaddress.ip_address(ip), ipaddress.IPv6Address)
            except Exception as e:
                return False

        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if not option and optional is False:
                err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function properly".format(
                    option_name)
                raise ValueError(err)
            else:
                return option

        """ Function Code """
        try:
            # Get the function parameters:
            ipinfo_query_ip = kwargs.get("ipinfo_query_ip")  # text

            log = logging.getLogger(__name__)
            log.info("ipinfo_query_ip: %s", ipinfo_query_ip)

            if not ipinfo_query_ip:
                raise ValueError("An IP to query is mandatory, check your provided input.")

            """Validate the input is a IP Address
            
            On Py2 the ipaddress package expects unicode 
            This is a problem as when we do a input.encode('utf-8')
            on python the type resolves as str and not unicode 
            """
            if not is_valid_ipv4_addr(ipinfo_query_ip
                                      if sys.version_info > (3, 0)
                                      else unicode(ipinfo_query_ip)) \
                    and not is_valid_ipv6_addr(ipinfo_query_ip
                                               if sys.version_info > (3, 0)
                                            else unicode(ipinfo_query_ip)):
                yield StatusMessage("Could not validate the IP as a IPV4 or IPV6 IP Address.")
                raise ValueError("Could not validate the IP as a IPV4 or IPV6 IP Address.")
            else:
                yield StatusMessage("Input IP has passed validation, querying for information")

            # Prepare the function payload
            payload = FunctionPayload({
                "ipinfo_query_ip": ipinfo_query_ip
            })

            access_token = get_config_option(option_name='ipinfo_access_token')
            # Setup the IpInfo API Class
            handler = ipinfo.getHandler(access_token)

            try:
                # Submit query
                details = handler.getDetails(ipinfo_query_ip)

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

            except Exception as e:
                payload.success = False
                if '404 Client Error' in e.args[0]:
                    yield StatusMessage(
                        "Encountered Not Found Error. Provided Message {0}".format(e.args[0]))
                else:
                    yield StatusMessage(
                        "Encountered error when querying Ip Info. Provided Message {0}".format(e.args[0]))

            # Produce a FunctionResult with the results
            yield FunctionResult(payload.as_dict())
        except Exception:
            yield FunctionError()