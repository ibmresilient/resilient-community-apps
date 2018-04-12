# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Latest Malicious Domains for an IP against a
Cisco Umbrella server """

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
        ipaddr

    An example of a set of query parameter might look like the following:

            ipaddr = "218.23.28.135"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {"latest_malicious_domains": [{
                                        "id": 22842894,
                                        "name": "www.cxhyly.com"
                                      },
                                      {
                                        "id": 22958747,
                                        "name": "cxhyly.com"
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

    @function("umbrella_ip_latest_malicious_domains")
    def _umbrella_ip_latest_malicious_domains_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Latest Malicious Domains for an IP."""
        try:
            # Get the function parameters:
            umbinv_ipaddr = kwargs.get("umbinv_ipaddr")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_ipaddr: %s", umbinv_ipaddr)

            if umbinv_ipaddr is None:
                raise ValueError("Required parameter 'umbinv_ipaddr' not set")

            self._params = {"ipaddr": umbinv_ipaddr}

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_ipaddr'):
               raise ValueError("Parameter 'ipaddr' was not processed correctly")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            results = {"latest_malicious_domains": json.loads(json.dumps(rinv.latest_domains(self._ipaddr)))}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()