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

CONFIG_DATA_SECTION = "fn_sep"

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_upload_file_to_sepm' of
    package fn_sep.

    The Function takes the following parameter:
            sep_file_path, sep_computer_ids, sep_sha256, sep_sha1, sep_md5, sep_source

    An example of a set of query parameter might look like the following:
            sep_file_path    =
            sep_computer_ids =
            sep_sha256
            sep_sha1
            sep_md5
            sep_source

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
      "input_params": {},
      "query_execution_time": "2018-08-09 12:34:15",
      "content": {
      }
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

    @function("fn_sep_upload_file_to_sepm")
    def _fn_sep_quarantine_file_function(self, event, *args, **kwargs):
        """Function: Upload suspicious file from endpoint back to SEPM server."""
        try:
            # Instantiate result payload object.
            rp = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            # Get the function parameters:
            sep_file_path = kwargs.get("sep_file_path")  # text
            sep_computer_ids = kwargs.get("sep_computer_ids")  # text
            sep_sha256 = kwargs.get("sep_sha256")  # text
            sep_sha1 = kwargs.get("sep_sha1")  # text
            sep_md5 = kwargs.get("sep_md5")  # text
            sep_source = kwargs.get("sep_source")  # text

            log = logging.getLogger(__name__)
            log.info("sep_file_path: %s", sep_file_path)
            log.info("sep_computer_ids: %s", sep_computer_ids)
            log.info("sep_sha256: %s", sep_sha256)
            log.info("sep_sha1: %s", sep_sha1)
            log.info("sep_md5: %s", sep_md5)
            log.info("sep_source: %s", sep_source)

            validate_fields(["sep_file_path", "sep_computer_ids", "sep_sha256", "sep_source"], kwargs)

            yield StatusMessage("Running Symantec SEP - Upload file to SEPM ...")
            if kwargs:
                transform_kwargs(kwargs)

            sep = Sepclient(self.options, kwargs)

            rtn = sep.upload_file(**kwargs)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Upload file to SEPM' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
