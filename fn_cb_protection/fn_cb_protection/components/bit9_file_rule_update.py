# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient
from resilient_lib import validate_fields


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
            validate_fields(["bit9_file_rule_id"], kwargs)
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
            log.info(u"bit9_file_rule_id: %s", bit9_file_rule_id)
            log.info(u"bit9_file_catalog_id: %s", bit9_file_catalog_id)
            log.info(u"bit9_file_rule_name: %s", bit9_file_rule_name)
            log.info(u"bit9_file_rule_description: %s", bit9_file_rule_description)
            log.info(u"bit9_file_rule_filestate: %s", bit9_file_rule_filestate)
            log.info(u"bit9_file_rule_sourcetype: %s", bit9_file_rule_sourcetype)
            log.info(u"bit9_file_rule_policyids: %s", bit9_file_rule_policyids)
            log.info(u"bit9_file_rule_hash: %s", bit9_file_rule_hash)

            # This can be called with a "file rule id", to update an existing rule.
            # Or, it can be called with no file rule id, to create a new rule for a hash or filename.

            if not (bit9_file_catalog_id and bit9_file_rule_name and bit9_file_rule_description and bit9_file_rule_filestate
                    and bit9_file_rule_sourcetype and bit9_file_rule_hash and bit9_file_rule_policyids):
                raise FunctionError("Specify at least one attribute to update: bit9_file_catalog_id, bit9_file_rule_name, \
bit9_file_rule_description, bit9_file_rule_filestate, bit9_file_rule_sourcetype, bit9_file_rule_hash or bit9_file_rule_policyids")

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

            bit9_client = CbProtectClient(self.options)
            results = bit9_client.update_file_rule(bit9_file_rule_id, payload)

            log.info("Done")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            log.error(err)
            yield FunctionError(err)
