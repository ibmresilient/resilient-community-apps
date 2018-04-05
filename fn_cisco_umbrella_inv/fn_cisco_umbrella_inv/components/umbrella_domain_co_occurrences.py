# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Co-Occurrences for a Domain against a Cisco
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
    """Component that implements Resilient function 'umbrella_domain_co_occurrences' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        domain

    An example of a set of query parameter might look like the following:

            domain = "malware.com"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.



    The Investigate Query will executs a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {"cooccurrences": {"pfs2": [
                                    "found": true,
                                        [
                                            "download.example.com",
                                            0.9320288065469468
                                        ],
                                        [
                                            "query.example.com",
                                            0.06797119345305325
                                        ]
                                    ],
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

    @function("umbrella_domain_co_occurrences")
    def _umbrella_domain_co_occurrences_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Co-Occurrences for a Domain."""
        try:
            # Get the function parameters:
            domain = kwargs.get("domain")  # text

            log = logging.getLogger(__name__)
            log.info("input: %s", input)

            if domain is None:
                raise ValueError("Required parameter 'domain' not set")

            self._params = {"domain": domain}

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_domain'):
               raise ValueError("Parameter 'domain' was not processed correctly")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            results = {"cooccurrences": json.loads(json.dumps(rinv.cooccurrences(self._domain)))}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()