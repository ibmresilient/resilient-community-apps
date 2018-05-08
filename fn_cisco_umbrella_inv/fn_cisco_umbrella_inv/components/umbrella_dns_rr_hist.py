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
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import init_env, validate_opts, validate_params, process_params, is_none


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        resource , dns_type

    An example of a set of query parameter might look like the following:

            umbinv_resource = "1.2.3.4" or resource = "example.com"
            umbinv_dns_type = "A"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'resource_name': 'cosmos.furnipict.com',
         'query_execution_time': '2018-05-02 16:03:15',
         "dns_rr_history": {  "rrs": [  {
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
        validate_opts(self)

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
            umbinv_resource_type = self.get_select_param(kwargs.get("umbinv_resource_type"))  # select, values: "domain_name", "ip_address", "url"
            umbinv_dns_type = self.get_select_param(kwargs.get("umbinv_dns_type"))  # select, values: "A", "NS", "MX", "TXT", "CNAME"

            log = logging.getLogger(__name__)
            log.info("umbinv_resource: %s", umbinv_resource)
            log.info("umbinv_dns_type: %s", umbinv_dns_type)

            if is_none(umbinv_resource):
                raise ValueError("Required parameter 'umbinv_resource' not set")

            if is_none(umbinv_resource_type):
                raise ValueError("Required parameter 'umbinv_resource_type' not set")

            yield StatusMessage("Starting...")
            init_env(self)

            self._params = {"resource": umbinv_resource.strip(), "dns_type": umbinv_dns_type,
                            "resource_type": umbinv_resource_type}

            validate_params(self)
            process_params(self)

            if not hasattr(self, '_res'):
               raise ValueError("Parameter 'umbinv_resource' was not processed properly.")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token,base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.rr_history(self._res,query_type=umbinv_dns_type)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if ("rrs" in rtn and len(rtn["rrs"]) == 0) \
                    or ("rrs_tf" in rtn and len(rtn["rrs_tf"]) == 0):
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for resource '{}' with query type '{}'."
                                    .format(self._res,umbinv_dns_type))
                results = {}
            else:
                # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"dns_rr_history": json.loads(json.dumps(rtn)), "resource_name": self._res,
                           "query_execution_time": query_execution_time}
            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            logging.exception("Exception in Resilient Function.")
            yield FunctionError()