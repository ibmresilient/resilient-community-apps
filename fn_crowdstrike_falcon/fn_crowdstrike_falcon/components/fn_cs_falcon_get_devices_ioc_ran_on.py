# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

import logging
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload
from fn_crowdstrike_falcon.util.cs_helper import CrowdStrikeHelper


class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'fn_cs_falcon_get_devices_ioc_ran_on"""

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

    @function("fn_cs_falcon_get_devices_ioc_ran_on")
    def _fn_cs_falcon_get_devices_ioc_ran_on_function(self, event, *args, **kwargs):
        """Function: Function that uses the CrowdStrike Falcon '/indicators/queries/devices/v1' endpoint to get the list of Devices an IOC Ran On. Supported IOC types: sha256, sha1, md5 and domain."""
        try:
            err_msg = None
            log = logging.getLogger(__name__)

            # Map resilient artifact type to crowdstrike ioc type
            map_artifact_type_to_ioc_type = {
                "DNS Name": "domain",
                "Malware SHA-256 Hash": "sha256",
                "Malware SHA-1 Hash": "sha1",
                "Malware MD5 Hash": "md5"
            }

            # Instansiate helper (which gets appconfigs)
            cs_helper = CrowdStrikeHelper(self.function_opts)

            # Get the function inputs:
            fn_inputs = {
                "cs_ioc_type": cs_helper.get_function_input(kwargs, "cs_ioc_type"),  # text (required)
                "cs_ioc_value": cs_helper.get_function_input(kwargs, "cs_ioc_value"),  # text (required)
                "cs_return_limit": cs_helper.get_function_input(kwargs, "cs_return_limit", True)  # text (optional)
            }

            # Create new Function ResultPayload with appconfigs and function inputs
            payload = ResultPayload(CrowdStrikeHelper.app_config_section, **fn_inputs)

            # Get crowdstrike cs_ioc_type, cs_ioc_value and cs_return_limit
            cs_ioc_type = fn_inputs.get("cs_ioc_type")
            cs_ioc_value = fn_inputs.get("cs_ioc_value")
            cs_return_limit = fn_inputs.get("cs_return_limit")

            yield StatusMessage("> Function Inputs OK")

            # Convert Resilient Artifact Type to support CrowdStrike IOC type
            supported_ioc_type = map_artifact_type_to_ioc_type.get(cs_ioc_type, None)

            # If its a type that is not supported, raise error
            if supported_ioc_type is None:
                raise ValueError("{0} is not a supported IOC type. Supported types are {1}".format(cs_ioc_type, map_artifact_type_to_ioc_type))

            # Set request url and payload
            get_device_ioc_ran_on_url = "{0}{1}".format(cs_helper.bauth_base_url, "/indicators/queries/devices/v1")
            get_device_ioc_ran_on_payload = {
                "type": supported_ioc_type,
                "value": cs_ioc_value
            }

            # If the no. of devices to be returned limit is defined, set it in the payload
            if cs_return_limit:
                log.debug("cs_return_limit set to: %s", cs_return_limit)
                get_device_ioc_ran_on_payload["limit"] = cs_return_limit

            # Set the request
            get_device_ioc_ran_on_response = cs_helper.cs_api_request(
                method="GET",
                url=get_device_ioc_ran_on_url,
                basicauth=(cs_helper.bauth_api_uuid, cs_helper.bauth_api_key),
                params=get_device_ioc_ran_on_payload)

            # If there is a 'handled' error, handle it
            if get_device_ioc_ran_on_response.get("error"):
                err_msg = get_device_ioc_ran_on_response.get("err_msg")

                # If known error of no devices found for the IOC, handle gracefully
                if "Resource Not Found" in err_msg:
                    err_msg = "IOC {0}:{1} not found on any CrowdStrike Device.".format(cs_ioc_type, cs_ioc_value)
                    yield StatusMessage("> {0}".format(err_msg))
                    payload = payload.done(False, None, reason=err_msg)

                # Else raise the error
                else:
                    raise ValueError(err_msg)

            # Else if no errors, set build function results payload
            else:
                payload = payload.done(True, {
                    "meta": get_device_ioc_ran_on_response.get("meta"),
                    "device_ids": get_device_ioc_ran_on_response.get("resources")
                })

            results = payload
            log.debug("RESULTS: %s", results)
            log.info("> Complete")

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()
