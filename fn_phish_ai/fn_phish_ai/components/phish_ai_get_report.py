# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
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
            timeout_seconds = int(self.options.get("timeout_seconds", 60))

            # Get the function parameters:
            phishai_scan_id = kwargs.get("phishai_scan_id")  # text

            log = logging.getLogger(__name__)
            if phishai_scan_id is not None:
                log.info("phishai_scan_id: %s", phishai_scan_id)
            else:
                raise ValueError("phishai_scan_id needs to be set to run this function.")

            res = {}
            ph = API(api_key=api_key)

            # Keep checking until report is ready, will timeout after a minute
            i = 0
            while i < round(timeout_seconds/5):
                time.sleep(5)
                res = ph.get_report(phishai_scan_id)
                if res.get("status") == "completed":
                    break
                i += 5
                yield StatusMessage("Waiting for report to report to complete")

            if res.get("status") != "completed":
                raise FunctionError("Timed out getting report from Phish.AI")

            end_time = time.time()
            yield StatusMessage("done...")
            results = {
                "inputs": {
                    "phishai_scan_id": phishai_scan_id
                },
                "run_time": str(end_time - start_time),
                "content": res
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
