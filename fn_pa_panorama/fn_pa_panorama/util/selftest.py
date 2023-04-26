# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
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

    # Call the getAddresses API with the hardcoded 'vsys' and 'vsys1' for the location since those are typically
    # function inputs. Returns success if the call is successful

    server_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else PanoramaServers(opts).get_server_name_list()

    err_reason_msg = None
    try:
        for server_name in server_list:
            options = opts.get(server_name, {})
            panorama_util = PanoramaClient(opts, options, "vsys", "vsys1")
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
        cert: {options.get("cert")}"""

    return {
        "state": "success" if status else "failure",
        "reason": err_reason_msg
    }
