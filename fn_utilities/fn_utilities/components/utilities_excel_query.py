# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_excel_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_utilities", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_utilities", {})

    @function("utilities_excel_query")
    def _utilities_excel_query_function(self, event, *args, **kwargs):
        """Function: Extract ranges of data or named ranges specified by the user from an excel document."""
        try:
            # Get the function parameters:
            attachment_id = kwargs.get("attachment_id")  # number
            excel_ranges = kwargs.get("excel_ranges")  # text
            excel_defined_names = kwargs.get("excel_defined_names")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number

            log = logging.getLogger(__name__)
            log.info("attachment_id: %s", attachment_id)
            log.info("excel_ranges: %s", excel_ranges)
            log.info("excel_defined_names: %s", excel_defined_names)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)

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