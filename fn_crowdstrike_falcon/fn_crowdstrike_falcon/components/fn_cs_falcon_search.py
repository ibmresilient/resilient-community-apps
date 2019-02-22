# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, RequestsCommon
from resilient_lib.components.integration_errors import IntegrationError
from fn_crowdstrike_falcon.util.cs_helper import CrowdStrikeHelper

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cs_falcon_search"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.opts = opts
        self.function_opts = opts.get(CrowdStrikeHelper.app_config_section, {})

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.opts = opts
        self.function_opts = opts.get(CrowdStrikeHelper.app_config_section, {})
        CrowdStrikeHelper.load_class_variables(self.function_opts)

    @function("fn_cs_falcon_search")
    def _fn_cs_falcon_search_function(self, event, *args, **kwargs):
        """Function that queries your CrowdStrike Falcon Hosts for a list of Devices using a Filter and/or Query. If Devices are found they are returned as a Python List"""

        err_msg = None
        log = logging.getLogger(__name__)

        try:
            # Instansiate helper (which gets appconfigs)
            cs_helper = CrowdStrikeHelper(self.function_opts)

            # Get the function inputs:
            fn_inputs = {
                "cs_filter_string": cs_helper.get_function_input(kwargs, "cs_filter_string", True),  # text (optional)
                "cs_query": cs_helper.get_function_input(kwargs, "cs_query", True)  # text (optional)
            }

            # Create new Function ResultPayload with appconfigs and function inputs
            payload = ResultPayload(CrowdStrikeHelper.app_config_section, **fn_inputs)

            # Get crowdstrike filter and query
            cs_filter_string = fn_inputs.get("cs_filter_string")
            cs_query = fn_inputs.get("cs_query")

            # At least on of them has to be defined
            if cs_filter_string is None and cs_query is None:
                raise IntegrationError("Function Input cs_filter_string or cs_query must be defined")

            yield StatusMessage("> Function Inputs OK")

            # Instansiate new RequestCommon object to facilitate CrowdStrike REST API calls
            rqc = RequestsCommon(self.opts, self.function_opts)

            # Fist we look ip device ids
            # Set the request URL and payload
            get_device_ids_url = "{0}{1}".format(cs_helper.bauth_base_url, "/devices/queries/devices/v1")
            get_device_ids_payload = {}

            if cs_filter_string is not None:
                get_device_ids_payload["filter"] = cs_filter_string

            if cs_query is not None:
                get_device_ids_payload["q"] = cs_query

            yield StatusMessage(u'> Searching CrowdStrike for devices. Filter: "{0}" Query: {1}'.format(cs_helper.str_to_unicode(cs_filter_string), cs_query))

            # Make GET request for device_ids
            get_device_ids_response = rqc.execute_call(
                verb="GET",
                url=get_device_ids_url,
                payload=get_device_ids_payload,
                basicauth=(cs_helper.bauth_api_uuid, cs_helper.bauth_api_key),
                headers=cs_helper.json_header)

            device_ids = get_device_ids_response.get("resources", [])

            if len(device_ids) > 0:
                # Then we get device_details for each device_id
                yield StatusMessage("> Devices found. Getting device details")

                get_device_details_url = "{0}{1}".format(cs_helper.bauth_base_url, "/devices/entities/devices/v1")
                get_device_details_payload = {
                    "ids": device_ids
                }

                get_device_details_response = rqc.execute_call(
                    verb="GET",
                    url=get_device_details_url,
                    payload=get_device_details_payload,
                    basicauth=(cs_helper.bauth_api_uuid, cs_helper.bauth_api_key),
                    headers=cs_helper.json_header)

                device_details = get_device_details_response.get("resources")

                if device_details is not None:
                    yield StatusMessage("> Device details received. Finishing...")

                    # For each device, convert their string timestamps to utc_time in ms
                    for device in device_details:
                        device["agent_local_time"] = cs_helper.timestamp_to_ms_epoch(device.get("agent_local_time"), timestamp_format="%Y-%m-%dT%H:%M:%S.%fZ")
                        device["first_seen"] = cs_helper.timestamp_to_ms_epoch(device.get("first_seen"))
                        device["modified_timestamp"] = cs_helper.timestamp_to_ms_epoch(device.get("modified_timestamp"))
                        device["last_seen"] = cs_helper.timestamp_to_ms_epoch(device.get("last_seen"))

                    payload = payload.done(True, device_details)

                else:
                    err_msg = u'> Could not get device details from CrowdStrike. Filter: "{0}" Query: {1}'.format(cs_helper.str_to_unicode(cs_filter_string), cs_query)
                    yield StatusMessage(err_msg)
                    payload = payload.done(False, None, reason=err_msg)

            else:
                err_msg = u'> No devices found in CrowdStrike. Filter: "{0}" Query: {1}'.format(cs_helper.str_to_unicode(cs_filter_string), cs_query)
                yield StatusMessage(err_msg)
                payload = payload.done(False, None, reason=err_msg)

            results = payload
            log.debug("RESULTS: %s", results)
            log.info("Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
