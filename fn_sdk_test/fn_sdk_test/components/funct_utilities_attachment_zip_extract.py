# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError

PACKAGE_NAME = "fn_sdk_test"


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'utilities_attachment_zip_extract''"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(PACKAGE_NAME, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(PACKAGE_NAME, {})

    @function("utilities_attachment_zip_extract")
    def _utilities_attachment_zip_extract_function(self, event, *args, **kwargs):
        """Function: Extracts a file from a ZIP file attachment, producing a base64 string.

That string can then be used as input to subsequent functions that might write it as a file attachment, as a malware sample artifact, or in other ways."""
        try:

            # Get the wf_instance_id of the workflow this Function was called in
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            yield StatusMessage("Starting 'utilities_attachment_zip_extract' running in workflow '{0}'".format(wf_instance_id))

            # Get the function parameters:
            file_path = kwargs.get("file_path")  # text
            incident_id = kwargs.get("incident_id")  # number
            task_id = kwargs.get("task_id")  # number
            zipfile_password = kwargs.get("zipfile_password")  # text
            attachment_id = kwargs.get("attachment_id")  # number

            log = logging.getLogger(__name__)
            log.info("file_path: %s", file_path)
            log.info("incident_id: %s", incident_id)
            log.info("task_id: %s", task_id)
            log.info("zipfile_password: %s", zipfile_password)
            log.info("attachment_id: %s", attachment_id)

            ##############################################
            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE #
            ##############################################

            yield StatusMessage("Finished 'utilities_attachment_zip_extract' that was running in workflow '{0}'".format(wf_instance_id))

            results = {
                "content": "xyz"
            }

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
