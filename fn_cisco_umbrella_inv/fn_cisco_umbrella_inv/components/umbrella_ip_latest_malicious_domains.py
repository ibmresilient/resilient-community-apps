# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Latest Malicious Domains for an IP against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs, IP_PATTERN, IP_ERR
from resilient_lib import validate_fields

FN_NAME = "umbrella_ip_latest_malicious_domains"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_ip_latest_malicious_domains' of
    package fn_cisco_umbrella_inv.
    This function can only be used with legacy version of Cisco Umbrella Investigate.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_ipaddr

    An example of a set of query parameter might look like the following:
        umbinv_ipaddr = "218.23.28.135"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {'ip_address': '104.27.163.228',
         'query_execution_time': '2018-05-02 16:22:14',
        'latest_malicious_domains': ['textspeier.de']
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Latest Malicious Domains for an IP."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_ipaddr"], fn_inputs)
            # Get the function parameters:
            umbinv_ipaddr = fn_inputs.umbinv_ipaddr  # text
            self.LOG.info("umbinv_ipaddr: %s", umbinv_ipaddr)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            ipaddr = None
            process_result = {}
            process_params({"ipaddr": umbinv_ipaddr.strip()}, process_result)

            if "_ipaddr" not in process_result:
                 raise ValueError("Parameter 'ipaddr' was not processed correctly")
            else:
                ipaddr = process_result.pop("_ipaddr")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            if not IP_PATTERN.match(ipaddr):
                raise IP_ERR
            resp = invClient.make_api_call("GET", URIs.get("latest_domains").format(ipaddr))
            rtn = [ d.get("name") for d in resp if d.get("name") ]

            results = {}
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn) == 0:
                yield self.status_message(f"No Results returned for ip address '{ipaddr}'.")
            else:
                # Add  "query_execution_time" and "ip_address" to result to facilitate post-processing.
                results = {"latest_malicious_domains": rtn, "ip_address": ipaddr,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'latest_malicious_domains' results for ip address '{ipaddr}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
