# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_attachment_to_base64''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_attachment_to_base64")
    def _utilities_attachment_to_base64_function(self, event, *args, **kwargs):
        """Function: Reads a file attachment in the incident, and produces a base64-encoded string with the file attachment content. This content can then be used in combination with other workflow functions to create an artifact, a new file attachment, or to analyze the contents using various tools."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_attachment_to_base64' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            task_id = kwargs.get("task_id")  # number
            incident_id = kwargs.get("incident_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            artifact_id = kwargs.get("artifact_id")  # number

            log = logging.getLogger(__name__)
            log.info("task_id: %s", task_id)
            log.info("incident_id: %s", incident_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("artifact_id: %s", artifact_id)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_attachment_to_base64' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
