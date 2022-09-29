# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Function implementation"""

import logging
import json
import re
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements SOAR function 'soar_utils_soar_search"""

    @function("soar_utils_soar_search")
    def _soar_utils_soar_search_function(self, event, *args, **kwargs):
        """Function: Searches SOAR for incident data.
            NOTE: The results may include incidents that the current user cannot access.
            Use with caution, to avoid information disclosure."""
        try:
            # Get the function parameters:
            soar_search_template = self.get_textarea_param(kwargs.get("soar_search_template"))  # textarea
            soar_search_query = kwargs.get("soar_search_query")  # text

            log = logging.getLogger(__name__)
            log.info("soar_search_template: %s", soar_search_template)
            log.info("soar_search_query: %s", soar_search_query)

            # ensure the input is properly escaped
            p = re.compile('(\[|\]|\(|\)\||\+|\-|\^|{|}|&|!|:|\?|\\|\\/)')
            soar_search_query = p.sub(r'\\\1', soar_search_query)

            # Read the search template as JSON
            template = json.loads(soar_search_template)

            # Add in the search query
            template["query"] = soar_search_query
            # Add in the current organization id (don't want results outside this org!)
            template["org_id"] = self.rest_client().org_id

            log.debug(template)

            # Run the search and return the results
            yield StatusMessage("Searching...")
            results = self.rest_client().search(template)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
