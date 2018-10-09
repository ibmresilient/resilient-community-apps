# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get file lists """

# Set up:
# Destination: a Queue named "amp_get_file_lists".
# Manual Action: Execute a REST query against a Cisco AMP for endpoints server.
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'amp_set_file_list_files' of package fn_cisco_amp4ep.

    The Function does a Cisco AMP for endpoints query operation takes the following parameter:
        amp_scd_name, amp_limit, amp_offset

    An example of a set of query parameter might look like the following:
            amp_scd_name = None
            amp_limit = None
            amp_offset = None

    The Investigate Query will executs a REST call against the Cisco Umbrell Investigate server and returns a result in
    JSON format similar to the following.
    {
     "file_lists": {    u'version': u'v1.2.0',
                        u'data': [{
                            u'guid': u'9710a198-b95a-462a-b184-9e688968fd94',
                            u'type': u'simple_custom_detections',
                            u'name': u'File Blacklist',
                                    u'links': {
                                        u'file_list': u'https://api.amp.cisco.com/v1/file_lists/9710a198-b95a-462a-b184-9e688968fd94'
                                    }
                                }
                            ],
                        u'metadata': {u'results': {
                                        u'index': 0,
                                        u'total': 1,
                                        u'items_per_page': 500,
                                        u'current_item_count': 1
                                     },
                                     u'links': {
                                                    u'self': u'https://api.amp.cisco.com/v1/file_lists/simple_custom_detections'
                                               }
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

    @function("fn_amp_get_file_lists")
    def _fn_amp_get_file_lists_function(self, event, *args, **kwargs):
        """Function: Returns a list of simple custom detection file lists. You can filter this list by name."""
        try:
            # Get the function parameters:
            amp_scd_name = kwargs.get("amp_scd_name")  # text
            amp_limit = kwargs.get("amp_limit")  # number
            amp_offset = kwargs.get("amp_offset")  # number

            log = logging.getLogger(__name__)
            log.info("amp_scd_name: %s", amp_scd_name)
            log.info("amp_limit: %s", amp_limit)
            log.info("amp_offset: %s", amp_offset)

            yield StatusMessage("Running Cisco AMP for endpoints get file lists ...")

            params = {"name": amp_scd_name, "limit": amp_limit, "offset": amp_offset  }

            validate_params(params)

            amp = Ampclient(self.options)

            rtn = amp.get_file_lists(**params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'file lists' results.")

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()