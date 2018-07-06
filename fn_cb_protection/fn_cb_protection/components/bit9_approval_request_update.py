# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_approval_request_update"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    @function("bit9_approval_request_update")
    def _bit9_approval_request_update_function(self, event, *args, **kwargs):
        """Function: Update an approval request"""
        try:
            # Get the function parameters:
            bit9_approval_request_id = kwargs.get("bit9_approval_request_id")  # number
            bit9_approval_request_resolution = kwargs.get("bit9_approval_request_resolution")  # number
            bit9_approval_request_resolution_comments = kwargs.get("bit9_approval_request_resolution_comments")  # text
            bit9_approval_request_status = kwargs.get("bit9_approval_request_status")  # number

            log = logging.getLogger(__name__)
            log.info("bit9_approval_request_id: %s", bit9_approval_request_id)
            log.info("bit9_approval_request_resolution: %s", bit9_approval_request_resolution)
            log.info("bit9_approval_request_resolution_comments: %s", bit9_approval_request_resolution_comments)
            log.info("bit9_approval_request_status: %s", bit9_approval_request_status)

            payload = {}
            if bit9_approval_request_resolution:
                payload["resolution"] = bit9_approval_request_resolution
            if bit9_approval_request_resolution_comments:
                payload["resolutionComments"] = bit9_approval_request_resolution_comments
            if bit9_approval_request_status:
                payload["status"] = bit9_approval_request_status

            self.bit9_client = CbProtectClient(self.options)
            results = self.bit9_client.update_approval_request(bit9_approval_request_id, payload)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()