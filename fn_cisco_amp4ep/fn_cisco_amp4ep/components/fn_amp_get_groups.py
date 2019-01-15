# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get groups """

# Set up:
# Destination: a Queue named "amp_get_groups".
# Manual Action: Execute a REST query against a Cisco AMP for endpoints server.
import logging
import json
from datetime import datetime
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params
from fn_cisco_amp4ep.lib.amp_ratelimit import AmpRateLimit

RATE_LIMITER = AmpRateLimit()

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_get_groups' of package fn_cisco_amp4ep.
    The function can be used to query to get information on groups or individual group by group_guid.

    The Function takes the following parameter:
        amp_group_guid, amp_group_name, amp_limit

        An example of a set of query parameter might look like the following:
                amp_group_guid = None
                amp_group_name = None
                amp_limit      = None

    The function will execute a REST api get request against a Cisco AMP for endpoints server and returns a result in
    JSON format similar to the following.

    {
      "input_params": {"group_guid": null, "limit": null, "name": null},
      "response": {
        "version": "v1.2.0",
        "data": [
          {
            "source": null,
            "guid": "abcd1234-a123-b456-c769-abcdef123456",
            "name": "Audit",
            "links": {
              "group": "https://api.amp.cisco.com/v1/groups/abcd1234-a123-b456-c769-abcdef123456"
            },
            "description": "Test Audit Group 1"
          },
          {
            "source": null,
            "guid": "abcd1234-a123-b456-c769-abcdef123457",
            "name": "Domain Controller",
            "links": {
              "group": "https://api.amp.cisco.com/v1/groups/abcd1234-a123-b456-c769-abcdef123457"
            },
            "description": "Test Domain Controller Group 2"
          },
          {
            "source": null,
            "guid": "abcd1234-a123-b456-c769-abcdef123458",
            "name": "Protect",
            "links": {
              "group": "https://api.amp.cisco.com/v1/groups/abcd1234-a123-b456-c769-abcdef123458"
            },
            "description": "Test Protect Group 3"
          },
          ...
        ],
        "metadata": {
          "results": {
            "index": 0,
            "total": 5,
            "items_per_page": 500,
            "current_item_count": 5
          },
          "links": {
            "self": "https://api.amp.cisco.com/v1/groups"
          }
        }
      },
      "query_execution_time": "2018-10-08 12:49:38"
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

    @function("fn_amp_get_groups")
    def _fn_amp_get_groups_function(self, event, *args, **kwargs):
        """Function: Returns information on group or groups."""
        try:
            # Get the function parameters:
            amp_group_guid = kwargs.get("amp_group_guid")  # text
            amp_group_name = kwargs.get("amp_group_name")  # text
            amp_limit = kwargs.get("amp_limit")  # number

            log = logging.getLogger(__name__)
            log.info("amp_group_guid: %s", amp_group_guid)
            log.info("amp_group_name: %s", amp_group_name)
            log.info("amp_limit: %s", amp_limit)

            yield StatusMessage("Running Cisco AMP get groups query...")

            params = {"group_guid": amp_group_guid, "name": amp_group_name, "limit": amp_limit}

            validate_params(params)

            amp = Ampclient(self.options, RATE_LIMITER)

            rtn = amp.get_paginated_total(amp.get_groups, **params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time, "input_params": params}
            yield StatusMessage("Returning 'group' or 'groups' results for group_guid '{}', group name '{}' and limit '{}'"
                                .format(params["group_guid"], params["name"], params["limit"]))

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()