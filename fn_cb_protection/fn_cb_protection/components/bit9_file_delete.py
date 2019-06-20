# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient
from resilient_lib import validate_fields

log = logging.getLogger(__name__)


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
            validate_fields(["bit9_file_action"], kwargs)
            # Get the function parameters:
            yield StatusMessage("Deleting file...")
            bit9_file_action = self.get_select_param(kwargs.get("bit9_file_action"))  # select
            bit9_computer_id = kwargs.get("bit9_computer_id")  # number

            bit9_file_catalog_id = kwargs.get("bit9_file_catalog_id")  # number
            bit9_file_hash = kwargs.get("bit9_file_hash")  # text
            bit9_file_name = kwargs.get("bit9_file_name")  # text
            if not bit9_file_catalog_id and not bit9_file_hash and not bit9_file_name:
                raise FunctionError("bit9_file_catalog_id, bit9_file_hash, or bit9_file_name mush be set in order to "
                                    "run this function.")

            log.info("bit9_file_action: %s", bit9_file_action)
            log.info("bit9_computer_id: %s", bit9_computer_id)
            log.info("bit9_file_catalog_id: %s", bit9_file_catalog_id)
            log.info("bit9_file_hash: %s", bit9_file_hash)
            log.info("bit9_file_name: %s", bit9_file_name)

            # Supported file actions
            supported_file_actions = {
                "DeleteFileByName": 8,
                "DeleteFileByHash": 9
            }

            payload = {}
            if bit9_file_catalog_id:
                payload["fileCatalogId"] = bit9_file_catalog_id
            if bit9_computer_id is not None:
                payload["computerId"] = bit9_computer_id
            if bit9_file_action in supported_file_actions:
                payload["action"] = supported_file_actions.get(bit9_file_action)
            else:
                raise FunctionError(u"{} is not one of the support file actions: {}".format(bit9_file_name,
                                                                                           list(supported_file_actions
                                                                                                .keys())))
            if bit9_file_hash:
                payload["hash"] = bit9_file_hash
            if bit9_file_name:
                payload["fileName"] = bit9_file_name

            log.debug("uPayload: {}".format(payload))
            bit9_client = CbProtectClient(self.options)
            results = bit9_client.delete_file(payload)

            log.info("Done")
            yield StatusMessage("File deleted...")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            log.error(err)
            yield FunctionError(err)

