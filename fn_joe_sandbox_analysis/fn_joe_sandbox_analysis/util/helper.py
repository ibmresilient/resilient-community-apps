# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
from jbxapi import JoeSandbox
from resilient_lib import str_to_bool, validate_fields

def connect_to_joe_sandbox(options):
    # Validate that jsb_api_key in the app.config has a value
    validate_fields(["jsb_api_key"], options)

    # Get Joe Sandbox options from app.config file
    API_KEY = options.get("jsb_api_key")
    ACCEPT_TAC = str_to_bool(options.get("jsb_accept_tac"))
    ANALYSIS_URL = options.get("jsb_analysis_url")

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

    return ANALYSIS_URL, JoeSandbox(
        apikey=API_KEY,
        apiurl=ANALYSIS_URL,
        accept_tac=ACCEPT_TAC,
        proxies=proxies,
        verify_ssl=verify_ssl)