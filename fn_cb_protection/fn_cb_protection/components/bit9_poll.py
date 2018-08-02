# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient, escape


class Bit9PollComponent(ResilientComponent):
    """Component that polls CarbonBlack Protection for new approval requests"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(Bit9PollComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    def _bit9_poll(self, event, *args, **kwargs):
        """Query CbProtection for any new approval requests"""
        #
        # We want to find approval requests that match our escalation criteria
        # By default this is "all unresolved approval requests"
        escalation_query = "resolution:0"

        # TODO all the rest
