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
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_ip_latest_malicious_domains' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_ipaddr

    An example of a set of query parameter might look like the following:

            umbinv_ipaddr = "218.23.28.135"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'ip_address': '104.27.163.228',
         'query_execution_time': '2018-05-02 16:22:14',
        'latest_malicious_domains': [u'textspeier.de']
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

    @function("umbrella_ip_latest_malicious_domains")
    def _umbrella_ip_latest_malicious_domains_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Latest Malicious Domains for an IP."""
        try:
            # Get the function parameters:
            umbinv_ipaddr = kwargs.get("umbinv_ipaddr")  # text

            log = logging.getLogger(__name__)
            log.info("umbinv_ipaddr: %s", umbinv_ipaddr)

            if is_none(umbinv_ipaddr):
                raise ValueError("Required parameter 'umbinv_ipaddr' not set")

            yield StatusMessage("Starting...")
            ipaddr = None
            process_result = {}
            params = {"ipaddr": umbinv_ipaddr.strip()}

            validate_params(params)
            process_params(params, process_result)

            if "_ipaddr" not in process_result:
                 raise ValueError("Parameter 'ipaddr' was not processed correctly")
            else:
                ipaddr = process_result.pop("_ipaddr")


            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.latest_domains(ipaddr)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn) == 0:
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for ip address '{}'.".format(ipaddr))
                results = {}
            else:
                # Add  "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"latest_malicious_domains": json.loads(json.dumps(rtn)), "ip_address": ipaddr,
                           "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'latest_malicious_domains' results for ip address '{}'.".format(ipaddr))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()