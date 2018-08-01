# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'xforce_query_collection"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_xforce", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_xforce", {})

    @function("xforce_query_collection")
    def _xforce_query_collection_function(self, event, *args, **kwargs):
        """Function: Allows user to submit a query to the X-Force Collections API. Supports searching either public or private collections."""
        try:
            # Get the function parameters:
            xforce_collections_type = self.get_select_param(kwargs.get("xforce_collections_type"))  # multiselect, values: "public", "private"
            xforce_query = kwargs.get("xforce_query")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collections_type: %s", xforce_collections_type)
            log.info("xforce_query: %s", xforce_query)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            results = {
                "value": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()