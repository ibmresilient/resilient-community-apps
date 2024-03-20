# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Function implementation
   test with: resilient-circuits selftest -l fn-jira
"""
import logging
from fn_jira.util.helper import PACKAGE_NAME, JiraServers
from fn_jira.lib.app_common import AppCommon

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

def selftest_function(opts):
    """
    This test will attempt to login to Jira
    """
    reason = None
    server_list = {PACKAGE_NAME} if opts.get(PACKAGE_NAME, {}) else JiraServers(opts).get_server_name_list()

    try:
        for server_name in server_list:
            options = opts.get(server_name, {})
            r = AppCommon(opts, options).get_jira_client()

            status = True if r else False
            log.info(f"Test for {server_name} was successful")

    except Exception as err:
        status = False
        reason = f"""Could not connect to Jira
        error: {err}
        ---------
        Current Configs in app.config file:
        ---------
        url: {options.get("url")}
        auth_method: {options.get("auth_method")}
        user: {options.get("user")}
        jira_dt_name: {options.get("jira_dt_name")}
        verify_cert: {options.get("verify_cert")}"""

    return {
        "state": "success" if status else "failure",
        "reason": reason
    }
