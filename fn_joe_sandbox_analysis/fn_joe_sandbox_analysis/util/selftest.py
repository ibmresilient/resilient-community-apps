# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_joe_sandbox_analysis
"""

import logging
import jbxapi
from resilient_lib import str_to_bool, validate_fields

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    options = opts.get("fn_joe_sandbox_analysis", {})

    # Validate that jsb_api_key in the app.config has a value
    validate_fields(["jsb_api_key"], options)

    # Get proxies from app.config
    proxies = {}
    HTTP_PROXY = options.get("jsb_http_proxy", None)
    if HTTP_PROXY:
        proxies["http"] = HTTP_PROXY
    HTTPS_PROXY = options.get("jsb_https_proxy", None)
    if HTTPS_PROXY:
        proxies["https"] = HTTPS_PROXY

    # Get verify setting from app.config
    verify_ssl = options.get("jsb_verify", False)
    if verify_ssl:
        verify_ssl = False if verify_ssl.lower() == "false" else (True if verify_ssl.lower() == "true" else verify_ssl)

    joesandbox = jbxapi.JoeSandbox(apikey=options.get("jsb_api_key"),
                                   apiurl=options.get("jsb_analysis_url"),
                                   accept_tac=str_to_bool(options.get("jsb_accept_tac")),
                                   proxies=proxies,
                                   verify_ssl=verify_ssl)

    if joesandbox.server_online().get("online"):
        return {"state": "success", "reason": "Server Online"}
    else:
        return { "state": "failure", "reason": "Server Offline"}
