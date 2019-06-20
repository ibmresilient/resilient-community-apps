# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cb_protection.util.bit9_client import CbProtectClient, escape
from resilient_lib import validate_fields

log = logging.getLogger(__name__)


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'bit9_approval_request_query"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts["fn_cb_protection"]

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts["fn_cb_protection"]

    @function("bit9_approval_request_query")
    def _bit9_approval_request_query_function(self, event, *args, **kwargs):
        """Function: Return approval requests that match the given criteria."""
        try:
            validate_fields(["bit9_query"], kwargs)
            # Get the function parameters:
            bit9_query = kwargs.get("bit9_query")  # text

            log.info(u"bit9_query: %s", bit9_query)

            # Query example: 'id:6' (see https://<server>/api/bit9platform/v1 for details)
            bit9_client = CbProtectClient(self.options)
            results = bit9_client.query_approval_request(bit9_query)

            # Query results should be a list
            if isinstance(results, list):
                log.info("%d results", len(results))
                results = {
                    "count": len(results),
                    "items": results
                }
                log.debug(results)
            else:
                log.warn(u"Expected a list but received:")
                log.warn(results)

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception as err:
            log.error(err)
            yield FunctionError(err)
