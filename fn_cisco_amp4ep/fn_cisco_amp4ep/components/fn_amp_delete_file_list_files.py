## -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - delete file lists files """

# Set up:
# Destination: a Queue named "amp_delete_file_list_files".
# Manual Action: Execute a REST delete operation against a Cisco AMP for endpoints server
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'amp_delete_file_list_files' of
    package fn_cisco_amp4ep.

    The Function does a Cisco AMP for endpoints delete operation takes the following parameter:
        amp_file_list_guid, amp_file_sha256


    An example of a set of query parameter might look like the following:
            amp_file_list_guid = "e773a9eb-296c-40df-98d8-bed46322589d"
            amp_file_sha256 = "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284"

    The Investigate Query will executs a REST call against the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.
    {
     "delete_file_list_files": {u'version': u'v1.2.0',
                                u'data': {},
                                u'metadata': {u'links': {
                                                u'self': u'https://api.amp.cisco.com/v1/file_lists/e773a9eb-296c-40df-98d8-bed46322589d/files/4ce4e7ab22a8900bf438ff84baebe74d3ef3828a716b933b6e2a85b991b36f31'}
                                             }
                                },
      "query_execution_time": "2018-08-09 11:56:02"
    }
    """
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

    @function("fn_amp_delete_file_list_files_by_sha256")
    def _fn_amp_delete_file_list_files_by_sha256_function(self, event, *args, **kwargs):
        """Function: Delete file list item with a given SHA-256 and associated to file list with given file_list_guid."""
        try:
            # Get the function parameters:
            amp_file_list_guid = kwargs.get("amp_file_list_guid")  # text
            amp_sha256 = kwargs.get("amp_sha256")  # text

            log = logging.getLogger(__name__)
            log.info("amp_file_list_guid: %s", amp_file_list_guid)
            log.info("amp_sha256: %s", amp_sha256)

            yield StatusMessage("Running Cisco AMP for endpoints delete file lists files by guid and sha256...")

            params = {"file_list_guid": amp_file_list_guid, "sha256": amp_sha256}

            validate_params(params)

            amp = Ampclient(self.options)

            rtn = amp.delete_file_list_files(**params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": json.loads(json.dumps(rtn)),"query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'file lists files' results for guid '{}' and sha256 value '{}'."
                                .format(params["file_list_guid"], params["sha256"]))

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))


            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()