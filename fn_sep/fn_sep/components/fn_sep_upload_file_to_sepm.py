# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
""" Resilient functions component to run a Symantec SEPM action - upload file to SEPM server. """

# Set up:
# Destination: a Queue named "fn_sep".
# Manual Action: Execute a REST action against a SYMANTEC SEPM server.
import json
import logging

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_sep.lib.sep_client import Sepclient
from fn_sep.lib.helpers import CONFIG_DATA_SECTION, transform_kwargs

LOG = logging.getLogger(__name__)

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_sep_upload_file_to_sepm' of
    package fn_sep.

    The Function takes the following parameter:
            sep_file_path, sep_computer_ids, sep_sha256, sep_sha1, sep_md5, sep_source

    An example of a set of query parameter might look like the following:
            sep_file_path = 'C:\\temp\\New Text Document.txt'
            sep_computer_ids = '89AD1BBB0946C25D25E6C0984E971D8A'
            sep_sha256 = '590f9895c2cbe93d47c3f7a3104fb843edfb5d5741330593d7d302a1e11e0ba5'
            sep_sha1 = None
            sep_md5 = None
            sep_source = 'FILESYSTEM'

    The function will execute a REST api get request against a SYMANTEC  SEPM server for information on endpoints and
    returns a result in JSON format similar to the following.

    {
        'inputs': {u'sep_sha256': u'590f9895c2cbe93d47c3f7a3104fb843edfb5d5741330593d7d302a1e11e0ba5', u'sep_source': u'FILESYSTEM',
                   u'sep_computer_ids': u'89AD1BBB0946C25D25E6C0984E971D8A', u'sep_file_path': u'C:\\temp\\New Text Document.txt',
                   u'sep_sha1': None, u'sep_md5': None
                   },
        'metrics': {'package': 'fn-sep', 'timestamp': '2019-05-14 14:46:08', 'package_version': '1.0.0',
                    'host': 'myhost', 'version': '1.0', 'execution_time_ms': 1226
                   }, 'success': True,
        'content': {u'commandID': u'1BFD8C9B3FD74FF4A2490FFE63314E7A'},
        'raw': '{"commandID": "1BFD8C9B3FD74FF4A2490FFE63314E7A"}',
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

    @function("fn_sep_upload_file_to_sepm")
    def _fn_sep_upload_file_to_sepm_function(self, event, *args, **kwargs):
        """Function: Upload suspicious file from endpoint back to SEPM server."""
        try:
            params = transform_kwargs(kwargs) if kwargs else {}
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

            validate_fields(["sep_file_path", "sep_computer_ids", "sep_source"], kwargs)

            yield StatusMessage("Running Symantec SEP Upload File to SEPM ...")

            sep = Sepclient(self.options, params)

            rtn = sep.upload_file(**params)

            results = rp.done(True, rtn)
            yield StatusMessage("Returning 'Symantec SEP Upload File to SEPM' results")

            log.debug(json.dumps(results["content"]))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            LOG.exception("Exception in Resilient Function for Symantec SEP.")
            yield FunctionError()
