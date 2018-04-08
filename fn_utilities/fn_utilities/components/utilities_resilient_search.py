# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import json
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_resilient_search"""

    @function("utilities_resilient_search")
    def _utilities_resilient_search_function(self, event, *args, **kwargs):
        """Function: Searches Resilient for incident data.
            NOTE: The results may include incidents that the current user cannot access.
            Use with caution, to avoid information disclosure."""
        try:
            # Get the function parameters:
            resilient_search_template = self.get_textarea_param(kwargs.get("resilient_search_template"))  # textarea
            resilient_search_query = kwargs.get("resilient_search_query")  # text

            log = logging.getLogger(__name__)
            log.info("resilient_search_template: %s", resilient_search_template)
            log.info("resilient_search_query: %s", resilient_search_query)

            # Read the search template as JSON
            template = json.loads(resilient_search_template)

            # Add in the search query
            template["query"] = resilient_search_query
            # Add in the current organization id (don't want results outside this org!)
            template["org_id"] = self.rest_client().org_id

            # Run the search and return the results
            yield StatusMessage("Searching...")
            results = self.rest_client().search(template)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()