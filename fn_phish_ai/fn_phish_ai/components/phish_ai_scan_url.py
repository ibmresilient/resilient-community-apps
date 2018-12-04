# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from phish_ai_api import API


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'phish_ai_scan_url"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_phish_ai", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_phish_ai", {})

    @function("phish_ai_scan_url")
    def _phish_ai_scan_url_function(self, event, *args, **kwargs):
        """Function: Scans URL against Phish.AI."""
        try:
            start_time = time.time()
            yield StatusMessage("starting...")
            api_key = self.options.get("phishai_api_key", None)

            # Get the function parameters:
            artifact_value = kwargs.get("artifact_value")  # text

            log = logging.getLogger(__name__)
            if artifact_value is not None:
                log.info("artifact_value: %s", artifact_value)
            else:
                raise FunctionError("artifact_value needs to be set to run this function.")

            ph = API(api_key=api_key)
            res = ph.scan_url(artifact_value)

            end_time = time.time()
            yield StatusMessage("done...")
            results = {
                "Inputs": {
                    "artifact_value": artifact_value
                },
                "Run Time": str(end_time - start_time),
                "Value": res
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
