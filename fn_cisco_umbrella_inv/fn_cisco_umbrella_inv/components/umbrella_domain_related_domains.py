# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run an Umbrella investigate Query - Related Domains for a Domain against a
Cisco Umbrella server """

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
    """Component that implements Resilient function 'umbrella_domain_related_domains' of package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domain

    An example of a set of query parameter might look like the following:

            umbinv_domain = "domain.com"

    The Investigate Query will executs a REST call agaist the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.


    The Investigate Query will executs a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'domain_name': 'domain.com',
         'query_execution_time': '2018-04-27 11:37:38',
         'related_domains': {u'tb1': [[u'www.domain.com', 8],
                                     [u'secure.statcounter.com', 4],
                                     [u'static.addtoany.com', 4],
                                     [u'image.tmdb.org', 3],
                                     [u'0.gravatar.com', 3],
                                     [u'1.gravatar.com', 3],
                                     [u'2.gravatar.com', 3],
                                     [u'api.bltd.ovh', 3],
                                     [u'static.vnpt.vn', 3]],
                             u'found': True
                            },
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
        validate_opts(self)

    @function("umbrella_domain_related_domains")
    def _umbrella_domain_related_domains_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for lrelated domains for a Domain."""
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
            rtn = rinv.related(domain)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if rtn["found"] is None or str(rtn["found"]).lower() == 'false':
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for domain '{}'.".format(domain))
                results = {}
            else:
                # Add "query_execution_time" and "domain_name" to result to facilitate post-processing.
                results = {"related_domains": json.loads(json.dumps(rtn)), "domain_name": domain,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'related_domains' results for domain '{}'.".format(domain))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()