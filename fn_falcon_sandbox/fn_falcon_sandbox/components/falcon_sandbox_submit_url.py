# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'falcon_sandbox_submit_url"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_falcon_sandbox", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_falcon_sandbox", {})

    @function("falcon_sandbox_submit_url")
    def _falcon_sandbox_submit_url_function(self, event, *args, **kwargs):
        """Function: Submit URL of file to Falcon Sandbox for analysis"""
        try:
            # Get the function parameters:
            falcon_sandbox_incident_id = kwargs.get("falcon_sandbox_incident_id")  # number
            falcon_sandbox_artifact_id = kwargs.get("falcon_sandbox_artifact_id")  # number
            falcon_sandbox_input_url = kwargs.get("falcon_sandbox_input_url")  # text

            log = logging.getLogger(__name__)
            log.info("falcon_sandbox_incident_id: %s", falcon_sandbox_incident_id)
            log.info("falcon_sandbox_artifact_id: %s", falcon_sandbox_artifact_id)
            log.info("falcon_sandbox_input_url: %s", falcon_sandbox_input_url)

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