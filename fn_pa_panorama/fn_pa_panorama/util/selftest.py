# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn_pa_panorama
"""

import logging
from fn_pa_panorama.util.panorama_util import PanoramaClient

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
    options = opts.get("fn_pa_panorama", {})
    try:
        panorama_util = PanoramaClient(options, "vsys", "vsys1")
        panorama_util.get_addresses()

        return {"status": "success"}

    except Exception as err:
        err_reason_msg = """Could not connect to Panorama.
        error: {}
        ---------
        Current Configs in app.config file:
        ---------
        api_key: {}
        panorama_host: {}
        cert: {}""".format(
            err,
            options.get("api_key"),
            options.get("panorama_host"),
            options.get("cert")
        )

        return {
            "status": "failure",
            "reason": err_reason_msg
        }
