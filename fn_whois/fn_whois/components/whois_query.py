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

            url_params = urlparse.urlparse(whois_query)
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
                if u"Unknown TLD" in e.args[0]:
                    # Return a message telling the user which args are supported.
                    yield StatusMessage(
                        "Unsupported domain provided. The supported domains are {0}".format(e.args[0][32:-1]))
                payload.success = False

            domain_details = None
            if not isinstance(domain, type(None)):
                # Get a dict representation of the details
                domain_details = domain.__dict__
                payload.success = True

                yield StatusMessage("Gathered domain details, now normalising dates.")
                try:
                    for key,value in domain_details.items():
                        # If value is a datetime, convert to a datestring
                        if isinstance(value,datetime.datetime):
                            domain_details[key] = value.strftime('%m/%d/%Y')
                    # Last check if name_servers are provided
                    if isinstance(domain_details.get("name_servers",None),set):
                        # Servers are duplicated with /r char, remove it then convert it from set to list
                        domain_details["name_servers"] = list({
                            element.replace('\r', '')
                            for element in domain_details.get("name_servers",None)
                           })
                except Exception as e:
                    yield StatusMessage("Encountered exception while attempting to parse the results")


                finally:
                    payload.domain_details = domain_details
                    payload.domain_details_keys = list(domain_details.keys())
                    payload.domain_details_values = list(domain_details.values())

                yield StatusMessage("Returning results")


            # Produce a FunctionResult with the results
            yield FunctionResult(payload.as_dict())
            log.info("Complete")
        except Exception:
            yield FunctionError()