# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'attachment_zip_extract"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("utility_functions", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("utility_functions", {})

    @function("attachment_zip_extract")
    def _attachment_zip_extract_function(self, event, *args, **kwargs):
        """Function: For a zipfile attachment, extract a file."""
        try:
            # Get the function parameters:
            incident_id = kwargs.get("incident_id")  # number
            attachment_id = kwargs.get("attachment_id")  # number
            file_path = kwargs.get("file_path")  # text
            zipfile_password = kwargs.get("zipfile_password")  # text

            log = logging.getLogger(__name__)
            log.info("incident_id: %s", incident_id)
            log.info("attachment_id: %s", attachment_id)
            log.info("file_path: %s", file_path)

            # PUT YOUR FUNCTION IMPLEMENTATION CODE HERE
            #  yield StatusMessage("starting...")
            #  yield StatusMessage("done...")

            # Produce a FunctionResult with the return value
            yield FunctionResult({"value": "xyz"})
        except Exception:
            yield FunctionError()