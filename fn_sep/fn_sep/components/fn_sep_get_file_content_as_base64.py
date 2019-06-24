# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM query - get file content as base64. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST query against a SYMANTEC SEPM server.
import json
import logging
import base64

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.sep_client import Sepclient
from fn_sep.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_get_file_content_as_base64' of
    package fn_sep.

    The Function takes the following parameter:
            sep_file_id

    An example of a set of query parameter might look like the following:
            sep_file_id = 'D3FFC391A9FE9DC554E11DA825AE6805'

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        'inputs': {u'sep_file_id': u'D3FFC391A9FE9DC554E11DA825AE6805'},
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-14 14:18:25', 'package_version': '1.0.0',
                    'host': 'myhost',  'version': '1.0', 'execution_time_ms': 1215
                   },
        'success': True,
        'content': '<Bas64-string>',
        'raw': '"<Bas64-string>"',
        'reason': None,
        'version': '1.0'
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

    @function("fn_sep_get_file_content_as_base64")
    def _fn_sep_get_file_content_as_base64_function(self, event, *args, **kwargs):
        """Function: Get the contents of an uploaded binary file, in base64 format."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_file_id = kwargs.get("sep_file_id")  # text

            log = logging.getLogger(__name__)
            log.info("sep_file_id: %s", sep_file_id)

            validate_fields(["sep_file_id"], kwargs)

            yield StatusMessage("Running Symantec SEP Get File Content as Base64 ...")

            sep = Sepclient(self.options, params)

            rtn = base64.b64encode(sep.get_file_content(**params)).decode("utf-8")

            results = rp.done(True, rtn)

            yield StatusMessage("Returning 'Symantec SEP Get File Content as Base64' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
