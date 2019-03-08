# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.helpers import transform_kwargs
from os import path

CONFIG_DATA_SECTION = "fn_sep"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_scan_endpoints' of package fn_sep.

    The Function takes the following parameter:
        sep_policy_type, sep_domainid

    An example of a set of query parameter might look like the following:
            sep_policy_type = fw
            sep_domainid = None

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

    @function("fn_sep_scan_endpoints")
    def _fn_sep_scan_endpoints_function(self, event, *args, **kwargs):
        """Function: Run a Evidence of Compromise (EOC) scan on Symantec Endpoint Protection endpoints."""
        try:
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_group_ids = kwargs.get("sep_group_ids")  # text
            sep_computer_ids = kwargs.get("sep_computer_ids")  # text
            sep_scan_type = self.get_select_param(kwargs.get("sep_scan_type"))  # select, values: "FULL_SCAN"
            sep_file_name = kwargs.get("sep_file_path")  # text
            sep_sha256 = kwargs.get("sep_sha256")  # text
            sep_description = kwargs.get("sep_description")  # text

            log = logging.getLogger(__name__)
            log.info("sep_group_ids: %s", sep_group_ids)
            log.info("sep_computer_ids: %s", sep_computer_ids)
            log.info("sep_scan_type: %s", sep_scan_type)
            log.info("sep_file_path: %s", sep_file_name)
            log.info("sep_sha256: %s", sep_sha256)
            log.info("sep_description: %s", sep_description)

            validate_fields(["sep_group_ids", "sep_computer_ids", "sep_scan_type",
                             "sep_file_path", "sep_sha256", "sep_description"], kwargs)

            yield StatusMessage("Running Symantec SEP scan endpoints command...")

            if kwargs:
                transform_kwargs(kwargs)
            sep = Sepclient(self.options, kwargs)

            rtn = sep.scan_endpoints(**kwargs)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'scan endpoints' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
