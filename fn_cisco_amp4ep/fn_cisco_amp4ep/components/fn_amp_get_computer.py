# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get computer """

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
    """Component that implements Resilient function 'fn_amp_get_computer' of
    package fn_cisco_amp4ep.

    The Function takes the following parameter:
        amp_conn_guid

    An example of a set of query parameter might look like the following:
            amp_conn_guid = "00da1a57-b833-43ba-8ea2-79a5ab21908f"

    The function will execute a REST api get request against a Cisco AMP for endpoints server and returns a result in
    JSON format similar to the following.

    {
      "input_params": {"conn_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f"},
      "response": {
        "version": "v1.2.0",
        "data": {
          "operating_system": "Windows 7, SP 1.0",
          "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
          "links": {
            "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
            "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
            "group": "https://api.amp.cisco.com/v1/groups/9d55c259-c960-488b-9b2d-06478fa19ee4"
          },
          "external_ip": "145.1.91.176",
          "group_guid": "9d55c259-c960-488b-9b2d-06478fa19ee4",
          "hostname": "Demo_AMP",
          "install_date": "2018-05-22T16:53:27Z",
          "network_addresses": [
            {
              "ip": "255.240.221.92",
              "mac": "a0:28:f5:c3:71:d5"
            }
          ],
          "connector_version": "6.0.9.10685",
          "internal_ips": [
            "255.240.221.92"
          ],
          "policy": {
            "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
            "name": "Audit"
          },
          "active": true,
          "last_seen": "2018-05-22T16:53:27Z"
        },
        "metadata": {
          "links": {
            "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"
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

    @function("fn_amp_get_computer")
    def _fn_amp_get_computer_function(self, event, *args, **kwargs):
        """Function: Returns a  computer with an agent deployed on them by connector guid."""
        try:
            # Get the function parameters:
            amp_conn_guid = kwargs.get("amp_conn_guid")  # text

            log = logging.getLogger(__name__)
            log.info("amp_conn_guid: %s", amp_conn_guid)

            if is_none(amp_conn_guid):
                raise ValueError("Required parameter 'amp_conn_guid' not set.")

            yield StatusMessage("Running Cisco AMP for endpoints get computer by guid query...")

            params = {"conn_guid": amp_conn_guid}

            validate_params(params)

            amp = Ampclient(self.options, RATE_LIMITER)

            rtn = amp.get_computer(amp_conn_guid)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time, "input_params": params}
            yield StatusMessage("Returning 'computer by guid' results for guid '{}'.".format(params["conn_guid"]))

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()