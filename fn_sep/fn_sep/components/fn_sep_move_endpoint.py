# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM update - move client """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST update against a SYMANTEC SEPM server.import json
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_move_endpoint' of package fn_sep.

    The Function takes the following parameter:
            sep_hardwarekey, sep_group_id'

    An example of a set of query parameter might look like the following:
            sep_hardwarekey = "DC7D24D6465566D2941F35BC8D17801E"
            sep_group_id' = "8E20F39B0946C25D118925C2E28C2D59"

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.
    {
        "inputs": {'sep_hardwarekey': 'DC7D24D6465566D2941F35BC8D17801E', 'sep_group_id': '8E20F39B0946C25D118925C2E28C2D59'},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-07 11:39:14', 'package_version': '1.0.0',
        "host": 'myhost.ibm.com', 'version': '1.0', 'execution_time_ms': 9555},
        "success": True,
        "content": [{'responseMessage': 'OK', 'responseCode': '200'}],
        "raw": '<<a string representation of content.>>',
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

    @function("fn_sep_move_endpoint")
    def _fn_sep_move_endpoint_function(self, event, *args, **kwargs):
        """Function: Checks and moves a client computer to a specified group."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_group_id = kwargs.get("sep_group_id")  # text
            sep_hardwarekey = kwargs.get("sep_hardwarekey")  # text

            log = logging.getLogger(__name__)
            log.info("sep_group_id: %s", sep_group_id)
            log.info("sep_hardwarekey: %s", sep_hardwarekey)

            validate_fields(["sep_group_id", "sep_hardwarekey"], kwargs)

            yield StatusMessage("Running Symantec SEP move endpoint action...")

            sep = Sepclient(self.options, params)
            rtn = sep.move_endpoint(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning move endpoint results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()