# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_phish_ai.lib.phish_ai_helper import PhishAI, PACKAGE_NAME


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'phish_ai_get_report"""

    def load_options(self, opts):
        """ Get app.config parameters and validate them. """
        self.options = opts.get(PACKAGE_NAME, {})
        self.opts = opts

        # Validate required fields in app.config are set
        required_fields = ["phishai_api_key"]
        validate_fields(required_fields, self.options)

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.load_options(opts)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.load_options(opts)

    @function("phish_ai_get_report")
    def _phish_ai_get_report_function(self, event, *args, **kwargs):
        """Function: Returns report of a URL scan from Phish.AI."""
        try:
            start_time = time.time()
            yield StatusMessage("starting...")
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            phishai_scan_id = kwargs.get("phishai_scan_id")  # text

            log = logging.getLogger(__name__)

            log.info("phishai_scan_id: %s", phishai_scan_id)

            ph = PhishAI(self.opts, self.options)

            response_json = ph.get_report(phishai_scan_id)

            if response_json.get("status") != "completed":
                raise FunctionError("Timed out getting report from Phish.AI")

            end_time = time.time()

            if response_json.status_code == 200:
                success = True
            else:
                success = False

            yield StatusMessage("done...")
            results = rp.done(success, response_json)

            """results = {
                "inputs": {
                    "phishai_scan_id": phishai_scan_id
                },
                "run_time": str(end_time - start_time),
                "content": respsonse_json
            }"""

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
