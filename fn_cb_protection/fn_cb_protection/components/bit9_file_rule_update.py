# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_file_rule_update"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    @function("bit9_file_rule_update")
    def _bit9_file_rule_update_function(self, event, *args, **kwargs):
        """Function: Create or update a File Rule"""
        try:
            # Get the function parameters:
            bit9_file_rule_id = kwargs.get("bit9_file_rule_id")  # number
            bit9_file_catalog_id = kwargs.get("bit9_file_catalog_id")  # number
            bit9_file_rule_name = kwargs.get("bit9_file_rule_name")  # text
            bit9_file_rule_description = kwargs.get("bit9_file_rule_description")  # text
            bit9_file_rule_filestate = kwargs.get("bit9_file_rule_filestate")  # number
            bit9_file_rule_sourcetype = kwargs.get("bit9_file_rule_sourcetype")  # number
            bit9_file_rule_policyids = kwargs.get("bit9_file_rule_policyids")  # text
            bit9_file_rule_hash = kwargs.get("bit9_file_rule_hash")  # text

            log = logging.getLogger(__name__)
            log.info("bit9_file_rule_id: %s", bit9_file_rule_id)
            log.info("bit9_file_catalog_id: %s", bit9_file_catalog_id)
            log.info("bit9_file_rule_name: %s", bit9_file_rule_name)
            log.info("bit9_file_rule_description: %s", bit9_file_rule_description)
            log.info("bit9_file_rule_filestate: %s", bit9_file_rule_filestate)
            log.info("bit9_file_rule_sourcetype: %s", bit9_file_rule_sourcetype)
            log.info("bit9_file_rule_policyids: %s", bit9_file_rule_policyids)
            log.info("bit9_file_rule_hash: %s", bit9_file_rule_hash)

            # This can be called with a "file rule id", to update an existing rule.
            # Or, it can be called with no file rule id, to create a new rule for a hash or filename.

            payload = {}
            if bit9_file_catalog_id:
                payload["fileCatalogId"] = bit9_file_catalog_id
            if bit9_file_rule_name:
                payload["name"] = bit9_file_rule_name
            if bit9_file_rule_description:
                payload["description"] = bit9_file_rule_description
            if bit9_file_rule_filestate:
                payload["fileState"] = bit9_file_rule_filestate
            if bit9_file_rule_sourcetype:
                payload["sourceType"] = bit9_file_rule_sourcetype
            if bit9_file_rule_policyids:
                payload["policyIds"] = bit9_file_rule_policyids
            if bit9_file_rule_hash:
                payload["hash"] = bit9_file_rule_hash

            self.bit9_client = CbProtectClient(self.options)
            results = self.bit9_client.update_file_rule(bit9_file_rule_id, payload)

            log.info("Done")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()