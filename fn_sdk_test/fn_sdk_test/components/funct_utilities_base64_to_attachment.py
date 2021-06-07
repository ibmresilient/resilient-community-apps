# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_base64_to_attachment''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_base64_to_attachment")
    def _utilities_base64_to_attachment_function(self, event, *args, **kwargs):
        """Function: Creates a new attachment from a base64 string."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_base64_to_attachment' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            base64content = kwargs.get("base64content")  # text
            incident_id = kwargs.get("incident_id")  # number
            file_name = kwargs.get("file_name")  # text
            task_id = kwargs.get("task_id")  # number
            content_type = kwargs.get("content_type")  # text

            log = logging.getLogger(__name__)
            log.info("base64content: %s", base64content)
            log.info("incident_id: %s", incident_id)
            log.info("file_name: %s", file_name)
            log.info("task_id: %s", task_id)
            log.info("content_type: %s", content_type)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_base64_to_attachment' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
