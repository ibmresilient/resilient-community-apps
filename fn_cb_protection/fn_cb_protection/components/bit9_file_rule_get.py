# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_file_rule_get"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    @function("bit9_file_rule_get")
    def _bit9_file_rule_get_function(self, event, *args, **kwargs):
        """Function: Get a file rule by ID"""
        try:
            # Get the function parameters:
            bit9_file_rule_id = kwargs.get("bit9_file_rule_id")  # number

            log = logging.getLogger(__name__)
            log.info("bit9_file_rule_id: %s", bit9_file_rule_id)

            self.bit9_client = CbProtectClient(self.options)
            results = self.bit9_client.get_file_rule(bit9_file_rule_id)

            log.info("Done")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()