# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

""" Resilient functions component to run a Cisco AMP for endpoints query - get events """

# Set up:
# Destination: a Queue named "amp_get_events".
# Manual Action: Execute a REST query against a Cisco AMP for endpoints server.
import json
import logging
from datetime import datetime

from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from fn_cisco_amp4ep.lib.amp_client import Ampclient
from fn_cisco_amp4ep.lib.helpers import validate_opts, validate_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_get_events of package fn_cisco_amp4ep.

    The Function takes the following parameters:
            amp_detection_sha256, amp_application_sha256, amp_conn_guid, amp_group_guid, amp_start_date,
            amp_event_type, amp_limit, amp_offset

    An example of a set of query parameter might look like the following:
            amp_detection_sha256    = None
            amp_application_sha256  = None
            amp_conn_guid           = None
            amp_group_guid          = None
            amp_start_date          = None
            amp_event_type          = None
            amp_limit               = None
            amp_offset              = None

    The function will execute a REST api request against a Cisco AMP for endpoints server and returns a result in JSON
    format similar to the following.

    {
      "response": {
        "version": "v1.2.0",
        "data": [
          {
            "id": 6455442249407791000,
            "timestamp": 1503024774,
            "timestamp_nanoseconds": 98000000,
            "date": "2017-08-18T02:52:54+00:00",
            "event_type": "Threat Detected",
            "event_type_id": 1090519054,
            "detection": "benign_qa_testware7",
            "detection_id": "6455442249407791109",
            "group_guids": [
              "b077d6bc-bbdf-42f7-8838-a06053fbd98a"
            ],
            "computer": {
              "connector_guid": "af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01",
              "hostname": "WIN-S1AC1PI6L5L",
              "external_ip": "10.200.65.31",
              "user": "johndoe@WIN-S1AC1PI6L5L",
              "active": true,
              "network_addresses": [
                {
                  "ip": "10.0.2.15",
                  "mac": "08:00:27:85:28:61"
                }
              ],
              "links": {
                "computer": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01",
                "trajectory": "https://api.amp.cisco.com/v1/computers/af73d9d5-ddc5-4c93-9c6d-d5e6b5c5eb01/trajectory",
                "group": "https://api.amp.cisco.com/v1/groups/b077d6bc-bbdf-42f7-8838-a06053fbd98a"
              }
            },
            "file": {
              "disposition": "Unknown",
              "file_name": "file.zip",
              "file_path": "\\\\?\\C:\\Users\\johndoe\\Downloads\\file.zip",
              "identity": {
                "sha256": "f8a6a244138cb1e2f044f63f3dc42beeb555da892bbd7a121274498cbdfc9ad5",
                "sha1": "20eeee16345e0c1283f7b500126350cb938b8570",
                "md5": "6853839cde69359049ae6f7bd3ae86d7"
              },
              "archived_file": {
                "disposition": "Malicious",
                "identity": {
                  "sha256": "46679a50632d05b99683a14b91a69ce908de1673fbb71e9cd325e5685fcd7e49"
                }
              },
              "parent": {
                "process_id": 3416,
                "disposition": "Clean",
                "file_name": "explorer.exe",
                "identity": {
                  "sha256": "80ef843fa78c33b511394a9c7535a9cbace1deb2270e86ee4ad2faffa5b1e7d2",
                  "sha1": "ea97227d34b8526055a543ade7d18587a927f6a3",
                  "md5": "15bc38a7492befe831966adb477cf76f"
                }
              }
            }
          },
          ...
          ...
        ],
        "metadata": {
          "results": {
            "index": 0,
            "total": 0,
            "items_per_page": 500,
            "current_item_count": 0
          },
          "links": {
            "self": "https://api.amp.cisco.com/v1/events"
          }
        }
      },
      "query_execution_time": "2018-10-09 11:05:12"
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

    @function("fn_amp_get_events")
    def _fn_amp_get_events_function(self, event, *args, **kwargs):
        """Function: Returns a  list of events."""
        try:
            # Get the function parameters:
            amp_detection_sha256 = kwargs.get("amp_detection_sha256")  # text
            amp_application_sha256 = kwargs.get("amp_application_sha256")  # text
            amp_conn_guid = kwargs.get("amp_conn_guid")  # text
            amp_group_guid = kwargs.get("amp_group_guid")  # text
            amp_start_date = kwargs.get("amp_start_date")  # datetimepicker
            amp_event_type = kwargs.get("amp_event_type")  # text
            amp_limit = kwargs.get("amp_limit")  # number
            amp_offset = kwargs.get("amp_offset")  # number

            log = logging.getLogger(__name__)
            log.info("amp_detection_sha256: %s", amp_detection_sha256)
            log.info("amp_application_sha256: %s", amp_application_sha256)
            log.info("amp_conn_guid: %s", amp_conn_guid)
            log.info("amp_group_guid: %s", amp_group_guid)
            log.info("amp_start_date: %s", amp_start_date)
            log.info("amp_event_type: %s", amp_event_type)
            log.info("amp_limit: %s", amp_limit)
            log.info("amp_offset: %s", amp_offset)

            yield StatusMessage("Running Cisco AMP get events query...")

            params = {"detection_sha256": amp_detection_sha256, "application_sha256": amp_application_sha256,
                      "connector_guid": amp_conn_guid, "group_guid": amp_group_guid, "start_date": amp_start_date,
                      "event_type": amp_event_type, "limit": amp_limit, "offset": amp_offset}

            validate_params(params)

            amp = Ampclient(self.options)

            rtn = amp.get_paginated_total(amp.get_events, **params)
            query_execution_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # Add in "query_execution_time" and "ip_address" to result to facilitate post-processing.
            results = {"response": rtn, "query_execution_time": query_execution_time}
            yield StatusMessage("Returning 'events' results")

            yield StatusMessage("Done...")

            log.debug(json.dumps(results))
            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            log.exception("Exception in Resilient Function for Cisco AMP for endpoints.")
            yield FunctionError()