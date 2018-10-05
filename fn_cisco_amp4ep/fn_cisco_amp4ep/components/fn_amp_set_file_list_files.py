# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - set file list files """

# Set up:
# Destination: a Queue named "amp_set_file_list_files".
# Manual Action: Execute a REST post operation against a Cisco AMP for endpoints server.
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_set_file_list_files_by_sha256"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @function("fn_amp_set_file_list_files_by_sha256")
    def _fn_amp_set_file_list_files_by_sha256_function(self, event, *args, **kwargs):
        """Function: Add a SHA-256 to a file list using file_list_guid."""
        try:
            # Get the function parameters:
            amp_file_list_guid = kwargs.get("amp_file_list_guid")  # text
            amp_sha256 = kwargs.get("amp_sha256")  # text
            amp_file_description = kwargs.get("amp_file_description")  # text

            log = logging.getLogger(__name__)
            log.info("amp_file_list_guid: %s", amp_file_list_guid)
            log.info("amp_sha256: %s", amp_sha256)
            log.info("amp_file_description: %s", amp_file_description)

            yield StatusMessage("Running Cisco AMP for endpoints set file lists file by guid and sha256 ...")

            params = {"file_list_guid": amp_file_list_guid, "sha256": amp_sha256,
                      "file_description": amp_file_description }

            validate_params(params)

            amp = Ampclient(self.options)

            rtn = amp.set_file_list_files(**params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"file_lists_files": rtn,"query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'file lists files' results for guid '{}' and sha256 value '{}'."
                                .format(params["file_list_guid"], params["sha256"]))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()