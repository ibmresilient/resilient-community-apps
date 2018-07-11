# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params, omit_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_pattern_search' of
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
         "search_matches": {  "expression": "exa[a-z]ple.com",
                              "totalResults": 1,
                              "moreDataAvailable": false,
                              "limit": 30,
                              "matches": [
                                {
                                  "name": "example",
                                  "firstSeen": 1432330927421,
                                  "firstSeenISO": "2015-05-22T21:42:07.421Z",
                                  "securityCategories": [
                                    "Botnet"
                                  ]
                                }
                              ]
                            }
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

    @function("umbrella_pattern_search")
    def _umbrella_pattern_search_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Pattern Search."""
        try:
            # Get the function parameters:
            umbinv_regex = kwargs.get("umbinv_regex")  # text
            umbinv_start_epoch = kwargs.get("umbinv_start_epoch")  # datetimepicker
            umbinv_start_relative = kwargs.get("umbinv_start_relative")  # text
            umbinv_limit = kwargs.get("umbinv_limit")  # number
            umbinv_include_category = kwargs.get("umbinv_include_category")  # boolean

            log = logging.getLogger(__name__)
            log.info("umbinv_regex: %s", umbinv_regex)
            log.info("umbinv_start_epoch: %s", umbinv_start_epoch)
            log.info("umbinv_start_relative: %s", umbinv_start_relative)
            log.info("umbinv_limit: %s", umbinv_limit)
            log.info("umbinv_include_category: %s", umbinv_include_category)

            if is_none(umbinv_regex):
                raise ValueError("Required parameter 'regex' not set")

            yield StatusMessage("Starting...")
            regex = None
            process_result = {}
            params = {"regex": umbinv_regex.strip(), "start_epoch": umbinv_start_epoch,
                            "start_relative": umbinv_start_relative,
                            "limit": umbinv_limit, "include_category": umbinv_include_category}

            validate_params(params)
            process_params(params, process_result)

            if "_regex" not in process_result:
               raise ValueError("Parameter 'umbinv_regex' was not processed correctly")
            else:
                regex = process_result.pop("_regex")

            api_token = self.options.get("api_token")
            base_url = self.options.get("base_url")
            rinv = ResilientInv(api_token, base_url)

            yield StatusMessage("Running Cisco Investigate query...")
            rtn = rinv.search(regex, **omit_params(params, ["regex"]))
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            if len(rtn["matches"]) == 0:
                log.debug(json.dumps(rtn))
                yield StatusMessage("No Results returned for regular expression '{}'.".format(regex))
                results = {}
            else:
                # Add "query_execution_time" to result to facilitate post-processing.
                results = {"search_matches": json.loads(json.dumps(rtn)), "query_execution_time": query_execution_time}
                yield StatusMessage("Returning 'search_matches' results for regex '{}'.".format(regex))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function.")
            yield FunctionError()