# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
import time
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_crowdstrike_falcon.util.cs_helper import CrowdStrikeHelper


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cs_falcon_device_actions"""

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

    @function("fn_cs_falcon_device_actions")
    def _fn_cs_falcon_device_actions_function(self, event, *args, **kwargs):
        """Function: Function that uses the CrowdStrike Falcon '/devices/entities/devices-actions/' endpoint to Contain or Lit Containment on a Device"""
        try:
            err_msg = None
            log = logging.getLogger(__name__)

            # Get the wf_instance_id so we can raise an error if the workflow was terminated by the user
            wf_instance_id = event.message["workflow_instance"]["workflow_instance_id"]

            # Map cs actions to their status
            cs_action_name_to_status_map = {
                "contain": "contained",
                "lift_containment": "normal"
            }

            # Instansiate helper (which gets appconfigs)
            cs_helper = CrowdStrikeHelper(self.function_opts)

            # Instansiate new Resilient API object
            res_client = self.rest_client()

            # Get the function inputs:
            fn_inputs = {
                "cs_device_id": cs_helper.get_function_input(kwargs, "cs_device_id"),  # text (required)
                "cs_action_name": self.get_select_param(kwargs.get("cs_action_name"))  # select, values: "contain", "lift_containment"
            }

            # Create new Function ResultPayload with appconfigs and function inputs
            payload = ResultPayload(CrowdStrikeHelper.app_config_section, **fn_inputs)

            # Get crowdstrike device_id and action_name
            cs_device_id = fn_inputs.get("cs_device_id")
            cs_action_name = fn_inputs.get("cs_action_name")

            yield StatusMessage("> Function Inputs OK")

            # Set request url, headers, params and data
            device_action_url = "{0}{1}".format(cs_helper.oauth2_base_url, "/devices/entities/devices-actions/v2")
            device_action_headers = {"Content-Type": "application/json", "Authorization":"Bearer {0}".format(cs_helper.oauth2_token)}
            device_action_params = {"action_name": cs_action_name}

            # As per CS APIs: Provide the ID in JSON format with the key ids and the value in square brackets,
            device_action_json = {
                "ids": [cs_device_id]
            }

            yield StatusMessage("> Sending device-action '{0}' request to CrowdStrike for device: {1}".format(
                cs_action_name, cs_device_id))

            # Call the request
            post_device_action_response = cs_helper.cs_api_request(
                method="POST",
                url=device_action_url,
                headers=device_action_headers,
                params=device_action_params,
                json_data=device_action_json)

            # If the response contains an "invalid bearer token" error, our oauth2 token is out of date
            if post_device_action_response.get("error"):
                err_msg = post_device_action_response.get("err_msg")
                if "invalid bearer token" in err_msg:

                    yield StatusMessage("> oauth2 Token out of date. Requesting new one")
                    cs_helper.get_oauth2_token()

                    yield StatusMessage("> Re-sending device-action '{0}' request to CrowdStrike for device: {1}".format(
                        cs_action_name, cs_device_id))

                    # Reset headers with new token
                    device_action_headers = {"Content-Type": "application/json", "Authorization":"Bearer {0}".format(cs_helper.oauth2_token)}

                    post_device_action_response = cs_helper.cs_api_request(
                        method="POST",
                        url=device_action_url,
                        headers=device_action_headers,
                        params=device_action_params,
                        json_data=device_action_json)

                    # If after the second request, there is still some other error, raise that error
                    if post_device_action_response.get("error"):
                        raise ValueError("> Failed to {0} device {1}. {2}".format(
                            cs_action_name, cs_device_id, post_device_action_response.get("err_msg")))

                else:
                    raise ValueError("> Failed to {0} device {1}. {2}".format(
                        cs_action_name, cs_device_id, err_msg))

            # Get current time in seconds
            start_time = time.time()

            # Get the status of the device
            device_status = cs_helper.get_device_status(cs_device_id)

            # While the status is not 'normal' or 'contained'
            while device_status.get("status") != cs_action_name_to_status_map.get(cs_action_name):

                if device_status.get("error"):
                    raise ValueError(device_status.get("err_msg"))

                 # Check if workflow has been terminated by user"
                if cs_helper.is_workflow_terminated(wf_instance_id, res_client):
                    raise ValueError("> Workflow terminated by user.")

                if cs_helper.should_timeout(start_time):
                    yield StatusMessage("> Workflow timed out trying to latest status of the device_id {0}".format(cs_device_id))
                    break

                yield StatusMessage("> Device Status: {0}. Fetching again every {1} seconds".format(device_status.get("status"), cs_helper.ping_delay))
                device_status = cs_helper.get_device_status(cs_device_id)

            payload = payload.done(True, {
                "meta": post_device_action_response.get("meta"),
                "device_id": post_device_action_response.get("resources")[0].get("id"),
                "device_status": device_status.get("status")
            })

            results = payload
            log.debug("RESULTS: %s", results)
            log.info("> Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
