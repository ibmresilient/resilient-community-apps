# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints patch - move computer """

# Set up:
# Destination: a Queue named "amp_move_computer".
# Manual Action: Execute a REST move(patch) against a Cisco AMP for endpoints server.
import logging
import json
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params, is_none

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_move_computer"""

    def __init__(self, opts):
        """Component that implements Resilient function 'amp_move_computer' of package fn_cisco_amp4ep.

        The Function does a Cisco AMP for endpoints move(patch) operation and takes the following parameter:
            amp_conn_guid, amp_group_guid

        An example of a set of query parameter might look like the following:
                amp_conn_guid = "00da1a57-b833-43ba-8ea2-79a5ab21908f"
                amp_group_guid = "89663c44-f95e-4ee8-896d-7611744a6e9a"

    The function will execute a REST api patch request against a Cisco AMP for endpoints server and returns a result in
    JSON format similar to the following.

    {
          "input_params": {"conn_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
                           "group_guid": "89663c44-f95e-4ee8-896d-7611744a6e9a"},
          "response": {
            "version": "v1.2.0",
            "data": {
              "operating_system": "Windows 7, SP 1.0",
              "connector_guid": "00da1a57-b833-43ba-8ea2-79a5ab21908f",
              "links": {
                "trajectory": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f/trajectory",
                "computer": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f",
                "group": "https://api.amp.cisco.com/v1/groups/89663c44-f95e-4ee8-896d-7611744a6e9a"
              },
              "policy": {
                "guid": "a98a0f97-4d54-4175-9eef-b8dee9c8e74b",
                "name": "Audit"
              },
              "external_ip": "145.1.91.176",
              "group_guid": "89663c44-f95e-4ee8-896d-7611744a6e9a",
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
              "active": true
            },
            "metadata": {
              "links": {
                "self": "https://api.amp.cisco.com/v1/computers/00da1a57-b833-43ba-8ea2-79a5ab21908f"
              }
            }
          },
          "query_execution_time": "2018-10-08 15:22:26"
        }

        """
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_amp4ep", {})
        validate_opts(self)

    @function("fn_amp_move_computer")
    def _fn_amp_move_computer_function(self, event, *args, **kwargs):
        """Function: Move computer to a group with given connector guid and group guid."""
        try:
            # Get the function parameters:
            amp_conn_guid = kwargs.get("amp_conn_guid")  # text
            amp_group_guid = kwargs.get("amp_group_guid")  # text

            log = logging.getLogger(__name__)
            log.info("amp_conn_guid: %s", amp_conn_guid)
            log.info("amp_group_guid: %s", amp_group_guid)

            if is_none(amp_conn_guid):
                raise ValueError("Required parameter 'amp_conn_guid' not set.")
            if is_none(amp_group_guid):
                raise ValueError("Required parameter 'amp_group_guid' not set.")

            yield StatusMessage("Running Cisco AMP for endpoints get computer by guid query...")

            params = {"conn_guid": amp_conn_guid, "group_guid": amp_group_guid,}

            validate_params(params)

            amp = Ampclient(self.options)

            rtn = amp.move_computer(params["conn_guid"], params["group_guid"])
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "response" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time, "input_params": params}
            yield StatusMessage("Returning 'move computer' results for connector guid '{}' and new group guid '{}'."
                                .format(params["conn_guid"], params["group_guid"]))

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()