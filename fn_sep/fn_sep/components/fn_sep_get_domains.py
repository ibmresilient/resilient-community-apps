# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get domains. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"
LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_domains' of
    package fn_sep.

    The Function takes the following parameter:
        None

    An example of a set of query parameter might look like the following:


    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        "inputs": {},
        "metrics": {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
                'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1085},
        "success": True,
        "content": {
            [
              {
                "enable": true,
                "description": null,
                "administratorCount": 1,
                "companyName": "",
                "createdTime": 1548481071820,
                "contactInfo": null,
                "id": "908090000946C25D330E919313D23887",
                "name": "Default"
              },
              {
                "enable": true,
                "description": null,
                "administratorCount": 1,
                "companyName": "Resilient",
                "createdTime": 1550680668947,
                "contactInfo": "",
                "id": "A9B4B7160946C25D24B6AA458EF5557F",
                "name": "JP_test_Domain"
              }
            ]
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

    @function("fn_sep_get_domains")
    def _fn_sep_get_domains_function(self, event, *args, **kwargs):
        """Function: Gets a list of all accessible domains."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}

            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:

            log = logging.getLogger(__name__)

            yield StatusMessage("Running Symantec SEP Get Domains query...")

            sep = Sepclient(self.options, params)
            rtn = sep.get_domains(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Get Domains' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
