# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get computers """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs
from datetime import datetime

CONFIG_DATA_SECTION = "fn_sep"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_fingerprint_list' of
    package fn_sep.

    The Function takes the following parameter:
            sep_domainid, sep_name, sep_id

    An example of a set of query parameter might look like the following:
            sep_domainid = None
            sep_name = None
            sep_id = None

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        "inputs": {"sep_domainid": null, "sep_name": null, "sep_id": null},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
                'host': 'myhost.ibm.com', 'version': '1.0', 'execution_time_ms': 1085},
        "success": True,
        "content": {
        },
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

    @function("fn_sep_get_fingerprint_list")
    def _func_symc_get_computers_function(self, event, *args, **kwargs):
        """Function: Get the file fingerprint list for a specified name or id as a set of hash values."""
        try:
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_domainid = kwargs.get("sep_domainid")  # text
            sep_name = kwargs.get("sep_name")  # text
            sep_body = kwargs.get("sep_id")  # text

            log = logging.getLogger(__name__)
            log.info("sep_domainid: %s", sep_domainid)
            log.info("sep_name: %s", sep_name)
            log.info("sep_id: %s", sep_body)

            yield StatusMessage("Running Symantec SEP Get file fingerprint list query...")

            if kwargs:
                transform_kwargs(kwargs)

            sep = Sepclient(self.options, kwargs)
            rtn = sep.get_fingerprint_list(sep.get_computers, **kwargs)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning Get file fingerprint list results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
