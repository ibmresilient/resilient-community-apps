# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_query_tor_network
"""

import logging
import requests

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_query_tor_network", {})
    try:
        connection_status = requests.get(options.get('base_url'))
        if not connection_status.status_code == 200:
            raise requests.ConnectionError("The Status code {}".format(connection_status))
        log.info("Successfully Established connection to TOR : {}".format(connection_status))
        return {"state": "Success"}

    except Exception as e:
        log.info("Failed Connection to TOR Error - {}".format(e))
        return {"state": "Failed"}