# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_string_to_attachment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_codegen_test", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_codegen_test", {})

    @function("utilities_string_to_attachment")
    def _utilities_string_to_attachment_function(self, event, *args, **kwargs):
        """Function: Creates a new file (.txt) attachment in the incident or task from a string that your workflow provides as input."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            string_to_convert_to_attachment = kwargs.get("string_to_convert_to_attachment")  # text
            attachment_name = kwargs.get("attachment_name")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number

            log = logging.getLogger(__name__)
            log.info("string_to_convert_to_attachment: %s", string_to_convert_to_attachment)
            log.info("attachment_name: %s", attachment_name)
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