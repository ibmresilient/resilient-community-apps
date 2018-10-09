# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get activity """

# Set up:
# Destination: a Queue named "amp_computers".
# Manual Action: Execute a REST query against a Cisco AMP for endpoints server.
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_get_activity' of
    package fn_cisco_amp4ep.

    The Function takes the following parameters:
        amp_q, amp_limit, amp_offset

    An example of a set of query parameter might look like the following:
            amp_q       = "SearchProtocolHost.exe"
            amp_limit   = None
            amp_offset  = None

    The function will execute a REST api get request against a Cisco AMP for endpoints server and returns a result in
    JSON format similar to the following.

    {
      "query_execution_time": "2018-08-09 13:19:22",
      "activity": {
        "version": "v1.2.0",
        "data": [],
        "metadata": {
          "results": {
            "index": 0,
            "total": 0,
            "items_per_page": 500,
            "current_item_count": 0
          },
          "links": {
            "self": "https://api.amp.cisco.com/v1/computers/activity?q=SearchProtocolHost.exe"
          }
        }
      }
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

    @function("fn_amp_get_activity")
    def _fn_amp_get_activity_function(self, event, *args, **kwargs):
        """Function: Search all computers in Cisco AMP environment for any events or activities associated with a file or network operation, and returns computers matching that criteria."""
        try:
            # Get the function parameters:
            amp_q = kwargs.get("amp_q")  # text
            amp_limit = kwargs.get("amp_limit")  # number
            amp_offset = kwargs.get("amp_offset")  # number

            log = logging.getLogger(__name__)
            log.info("amp_q: %s", amp_q)
            log.info("amp_limit: %s", amp_limit)
            log.info("amp_offset: %s", amp_offset)

            if is_none(amp_q):
                raise ValueError("Required parameter 'amp_q' not set.")

            yield StatusMessage("Running Cisco AMP for endpoints get activity...")

            params = {"q": amp_q, "limit": amp_limit, "offset": amp_offset}

            validate_params(params)

            amp = Ampclient(self.options)

            rtn = amp.get_activity(**params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'activity' results for query '{}'.".format(params["q"]))

            log.debug(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()