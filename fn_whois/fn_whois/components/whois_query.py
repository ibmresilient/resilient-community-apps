# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import datetime
import logging
from fn_whois.lib.whois_common import get_config_option, whois_query
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


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

        try:
            # Get the function parameters:
            whois_value = kwargs.get("whois_query")  # text
            log = logging.getLogger(__name__)

            log.info("whois_query: %s", whois_value)
            # Initialise the payload
            payload = FunctionPayload({
                "whois_query": whois_value
            })

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            yield StatusMessage("starting...")
            domain = None
            try:
                domain = whois_query(whois_value, get_config_option(self.options, "whois_https_proxy", True))
                log.debug(domain)
            except Exception as e:
                yield StatusMessage("Encountered exception when sending query. Reason {0}".format(str(e)))
                payload.success = False

            domain_details = None
            if not isinstance(domain, type(None)):
                domain_details = domain
                payload.success = True

                yield StatusMessage("Gathered domain details, now normalising dates.")
                try:
                    for key,value in domain_details.items():
                        # If value is a datetime, convert to a datestring
                        if isinstance(value, datetime.datetime):
                            domain_details[key] = value.strftime('%m/%d/%Y')

                        # Possible also to encounter a list of datetimes for updated_date
                        if isinstance(value, list) \
                           and any(isinstance(x, datetime.datetime) for x in value):
                            # Do a set comprehension to parse datetimes and remove duplicates then return update as list
                            domain_details[key] = list(set(date.strftime('%m/%d/%Y')
                                                           for date in value
                                                           if isinstance(date, datetime.datetime)))

                    # Ensure there aren't duplicate domain names
                    if isinstance(domain_details.get("domain_name", None), list):
                        domain_details["domain_name"] = list(set(element.lower() for element in domain_details["domain_name"]))

                    # Last check if name_servers are provided
                    if isinstance(domain_details.get("name_servers", None), list):
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
