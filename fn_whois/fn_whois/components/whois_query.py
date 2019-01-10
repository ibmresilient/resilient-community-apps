# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

import whois
import datetime
import socks
import socket

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse


class FunctionPayload:
    """Class that contains the payload sent back to UI and available in the post-processing script"""

    def __init__(self, inputs):
        self.success = True
        self.inputs = {}
        self.domain_details = {}
        self.domain_details_keys = [],
        self.domain_details_values = []



        for input in inputs:
            self.inputs[input] = inputs[input]

    def as_dict(self):
        """Return this class as a Dictionary"""
        return self.__dict__

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'whois_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_whois", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_whois", {})

    @function("whois_query")
    def _whois_query_function(self, event, *args, **kwargs):
        """Function: Used to send a query directly to a WHOIS server to gather information about an IP Or URL taken as an input."""

        # Inner Function used to get config:

        def get_config_option(option_name, optional=False):
            """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
            option = self.options.get(option_name)

            if not option and optional is False:
                err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
                    option_name)
                raise ValueError(err)
            else:
                return option
        try:
            # Get the function parameters:
            whois_query = kwargs.get("whois_query")  # text
            log = logging.getLogger(__name__)

            log.info("whois_query: %s", whois_query)
            # Initialise the payload
            payload = FunctionPayload({
                "whois_query": whois_query
            })

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")

            # Check proxy settings
            if get_config_option("whois_https_proxy", True):
                yield StatusMessage("Config option found for proxies. Attempting to setup with proxy.")
                uri = urlparse.urlparse(get_config_option("whois_https_proxy", True))
                socks.set_default_proxy(socks.PROXY_TYPE_HTTP, uri.hostname, uri.port)
                socket.socket = socks.socksocket

            domain = None
            try:
                domain = whois.whois(whois_query)
            except Exception as e:
                yield StatusMessage("Encountered exception when sending query. Reason {0}".format(str(e)))
                payload.success = False

            domain_details = None
            if not isinstance(domain, type(None)):
                domain_details = domain
                payload.success = True

                yield StatusMessage("Gathered domain details, now normalising dates.")
                try:
                    for key,value in zip(domain_details.keys(), domain_details.values()):
                        # If value is a datetime, convert to a datestring
                        if isinstance(value,datetime.datetime):

                            domain_details[key] = value.strftime('%m/%d/%Y')
                        # Possible also to encounter a list of datetimes for updated_date
                        if isinstance(value, list) \
                           and any(isinstance(x, datetime.datetime) for x in value):
                            # Do a set comprehension to parse datetimes and remove duplicates then return update as list
                            domain_details[key] = list(set(date.strftime('%m/%d/%Y')
                                                           for date in value
                                                           if isinstance(date, datetime.datetime)))

                    # Ensure there aren't duplicate domain names
                    if domain_details.get("domain_name", None):
                        domain_details["domain_name"] = list(set(element.lower() for element in domain_details["domain_name"]))

                    # Last check if name_servers are provided
                    if isinstance(domain_details.get("name_servers",None),list):
                        # Servers are duplicated with /r char, remove it then convert it from set to list
                        domain_details["name_servers"] = list({
                            element.lower()
                            for element in domain_details.get("name_servers",None)
                           })
                except Exception as e:
                    yield StatusMessage("Encountered exception while attempting to parse the results")
                finally:
                    # Put our results in the payload
                    payload.domain_details = domain_details
                    payload.domain_details_keys = list(domain_details.keys())
                    payload.domain_details_values = list(domain_details.values())

                yield StatusMessage("Returning results")
            # Produce a FunctionResult with the results
            yield FunctionResult(payload.as_dict())
            log.info("Complete")
        except Exception:
            yield FunctionError()

