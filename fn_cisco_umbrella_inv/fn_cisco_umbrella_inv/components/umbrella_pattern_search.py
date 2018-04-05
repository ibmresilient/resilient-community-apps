# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_umbrella_inv.util.resilient_inv import ResilientInv
from fn_cisco_umbrella_inv.util.helpers import validate_opts, validate_params, process_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'umbrella_pattern_search' of
    package fn_cisco_umbrella_inv.

    The Function does a Cisco Umbrella Investigate query lookup and takes the following parameters:
            regex, [start_epoch or start_relative], limit, include_category

    An example of a set of query parameter might look like the following:

            regex = "exa\[a-z\]ple.c"
            start_relative = "-30days" or start_epoch = 1525517214000
            limit = 30
            include_category = True

    The Investigate Query will executes a REST call against the Cisco Umbrella Investigate server and returns a result
    in JSON format similar to the following.

        {"search_matches": {  "expression": "exa[a-z]ple.com",
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

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_umbrella_inv", {})

    @function("umbrella_pattern_search")
    def _umbrella_pattern_search_function(self, event, *args, **kwargs):
        """Function: Resilient Function : Cisco Umbrella Investigate for Pattern Search."""
        try:
            # Get the function parameters:
            regex = kwargs.get("regex")  # text
            start_epoch = kwargs.get("start_epoch")  # datetimepicker
            start_relative = kwargs.get("start_relative")  # text
            limit = kwargs.get("limit")  # number
            include_category = kwargs.get("include_category")  # boolean

            log = logging.getLogger(__name__)
            log.info("regex: %s", regex)
            log.info("start_epoch: %s", start_epoch)
            log.info("start_relative: %s", start_relative)
            log.info("limit: %s", limit)
            log.info("include_category: %s", include_category)
            if regex is None:
                raise ValueError("Required parameter 'regex' not set")

            self._params = {"regex": regex, "start_epoch": start_epoch,"start_relative": start_relative,
                            "limit": limit, "include_category": include_category, }

            yield StatusMessage("Starting...")
            validate_opts(self)
            validate_params(self)
            process_params(self)

            if not hasattr(self, '_regex'):
               raise ValueError("Parameter 'regex' was not processed correctly")

            api_token = self.options.get("api_token")
            rinv = ResilientInv(api_token)

            yield StatusMessage("Running Cisco Investigate query...")
            results = {"search_matches": json.loads(json.dumps(rinv.search(self._regex, **helpers.omit_params(self._params, ["regex"]))))}
            yield StatusMessage("done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()