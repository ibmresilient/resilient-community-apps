# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import validate_fields, ResultPayload
from fn_phish_ai.lib.phish_ai_helper import PhishAI, PACKAGE_NAME

LOG = logging.getLogger(__name__)

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
            yield StatusMessage("starting...")
            rp = ResultPayload(PACKAGE_NAME, **kwargs)

            # Get the function parameters:
            phishai_scan_id = kwargs.get("phishai_scan_id")  # text

            LOG.info(u"phishai_scan_id: %s", phishai_scan_id)

            ph = PhishAI(self.opts, self.options)

            # Get the report
            response_json = ph.get_report(phishai_scan_id)

            yield StatusMessage("done...")
            results = rp.done(True, response_json)

            # For backward compatibility with v1.0.0
            results["run_time"] = str(results['metrics']['execution_time_ms'] /1000)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
