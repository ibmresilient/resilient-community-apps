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
from fn_cisco_amp4ep.lib.amp_ratelimit import AmpRateLimit

RATE_LIMITER = AmpRateLimit()

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
      "input_params": {"q": "SearchProtocolHost.exe", "limit": null, "offset": null},
      "query_execution_time": "2018-08-09 13:19:22",
      "query": "SearchProtocolHost.exe",
      "response": {
        {"version":"v1.2.0",
         "metadata":{
            "links":{"self": "https://api.amp.cisco.com/v1/computers/activity?q=SearchProtocolHost.exe"},
            "results":{"total":4, "current_item_count":4, "index":0, "items_per_page":500}
         },
         "data": [
                {"connector_guid": "0df31cae-120d-4fbc-ad7f-b0e7e96c01e5", "hostname": "Demo_Dyre", "active": true,
                    "links": {"computer": "https://api.amp.cisco.com/v1/computers/0df31cae-120d-4fbc-ad7f-b0e7e96c01e5",
                            "trajectory": "https://api.amp.cisco.com/v1/computers/0df31cae-120d-4fbc-ad7f-b0e7e96c01e5/trajectory?q=SearchProtocolHost.exe",
                            "group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}
                },
                {"connector_guid": "8c7c18d3-c1b4-4fa8-8d46-b6e467cdbae8", "hostname": "Demo_Upatre", "active": true,
                    "links": {"computer": "https://api.amp.cisco.com/v1/computers/8c7c18d3-c1b4-4fa8-8d46-b6e467cdbae8",
                            "trajectory": "https://api.amp.cisco.com/v1/computers/8c7c18d3-c1b4-4fa8-8d46-b6e467cdbae8/trajectory?q=SearchProtocolHost.exe",
                            "group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}
                },
                {"connector_guid": "ad29d359-dac9-4940-9c7e-c50e6d32ee6f", "hostname": "Demo_CozyDuke", "active": true,
                    "links": {"computer": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f",
                            '"trajectory": "https://api.amp.cisco.com/v1/computers/ad29d359-dac9-4940-9c7e-c50e6d32ee6f/trajectory?q=SearchProtocolHost.exe",
                            '"group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}
                },
                {"connector_guid": "af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01", "hostname": "WIN-S1AC1PI6L5L", "active": true,
                    "links": {"computer": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01",
                            "trajectory": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01/trajectory?q=SearchProtocolHost.exe",
                            "group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"}
                }
         ]
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
        """Function: Search all computers in Cisco AMP environment for any events or activities associated with a
        file or network operation, and returns computers matching that criteria."""
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

            amp = Ampclient(self.options, RATE_LIMITER)

            rtn = amp.get_paginated_total(amp.get_activity, **params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time, "input_params": params}
            yield StatusMessage("Returning 'activity' results for query '{}'.".format(params["q"]))

            log.debug(json.dumps(results))

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()