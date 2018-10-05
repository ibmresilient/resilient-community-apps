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
from fn_cisco_amp4ep.lib.helpers import validate_params

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_amp_get_events"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.options = opts.get("fn_cisco_amp4ep", {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_cisco_amp4ep", {})

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

            params = {"detection_sha256": amp_detection_sha256, "application_sha256": amp_application_sha256,
                      "connector_guid": amp_conn_guid, "group_guid": amp_group_guid, "start_date": amp_start_date,
                      "event_type": amp_event_type, "limit": amp_limit, "offset": amp_offset}

            validate_params(params)

            amp = Ampclient(self.options)

            yield StatusMessage("Running Cisco AMP get computers query...")
            rtn = amp.get_events(**params)
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