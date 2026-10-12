# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
from jbxapi import JoeSandbox
from resilient_lib import str_to_bool, validate_fields, RequestsCommon

PACKAGE_NAME = "fn_joe_sandbox_analysis"

def connect_to_joe_sandbox(opts, options):
    # Validate that jsb_api_key in the app.config has a value
    validate_fields(["jsb_api_key", "jsb_api_url", "jsb_accept_tac"], options)

    # Get Joe Sandbox options from app.config file
    API_KEY = options.get("jsb_api_key")
    ACCEPT_TAC = str_to_bool(options.get("jsb_accept_tac"))
    ANALYSIS_URL = options.get("jsb_api_url")
    # Get proxies from app.config
    proxies = RequestsCommon(opts, options).get_proxies()

    # Get verify setting from app.config
    verify_ssl = options.get("jsb_verify", True)
    if verify_ssl:
        verify_ssl = False if verify_ssl.lower() == "false" else (True if verify_ssl.lower() == "true" else verify_ssl)

    return ANALYSIS_URL, JoeSandbox(
        apikey=API_KEY,
        apiurl=ANALYSIS_URL,
        accept_tac=ACCEPT_TAC,
        proxies=proxies,
        verify_ssl=verify_ssl)