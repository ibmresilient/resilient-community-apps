# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-ip-void
"""

import logging
import requests
from fn_ip_void.util.ipvoid_helper import get_config_option, SUB_URL

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example 
    use would be to test package api connectivity.
    Suggested return values are be unimplemented, 
    success, or failure.
    """
    options = opts.get("fn_ip_void", {})
    api_token = get_config_option(options, "ipvoid_api_key")
    base_url = get_config_option(options, "ipvoid_base_url")
    url = "/".join((base_url, SUB_URL)).format('iprep', api_token,'stats')
    try:
        res = requests.get(url)
        if res.status_code == 200:
            log.info("elapsed_time:  %s", res.json()["elapsed_time"])
            log.info("credits_remained:  %s", res.json()["credits_remained"])
            log.info("credits_expiration:  %s", res.json()["credits_expiration"])
            log.info("estimated_queries:  %s", res.json()["estimated_queries"])
            log.info("estimated_queries:  %s", res.json()["estimated_queries"])
            return {"state": "success"}

        else:
            return {"state": "failure", "reason": res.json()["error"]}

    except Exception as e:
        log and log.error(e)
        return {"state": "failure", "reason": e}
