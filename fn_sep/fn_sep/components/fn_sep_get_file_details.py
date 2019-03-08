# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_sep.lib.sep_client import Sepclient
from resilient_lib import ResultPayload
from fn_sep.lib.helpers import transform_kwargs

CONFIG_DATA_SECTION = "fn_sep"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_file_details' of
    package fn_sep.

    The Function takes the following parameter:
            sep_file_id

    An example of a set of query parameter might look like the following:
            sep_file_id =

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        'inputs': {'sep_file_id': null},
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-03-01 12:46:27', 'package_version': '1.0.0',
                'host': 'johns-mbp-2.galway.ie.ibm.com', 'version': '1.0', 'execution_time_ms': 1085},
        'success': True,
        'content': {
        },
        "raw": '<<a string representation of content.>>',
        "reason": None, 'version': '1.0'
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_sep", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_sep", {})

    @function("fn_sep_get_file_details")
    def _fn_sep_quarantine_file_function(self, event, *args, **kwargs):
        """Function: Get the details of a binary file, such as the checksum and the file size."""
        try:
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_file_id = kwargs.get("sep_file_id")  # text

            log = logging.getLogger(__name__)
            log.info("sep_file_id: %s", sep_file_id)

            yield StatusMessage("Running Symantec SEP Get File Details ...")
            if kwargs:
                transform_kwargs(kwargs)

            sep = Sepclient(self.options, kwargs)

            rtn = sep.get_file_details(**kwargs)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning file details' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
