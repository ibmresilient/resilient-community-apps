# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Classifiers against a Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs
from resilient_lib import validate_fields

FN_NAME = "umbrella_classifiers"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_classifiers' of
    package fn_cisco_umbrella_inv. This function can only be used with legacy version of Cisco Umbrella Investigate.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domain, umbinv_classifiers_endpoint

    An example of a set of query parameter might look like the following:

            umbinv_domain = "cosmos.furnipict.com"

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result in
    JSON format similar to the following.

        {'domain_name': 'cosmos.furnipict.com',
         'query_execution_time': '2018-06-18 11:53:01'
         'classifiers_info': {'first_queried_converted': '2016-11-18 19:16:00', 'firstQueried': 1479496560000},
         'classifiers_classifiers': {'securityCategories': ['Malware'], 'attacks': ['Neutrino'],
                                     'threatTypes': ['Exploit Kit']}
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)
        # Validate required settings in the app.config
        validate_fields(["api_token", "base_url", "results_limit"], self.options)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Classifiers."""
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
            classifiers_res, info_res = True, True

            # Run against 'classifiers' endpoint
            rtn_classifiers = invClient.make_api_call("GET", URIs.get("classifiers_classifiers").format(domain))
            # Run against 'info' endpoint
            rtn_info = invClient.make_api_call("GET", URIs.get("classifiers_info").format(domain))
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            if ("securityCategories" in rtn_classifiers and not rtn_classifiers.get("securityCategories")) and \
                    ("attacks" in rtn_classifiers and not rtn_classifiers.get("attacks")) and \
                    ("threatTypes" in rtn_classifiers and not rtn_classifiers.get("threatTypes")):
                classifiers_res = False

            if "firstQueried" in rtn_info and not rtn_info.get("firstQueried"):
                info_res = False
            else:
                # Make 'firstQueried' more readable
                fq = rtn_info.get("firstQueried")
                try:
                    fq_readable = datetime.fromtimestamp(int(fq) / 1000).strftime('%Y-%m-%d %H:%M:%S')
                    rtn_info["first_queried_converted"] = fq_readable
                except ValueError:
                    yield FunctionResult({}, success=False, reason='timestamp value incorrectly specified')

            results = {}
            if not classifiers_res and not info_res:
                yield self.status_message(f"No Results returned for domain '{domain}'.")
            else:
                # Add "query_execution_time" and "domain_name" to result to facilitate post-processing.
                results = {"classifiers_classifiers": rtn_classifiers,
                            "classifiers_info": rtn_info,
                            "domain_name": domain,
                            "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'classifiers and info' results for domain '{domain}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
