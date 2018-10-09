# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get event types """

# Set up:
# Destination: a Queue named "amp_get_event_types".
# Manual Action: Execute a REST query against a Cisco AMP for endpoints server.
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_get_event_types of package fn_cisco_amp4ep.
    The Function takes no parameters.

    The function will execute a REST api get request against a Cisco AMP for endpoints server and returns a result in JSON
    format similar to the following.

    {
      "response": {
        "version": "v1.2.0",
        "data": [
          {
            "description": "An agent has been told to fetch policy.",
            "id": 553648130,
            "name": "Policy Update"
          },
          {
            "description": "An agent has started scanning.",
            "id": 554696714,
            "name": "Scan Started"
          },
          {
            "description": "A scan has completed without detecting anything malicious.",
            "id": 554696715,
            "name": "Scan Completed, No Detections"
          },
          ...
          ...

        ],
        "metadata": {
          "results": {
            "total": 94
          },
          "links": {
            "self": "https://api.amp.cisco.com/v1/event_types"
          }
        }
      },
      "query_execution_time": "2018-10-08 16:27:32"
    }
    """
    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_amp4ep", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_amp4ep", {})

    @function("fn_amp_get_event_types")
    def _fn_amp_get_event_types_function(self, event, *args, **kwargs):
        """Function: Events are identified and filtered by a unique ID. Provides a human readable name, and short description of each event by ID."""
        try:
            # Get the function parameters:

            log = logging.getLogger(__name__)

            amp = Ampclient(self.options)

            yield StatusMessage("Running Cisco AMP get computers query...")
            rtn = amp.get_event_types()
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'event types' results")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()