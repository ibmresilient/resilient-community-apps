# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Security Information for a Domain against a Cisco
Umbrella server """

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
        domain

    An example of a set of query parameter might look like the following:

            domain = "example.com"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.

        {"security_info": {   "found": true,
                              "dga_score": 38.301771886101335,
                              "perplexity": 0.4540313302593146,
                              "entropy": 2.5216406363433186,
                              "securerank2": -1.3135141095601992,
                              "pagerank": 0.0262532,
                              "asn_score": -29.75810625887133,
                              "prefix_score": -64.9070502788884,
                              "rip_score": -75.64720536038982,
                              "popularity": 25.335450495507196,
                              "fastflux": false,
                              "geodiversity": [
                                [
                                  "UA",
                                  0.24074075
                                ],
                                [
                                  "IN",
                                  0.018518519
                                ]
                              ],
                              "geodiversity_normalized": [
                                [
                                  "AP",
                                  0.3761535390278368
                                ],
                                [
                                  "US",
                                  0.0005015965168831449
                                ]
                              ],
                              "tld_geodiversity": [],
                              "geoscore": 0,
                              "ks_test": 0,
                              "attack: "",
                                "threat_type: ""
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

    @function("umbrella_domain_security_info")
    def _umbrella_domain_security_info_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Security Investigate for Information for a Domain"""
        try:
            # Get the function parameters:
            umbinv_domain = kwargs.get("umbinv_domain")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_domain: %s", umbinv_domain)

            if umbinv_domain is None:
                raise ValueError("Required parameter 'umbinv_domain' not set")

            self._params = {"domain": umbinv_domain}

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_domain'):
                raise ValueError("Parameter 'umbinv_domain' was not processed correctly")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            results = {"security_info": json.loads(json.dumps(rinv.security(self._domain)))}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()