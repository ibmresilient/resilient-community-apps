# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_base64_to_attachment"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_codegen_test", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_codegen_test", {})

    @function("utilities_base64_to_attachment")
    def _utilities_base64_to_attachment_function(self, event, *args, **kwargs):
        """Function: Creates a new attachment from a base64 string."""
        try:
            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Get the function parameters:
            base64content = kwargs.get("base64content")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            file_name = kwargs.get("file_name")  # text
            content_type = kwargs.get("content_type")  # text

            log = logging.getLogger(__name__)
            log.info("base64content: %s", base64content)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("file_name: %s", file_name)
            log.info("content_type: %s", content_type)

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