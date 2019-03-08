# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get fingerprint list """

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
    """Component that implements Resilient function 'fn_sep_add_fingerprint_list' of
    package fn_sep.

    The Function takes the following parameters:
            sep_data, sep_description, sep_domainid, sep_hashtype, sep_name

    An example of a set of query parameter might look like the following:
            sep_data = "Abcd"
            sep_description = "My fingerprint list"
            sep_domainid = "A9B4B7160946C25D24B6AA458EF5557F"
            sep_hashtype = {'name': 'SHA256', 'id': 261}
            sep_name = my_fp_list

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        "inputs": {"sep_domainid": "A9B4B7160946C25D24B6AA458EF5557F", "sep_hashtype": {'name': 'SHA256', 'id': 261,
        "sep_name": " my_fp_list"},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
        "host": 'myhost.ibm.com', 'version': '1.0', 'execution_time_ms': 1085},
        "success': True,
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

    @function("fn_sep_add_fingerprint_list")
    def _func_symc_get_computers_function(self, event, *args, **kwargs):
        """Function: Returns a list of computers with agents deployed on them. You can use parameters to narrow the search by IP address or hostname."""
        try:
            # Instantiate result payload object
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_data = kwargs.get("sep_data")  # text
            sep_description = kwargs.get("sep_description")  # text
            sep_domainid = kwargs.get("sep_domainid")  # text
            sep_hashtype = self.get_select_param(kwargs.get("sep_hashtype"))  # select, values: "SHA256", "MD5"
            sep_name = kwargs.get("sep_name")  # text

            log = logging.getLogger(__name__)
            log.info("sep_data: %s", sep_data)
            log.info("sep_description: %s", sep_description)
            log.info("sep_domainid: %s", sep_domainid)
            log.info("sep_hashtype: %s", sep_hashtype)
            log.info("sep_name: %s", sep_name)

            yield StatusMessage("Running Symantec SEP add fingerprint list action ...")

            if kwargs:
                transform_kwargs(kwargs)

            sep = Sepclient(self.options, kwargs)
            rtn = sep.add_fingerprint_list(**kwargs)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'add fingerprint list status' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
