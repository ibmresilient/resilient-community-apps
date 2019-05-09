# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_quarantine_endpoints' of package fn_sep.

    The Function takes the following parameter:
            sep_group_ids, sep_computer_ids, sep_undo

    An example of a set of query parameter might look like the following:
            sep_group_ids =
            sep_computer_ids =
            sep_undo =

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.
    {
        "inputs": {'sep_group_ids': 'DC7D24D6465566D2941F35BC8D17801E', 'sep_group_id': '8E20F39B0946C25D118925C2E28C2D59',
                   'sep_undo' = null},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-07 11:39:14', 'package_version': '1.0.0',
        "host": 'myhost.ibm.com', 'version': '1.0', 'execution_time_ms': 9555},
        "success": True,
        "content": {
         }
        "raw": '',
        "reason": None, 'version': '1.0'
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get(CONFIG_DATA_SECTION, {})

    @function("fn_sep_quarantine_endpoints")
    def _fn_sep_quarantine_endpoints_function(self, event, *args, **kwargs):
        """Function: Quarantine/unquarantine Symantec Endpoint Protection endpoints."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_group_ids = kwargs.get("sep_group_ids")  # text
            sep_computer_ids = kwargs.get("sep_computer_ids")  # text
            sep_undo = kwargs.get("sep_undo")  # boolean

            log = logging.getLogger(__name__)
            log.info("sep_group_ids: %s", sep_group_ids)
            log.info("sep_computer_ids: %s", sep_computer_ids)
            log.info("sep_undo: %s", sep_undo)

            validate_fields(["sep_undo"], kwargs)

            yield StatusMessage("Running Symantec SEP Quarantine endpoint or group...")

            sep = Sepclient(self.options, params)

            rtn = sep.quarantine_endpoints(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning Symantec SEP Quarantine endpoint or group results")

            import json
            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
