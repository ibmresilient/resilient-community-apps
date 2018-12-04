# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from phish_ai_api import API


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'phish_ai_get_report"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_phish_ai", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_phish_ai", {})

    @function("phish_ai_get_report")
    def _phish_ai_get_report_function(self, event, *args, **kwargs):
        """Function: Returns report of a URL scan from Phish.AI."""
        try:
            start_time = time.time()
            yield StatusMessage("starting...")
            api_key = self.options.get("phishai_api_key", None)

            # Get the function parameters:
            phishai_scan_id = kwargs.get("phishai_scan_id")  # text

            log = logging.getLogger(__name__)
            if phishai_scan_id is not None:
                log.info("phishai_scan_id: %s", phishai_scan_id)
            else:
                raise FunctionError("phishai_scan_id needs to be set to run this function.")

            ph = API(api_key=api_key)
            res = ph.get_report(phishai_scan_id)

            end_time = time.time()
            yield StatusMessage("done...")
            results = {
                "Inputs": {
                    "phishai_scan_id": phishai_scan_id
                },
                "Run Time": str(end_time - start_time),
                "Value": res
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
