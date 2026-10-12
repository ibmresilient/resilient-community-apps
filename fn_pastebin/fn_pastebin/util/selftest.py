# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_pastebin
"""

import requests
import logging
from resilient_lib import RequestsCommon

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())


def get_proxies(opts, options):
    rc = RequestsCommon(opts, options)
    proxies = rc.get_proxies()
    return proxies


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_pastebin", {})

    pastebin_proxy_http = app_configs.get("pastebin_proxy_http", True)
    pastebin_proxy_https = app_configs.get("pastebin_proxy_https", True)
    proxies = {}

    try:
        proxies = get_proxies(opts, app_configs)
        if pastebin_proxy_http and (len(proxies) == 0):
            proxies["http"] = pastebin_proxy_http

        if pastebin_proxy_https and (len(proxies) == 0):
            proxies["https"] = pastebin_proxy_https

        if len(proxies) == 0:
            proxies = None
    except Exception as proxy_error:
        proxies = None

    pastebin_api_dev_key = str(app_configs.get("pastebin_api_dev_key"))
    pastebin_api_user_name = str(app_configs.get("pastebin_api_user_name", True))
    pastebin_api_user_password = str(app_configs.get("pastebin_api_user_password"))
    pastebin_login_url = "https://pastebin.com/api/api_login.php"

    # Get the license key to access the API endpoint
    try:
        response = requests.post(pastebin_login_url, proxies=proxies, data={
            "api_dev_key": pastebin_api_dev_key,
            "api_user_name": pastebin_api_user_name,
            "api_user_password": pastebin_api_user_password
        })

        if response.status_code == 200:
            return {"state": "success", "status_code": response.status_code}
        else:
            return {"state": "failure", "status_code": response.status_code}

    except Exception as e:
        return {"state": "failure", "status_code": e}
