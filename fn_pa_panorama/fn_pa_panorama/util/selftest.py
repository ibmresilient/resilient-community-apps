# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_pa_panorama
"""

import logging
from fn_pa_panorama.util.panorama_util import PanoramaClient, PACKAGE_NAME, PanoramaServers

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """

    # Call the getAddresses API with 'vsys' and 'vsys1' by default for the location if not specified in the app.config
    # Returns success if the call is successful

    server_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else PanoramaServers(opts).get_server_name_list()

    err_reason_msg = None
    try:
        for server_name in server_list:
            options = opts.get(server_name, {})
            
            # Set variables based on how sf_location is configured.
            sf_vsys = options.get("sf_vsys", "vsys1") if options.get("sf_location", "vsys") in ["vsys", "panorama-pushed"] else None
            sf_device_group = options.get("sf_device_group", None) if options.get("sf_location", "vsys") == "device-group" else None

            panorama_util = PanoramaClient(opts, options, options.get("sf_location", "vsys"), sf_vsys, sf_device_group)
            panorama_util.get_addresses()

            status = True if panorama_util else False
            log.info(f"Test for {server_name} was successful")

    except Exception as err:
        status = False
        err_reason_msg = f"""Could not connect to Panorama.
        error: {err}
        ---------
        Current Configs in app.config file:
        ---------
        panorama_host: {options.get("panorama_host")}
        api_version: {options.get("api_version")}
        cert: {options.get("cert")}
        sf_location: {options.get("sf_location")}
        sf_vsys: {options.get("sf_vsys")}
        sf_device_group: {options.get("sf_device_group")}"""

    return {
        "state": "success" if status else "failure",
        "reason": err_reason_msg
    }
