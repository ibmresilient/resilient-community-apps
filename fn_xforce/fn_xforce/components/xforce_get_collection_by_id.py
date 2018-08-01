# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'xforce_get_collection_by_id"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_xforce", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_xforce", {})

    @function("xforce_get_collection_by_id")
    def _xforce_get_collection_by_id_function(self, event, *args, **kwargs):
        """Function: Takes in a parameter of a casefileID and then submits this to the X-Force API to gather data for the provided case."""
        try:
            # Get the function parameters:
            xforce_collection_id = kwargs.get("xforce_collection_id")  # text

            log = logging.getLogger(__name__)
            log.info("xforce_collection_id: %s", xforce_collection_id)

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