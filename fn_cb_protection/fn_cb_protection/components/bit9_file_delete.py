# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

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

    @function("bit9_file_delete")
    def _bit9_file_delete_function(self, event, *args, **kwargs):
        """Function: Delete a file from all systems or a specific system"""
        try:
            # Get the function parameters:
            StatusMessage("Deleting file...")
            bit9_file_action = kwargs.get("bit9_file_action")  # number
            if bit9_file_action is None:
                raise FunctionError("bit9_file_action must be set to run this function.")

            bit9_computer_id = kwargs.get("bit9_computer_id")  # number
            if bit9_computer_id is None:
                raise FunctionError("bit9_computer_id must be set in order to run this function.")

            bit9_file_catalog_id = kwargs.get("bit9_file_catalog_id")  # number
            bit9_file_hash = kwargs.get("bit9_file_hash")  # text
            bit9_file_name = kwargs.get("bit9_file_name")  # text
            if not bit9_file_catalog_id and not bit9_file_hash and not bit9_file_name:
                raise FunctionError("bit9_file_catalog_id, bit9_file_hash, or bit9_file_name mush be set in order to "
                                    "run this function.")

            log = logging.getLogger(__name__)
            log.info("bit9_file_action: %s", bit9_file_action)
            log.info("bit9_computer_id: %s", bit9_computer_id)
            log.info("bit9_file_catalog_id: %s", bit9_file_catalog_id)
            log.info("bit9_file_hash: %s", bit9_file_hash)
            log.info("bit9_file_name: %s", bit9_file_name)

            payload = {}
            if bit9_file_catalog_id:
                payload["fileCatalogId"] = bit9_file_catalog_id
            if bit9_computer_id:
                payload["computerId"] = bit9_computer_id
            if bit9_file_action:
                payload["action"] = bit9_file_action
            if bit9_file_hash:
                payload["hash"] = bit9_file_hash
            if bit9_file_name:
                payload["fileName"] = bit9_file_name

            bit9_client = CbProtectClient(self.options)
            results = bit9_client.delete_file(payload)

            log.info("Done")
            StatusMessage("File deleted...")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as e:
            yield FunctionError(e)
