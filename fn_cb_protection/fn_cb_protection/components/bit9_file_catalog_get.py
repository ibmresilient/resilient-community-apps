# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_file_catalog_get"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    @function("bit9_file_catalog_get")
    def _bit9_file_catalog_get_function(self, event, *args, **kwargs):
        """Function: Get a file catalog item by ID"""
        try:
            # Get the function parameters:
            bit9_file_catalog_id = kwargs.get("bit9_file_catalog_id")  # number

            log = logging.getLogger(__name__)
            log.info("bit9_file_catalog_id: %s", bit9_file_catalog_id)

            bit9_client = CbProtectClient(self.options)
            results = bit9_client.get_file_catalog(bit9_file_catalog_id)

            results["details_url"] = u"https://{}/file-details.php?antibody_id={}".format(
                bit9_client.server,
                bit9_file_catalog_id
            )
            log.info("Effective State :%s", results.get("effectiveState"))
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()