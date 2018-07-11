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
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, is_none


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_domain_co_occurrences' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domain

    An example of a set of query parameter might look like the following:

            umbinv_domain = "malware.com"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.



    The Investigate Query will executs a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'domain_name': 'googlevideo.com',
         'query_execution_time': '2018-05-02 16:03:15',
         'cooccurrences': { u'found': True,
                            u'domain_name': u'googlevideo.com'
                            u'pfs2': [[u'gowatchfreemovies.to', 0.14300200812663327],
                            [u'www.mc-skv.com', 0.12482579576302438],
                                ...
                                ...
                            [u'r5---sn-n4v7sn7l.googlevideo.com', 0.0064511764392265955],
                            [u'sage200.co.uk', 0.006262067692875829],
                            [u'demon.co.uk', 0.005126508408778887]]
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

    @function("umbrella_domain_co_occurrences")
    def _umbrella_domain_co_occurrences_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Co-Occurrences for a Domain."""
        try:
            # Get the function parameters:
            umbinv_domain = kwargs.get("umbinv_domain")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_domain: %s", umbinv_domain)

            if is_none(umbinv_domain):
                raise ValueError("Required parameter 'umbinv_domain' not set")

            yield StatusMessage("Starting...")
            domain = None
            process_result = {}
            params = {"domain": umbinv_domain.strip()}

            validate_params(params)
            process_params(params, process_result)

            if "_domain" not in process_result:
                 raise ValueError("Parameter 'umbinv_domain' was not processed correctly")
            else:
                domain = process_result.pop("_domain")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.cooccurrences(domain)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if rtn["found"] is None or str(rtn["found"]).lower() == 'false':
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for domain '{}'.".format(domain))
                results = {}
            else:
                # Add "query_execution_time" and "domain_name" to result to facilitate post-processing.
                results = {"cooccurrences": json.loads(json.dumps(rtn)), "domain_name": domain,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'cooccurrences' results for domain '{}'.".format(domain))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()