# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation"""
from urllib.parse import quote_plus
from datetime import datetime

from resilient_circuits import AppFunctionComponent, FunctionResult, app_function
from fn_cisco_umbrella_inv.util.helpers import process_params, PACKAGE_NAME,\
    investigateClient, URIs, get_time_input
from resilient_lib import validate_fields

FN_NAME = "umbrella_pattern_search"

class FunctionComponent(AppFunctionComponent):
    """Component that implements SOAR function 'umbrella_pattern_search' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
        umbinv_regex, [umbinv_start_epoch or umbinv_start_relative], umbinv_limit, umbinv_include_category

    An example of a set of query parameter might look like the following:
        umbinv_regex = "exa\[a-z\]ple.c"
        umbinv_start_relative = "-30days" or start_epoch = 1525517214000
        umbinv_limit = 30
        umbinv_include_category = True

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {"query_execution_time": '2018-05-02 16:03:15'
         "search_matches": {"expression": "exa[a-z]ple.com",
                "totalResults": 1,
                "moreDataAvailable": false,
                "limit": 30,
                "matches": [{
                    "name": "example",
                    "firstSeen": 1432330927421,
                    "firstSeenISO": "2015-05-22T21:42:07.421Z",
                    "securityCategories": ["Botnet"]
                }]
            }
        }
    """
    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """Function: SOAR Function: Cisco Umbrella Investigate for Pattern Search."""
        try:
            # Validate required input fields
            validate_fields(["umbinv_regex"], fn_inputs)
            # Get the function parameters:
            umbinv_regex = fn_inputs.umbinv_regex  # text
            umbinv_start_epoch = getattr(fn_inputs, "umbinv_start_epoch", None)  # datetimepicker
            umbinv_start_relative = getattr(fn_inputs, "umbinv_start_relative", None)  # text
            umbinv_limit = getattr(fn_inputs, "umbinv_limit", 30)  # number
            umbinv_include_category = getattr(fn_inputs, "umbinv_include_category", False)  # boolean

            self.LOG.info("umbinv_regex: %s", umbinv_regex)
            self.LOG.info("umbinv_start_epoch: %s", umbinv_start_epoch)
            self.LOG.info("umbinv_start_relative: %s", umbinv_start_relative)
            self.LOG.info("umbinv_limit: %s", umbinv_limit)
            self.LOG.info("umbinv_include_category: %s", umbinv_include_category)

            yield self.status_message(f"Starting App Function: '{FN_NAME}'")
            # If both start epoch and start relative are given then use start epoch
            if umbinv_start_epoch and umbinv_start_relative:
                umbinv_start_relative = None
                self.LOG.info("Both umbinv_start_epoch and umbinv_start_relative were given. Using umbinv_start_epoch.")

            regex = None
            process_result = {}
            params = {"regex": umbinv_regex.strip(), "start_epoch": umbinv_start_epoch,
                "start_relative": umbinv_start_relative,
                "limit": umbinv_limit, "include_category": umbinv_include_category}
            process_params(params, process_result)

            if "_regex" not in process_result:
               raise ValueError("Parameter 'umbinv_regex' was not processed correctly")
            else:
                regex = process_result.pop("_regex")

            invClient = investigateClient(self.options, self.rc)

            yield self.status_message("Running Cisco Investigate query...")
            rtn = invClient.make_api_call("GET",
                                          URIs.get("search").format(quote_plus(regex)),
                                          params={"start": get_time_input(params.get("start")),
                                                  "limit": umbinv_limit,
                                                  "includeCategory": str(umbinv_include_category).lower()})

            results = {}
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn.get("matches")) == 0:
                yield self.status_message(f"No Results returned for regular expression '{regex}'.")
            else:
                # Add "query_execution_time" to result to facilitate post-processing.
                results = {"search_matches": rtn, "query_execution_time": query_execution_time}
                yield self.status_message(f"Returning 'search_matches' results for regex '{regex}'.")

            yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            yield FunctionResult({}, success=False, reason=str(err))
