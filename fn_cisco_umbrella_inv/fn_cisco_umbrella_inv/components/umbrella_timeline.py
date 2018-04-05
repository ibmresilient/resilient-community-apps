# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Timeline against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
import logging
import json

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_dns_rr_hist' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        resource

    An example of a set of query parameter might look like the following:

            resource = "example.com" or resource = "http://domain.org/index.html"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.

        {"timeline": [
                      {
                        categories: [ ],
                        attacks: [ ],
                        threatTypes: [ ],
                        timestamp: 1501697925911
                      },
                      {
                        categories: [
                          "Malware"
                        ],
                        attacks: [ ],
                        threatTypes: [
                          "Exploit Kit"
                        ],
                        timestamp: 1488397543490
                      }
                    ]
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

    @function("umbrella_timeline")
    def _umbrella_timeline_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate Investigate for  Timeline."""
        try:
            # Get the function parameters:
            resource = kwargs.get("resource")  # text

            log = logging.getLogger(__name__)

            log.info("resource: %s", resource)

            if resource is None:
                raise ValueError("Required parameter 'resource' not set")

            self._params = {"resource": resource}

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_res'):
               raise ValueError("Parameter 'resource' was not processed correctly")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            results = json.loads(json.dumps({"timeline": rinv.timeline(self._res)}))
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()