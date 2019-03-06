# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn-ip-void
"""

import logging
import requests
from fn_ip_void.util.ipvoid_helper import get_config_option

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

SUB_URL = "iprep/v1/pay-as-you-go/?key={}&stats"


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_ipvoid", {})
    api_token = get_config_option("ipvoid_api_key", options)
    base_url = get_config_option("ipvoid_base_url", options)
    url = "/".join((base_url, SUB_URL)).format(api_token)
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
