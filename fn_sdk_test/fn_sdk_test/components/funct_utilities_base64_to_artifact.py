# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_base64_to_artifact''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_base64_to_artifact")
    def _utilities_base64_to_artifact_function(self, event, *args, **kwargs):
        """Function: Creates a new artifact from a Base64 string. You can  specify the artifact type and description."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_base64_to_artifact' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            artifact_file_type = self.get_select_param(kwargs.get("artifact_file_type"))  # select, values: "Email Attachment", "Malware Sample", "Log File", "X509 Certificate File", "RFC 822 Email Message File", "Other File"
            base64content = kwargs.get("base64content")  # text
            incident_id = kwargs.get("incident_id")  # number
            file_name = kwargs.get("file_name")  # text
            description = self.get_textarea_param(kwargs.get("description"))  # textarea
            content_type = kwargs.get("content_type")  # text

            log = logging.getLogger(__name__)
            log.info("artifact_file_type: %s", artifact_file_type)
            log.info("base64content: %s", base64content)
            log.info("incident_id: %s", incident_id)
            log.info("file_name: %s", file_name)
            log.info("description: %s", description)
            log.info("content_type: %s", content_type)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_base64_to_artifact' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
