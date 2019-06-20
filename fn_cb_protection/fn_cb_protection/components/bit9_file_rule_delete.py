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
    """Component that implements Resilient function 'bit9_file_rule_delete"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    @function("bit9_file_rule_delete")
    def _bit9_file_rule_delete_function(self, event, *args, **kwargs):
        """Function: Delete a file rule"""
        try:
            validate_fields(["bit9_file_rule_id"], kwargs)
            # Get the function parameters:
            bit9_file_rule_id = kwargs.get("bit9_file_rule_id")  # number

            log.info(u"bit9_file_rule_id: %s", bit9_file_rule_id)

            bit9_client = CbProtectClient(self.options)
            results = bit9_client.delete_file_rule(bit9_file_rule_id)

            log.info("Done")
            log.debug(results)

            # Produce a FunctionResult with the results
            yield FunctionResult({"content": results})
        except Exception as err:
            log.error(err)
            yield FunctionError(err)
