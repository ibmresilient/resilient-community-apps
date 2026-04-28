# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.

""" SOAR functions component to run an Umbrella investigate Query - Domain Status and Categorization against a
Cisco Umbrella server """

# Set up:
# Destination: a Queue named "umbrella_investigate".
# Manual Action: Execute a REST query against a Cisco Umbrella server.
from json import dumps
from datetime import datetime
from urllib.parse import urljoin

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs, DOMAIN_ERR
from resilient_lib import validate_fields

FN_NAME = "umbrella_domain_status_and_category"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_domain_status_and_category' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup takes the following parameters:
        umbinv_domains, umbinv_status_endpoint

    An example of a set of query parameter might look like the following:
        umbinv_domains = "amazon.com" or umbinv_domains = '"google.com","yahoo.com"' \
            or umbinv_domains = '"google.com" "yahoo.com"'
        umbinv_status_endpoint = "categorization" or status_endpoint = "categories"

    For status_endpoint = "categorization", the Investigate Query will executes a REST call against the Cisco Umbrella
    Investigate server and returns a result in JSON format similar to the following for single domain. Note: The
    Function adds an extra "domains" field in the returned result to aid post-processing.

         {'domains': ['amazon.com'],
          'query_execution_time': '2018-04-27 11:37:38',
          'statuses': {'amazon.com': {'status': 1,
                                       'content_categories': ['Ecommerce/Shopping'],
                                       'security_categories': []
                                      }
                      }
        }
    Categories can only be used with legacy version of Cisco Umbrella Investigate.
    For status_endpoint = "categories", the Investigate Query will executes a REST call against the Cisco Umbrella
    Investigate server and returns a result in JSON format similar to the following giving a list of category numbers
    mapped to strings. Note: The Function adds extra "min_id" and "max_id" field in the returned result to aid
    post-processing.

        {"query_execution_time": '2018-04-27 11:37:38',
         "min_id": 0,
         "max_id": 150,
         "categories": {"133": "Safe for Kids",
                        "132": "SaaS and B2B",
                        "131": "Real Estate",
                        "141": "Organization Email"}
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Domain Status and Categorization."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_status_endpoint"], fn_inputs)
            # Get the function parameters:
            umbinv_domains = getattr(fn_inputs, "umbinv_domains", None)  # text
            umbinv_status_endpoint = self.get_select_param(getattr(fn_inputs, "umbinv_status_endpoint", None))  # select, values: "categorization", "categories"

            self.LOG.info("umbinv_domains: %s", umbinv_domains)
            self.LOG.info("umbinv_status_endpoint: %s", umbinv_status_endpoint)

            if not umbinv_domains and umbinv_status_endpoint == "categorization":
                raise ValueError("Parameter 'umbinv_domains' should be set if 'umbinv_status_endpoint' has value 'categorization'.")

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            domains = None
            process_result = {}
            params = {"domains": umbinv_domains, "status_endpoint": umbinv_status_endpoint}

            # Reset 'domains' param if input parameters set.
            if umbinv_domains:
                params.setdefault("domains", umbinv_domains.strip())

            process_params(params, process_result)

            if umbinv_status_endpoint == "categorization":
                if "_domains" not in process_result:
                    raise ValueError("Parameter 'umbinv_domains' was not processed correctly")
                else:
                    domains = process_result.pop("_domains")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if umbinv_status_endpoint == "categories":
                cat_keys = []
                # Add metadata of "query_execution_time", "min_id" and "max_id" keys to make it easier in post-processing.
                rtn = invClient.make_api_call("GET", URIs.get("categories"))
                for c in rtn:
                    cat_keys.append(c)
                    cat_keys_int = list(map(int, cat_keys))
                results = {"categories": rtn, "min_id": min(cat_keys_int),
                           "max_id": max(cat_keys_int), "query_execution_time": query_execution_time}
                yield self.status_message("Returning 'categories' list results.")

            elif umbinv_status_endpoint == "categorization":
                if domains:
                    if not isinstance(domains, (str, list)):
                        raise DOMAIN_ERR
                    rtn = invClient.make_api_call("POST" if isinstance(domains, str) else "POST",
                                                  URIs.get("categorization"),
                                                  data=str(domains) if isinstance(domains, list) else None)
                dom_list = [d for d in rtn]
                # Add "query_execution_time" and "domains" key to result to facilitate post-processing.
                results = {"statuses": rtn, "domains": dom_list,
                           "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning categorization 'statuses' results for domains '{dom_list}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            #Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
