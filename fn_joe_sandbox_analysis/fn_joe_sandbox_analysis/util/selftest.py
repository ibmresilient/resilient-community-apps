# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_joe_sandbox_analysis
"""

from fn_joe_sandbox_analysis.util.helper import connect_to_joe_sandbox, PACKAGE_NAME

def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    try:
        options = opts.get(PACKAGE_NAME, {})
        ANALYSIS_URL, joesandbox = connect_to_joe_sandbox(opts, options)

        if joesandbox.server_online().get("online"):
            status = True
            reason = "Server Online"
        else:
            status = False
            reason = "Server Offline"

    except Exception as err:
        status = False
        reason = f"""Could not connect to joe_sandbox
        error: {err}
        ---------
        Current Configs in app.config file:
        ---------
        jsb_accept_tac: {options.get("jsb_accept_tac")}
        jsb_api_url: {options.get("jsb_api_url")}
        jsb_systems: {options.get("jsb_systems")}
        jsb_secondary_results: {options.get("jsb_secondary_results")}
        jsb_verify: {options.get("jsb_verify")}"""

    return {
        "state": "success" if status else "failure",
        "reason": reason
    }
