# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_phish_tank
"""

import logging
from fn_phish_tank.util.phish_tank_helper import *

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_phish_tank", {})
    phishtank_url = options.get('phish_tank_api_url')
    phishtank_api_key = options.get('phish_tank_api_key')
    phishtank_proxy = options.get('proxy')
    check_url = "https://elegancetille.com/"

    phish_helper_obj = phish_tank_helper()
    proxy_header = phish_helper_obj.format_proxy_data(phishtank_proxy)
    post_data_header = phish_helper_obj.create_post_data(check_url, phishtank_api_key)

    _api_session = phish_helper_obj.session()
    try:
        _api_response = _api_session.post(phishtank_url, data=post_data_header, proxies=proxy_header)
        _api_response.raise_for_status()
        _api_response_json = _api_response.json()
        log.info("Successfully Established the connection to the PhishTank Database.")
        return {"state": "Success"}
    except Exception as err_msg:
        log.info("Failed to Establish the connection to PhishTank Database: %s", err_msg)
        return {"state": "Failed"}
    finally:
        _api_session.close()