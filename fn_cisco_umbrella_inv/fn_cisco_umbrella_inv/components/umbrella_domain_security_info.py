# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Security Information for a Domain against a Cisco
Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs
from resilient_lib import validate_fields

FN_NAME = "umbrella_domain_security_info"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_domain_security_info' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domain

    An example of a set of query parameter might look like the following:
        umbinv_domain = "example.com"

    The Investigate Query will execute a REST call against the Cisco Umbrella Investigate server and returns a result in
    JSON format similar to the following.Note: The Function adds an extra "domain_name" field in the returned result to
    aid post-processing.

        {
            'domain_name': 'domain.com',
            'query_execution_time': '2018-04-27 11:37:38',
            'security_info':{
              'domain_name':'example.com',
              'found':True,
              'geodiversity_normalized':[
                 ['??',0.5706777350888877],
                 ['DZ',0.000126500569665041]
              ],
              'geodiversity':[
                 ['US',0.4534],
                 ['LB',0.0001]
              ],
              'dga_score':0.0,
              'rip_score':0.0,
              'asn_score':-0.041783697445309576,
              'securerank2':100.0,
              'popularity':100.0,
              'geoscore':0.0,
              'attack':'',
              'pagerank':40.914368,
              'entropy':2.521640636343318,
              'ks_test':0.0,
              'prefix_score':0.0,
              'perplexity':0.2327827581680193,
              'fastflux':False,
              'threat_type':'',
              'tld_geodiversity':[]
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Security Information for a Domain"""
        try:
            # Validate required input fields
            validate_fields(["umbinv_domain"], fn_inputs)
            # Get the function parameters:
            umbinv_domain = fn_inputs.umbinv_domain  # text
            self.LOG.info("umbinv_domain: %s", umbinv_domain)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            process_result = {}
            process_params({"domain": umbinv_domain.strip()}, process_result)

            domain = None
            if "_domain" not in process_result:
                 raise ValueError("Parameter 'umbinv_domain' was not processed correctly")
            domain = process_result.pop("_domain")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            rtn = invClient.make_api_call("GET", URIs.get("security").format(domain))

            results = {}
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if not rtn.get("found", False):
                yield self.status_message(f"No Results returned for domain '{domain}'.")
            else:
                # Add "query_execution_time" and "domain_name" to result to facilitate post-processing.
                results = {"security_info": rtn, "domain_name": domain,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'security_info' results for domain '{domain}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
