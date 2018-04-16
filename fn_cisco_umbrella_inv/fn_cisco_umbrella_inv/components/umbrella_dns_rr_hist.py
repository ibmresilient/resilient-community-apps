# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - DNS RR History for an IP Address or domain
against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.

import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        resource , dns_type

    An example of a set of query parameter might look like the following:

            resource = "1.2.3.4" or resource = "example.com"
            dns_type = "A"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {"dns_rr_history": {  "rrs": [  {
                                  "rr": "www.example.com.",
                                  "ttl": 86400,
                                  "class": "IN",
                                  "type": "A",
                                  "name": "93.184.216.119"
                                }
                                ...
                                ...
                              ],
                              "features": {
                                "rr_count": 19,
                                "ld2_count": 10,
                                "ld3_count": 14,
                                "ld2_1_count": 7,
                                "ld2_2_count": 11,
                                "div_ld2": 0.5263157894736842,
                                "div_ld3": 0.7368421052631579,
                                "div_ld2_1": 0.3684210526315789,
                                "div_ld2_2": 0.5789473684210527
                              }
                        }
        }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_umbrella_inv", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_umbrella_inv", {})

    @function("umbrella_dns_rr_hist")
    def _umbrella_dns_rr_hist_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for DNS RR History for a IP, Type and Domain Name"""
        try:
            # Get the function parameters:
            umbinv_resource = kwargs.get("umbinv_resource")  # text
            umbinv_dns_type = self.get_select_param(kwargs.get("umbinv_dns_type"))  # select, values: "A", "NS", "MX", "TXT", "CNAME"

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)
            log.info("umbinv_dns_type: %s", umbinv_dns_type)

            if umbinv_resource is None:
                raise ValueError("Required parameter 'umbinv_resource' not set")

            self._params = {"resource": umbinv_resource, "dns_type": umbinv_dns_type}

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_res'):
               raise ValueError("Parameter 'umbinv_resource' was not processed properly.")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.rr_history(self._res,query_type=umbinv_dns_type)
            # Add in ip address it ran against to result.
            results = {"dns_rr_history": json.loads(json.dumps(rtn)), "resource_name": self._res}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()