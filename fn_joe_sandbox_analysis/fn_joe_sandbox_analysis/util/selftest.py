# -*- coding: utf-8 -*-

"""
Function implementation test.
Usage: resilient-circuits selftest -l fn_joe_sandbox_analysis
"""

import logging
import jbxapi
from resilient_lib import RequestsCommon, str_to_bool

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log.addHandler(logging.StreamHandler())

def get_config_option(option_name, options, optional=False):
    """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
    option = options.get(option_name)

    if option is None and optional is False:
        err = "'{0}' is mandatory and is not set in ~/.resilient/app.config file. You must set this value to run this function".format(option_name)
        raise ValueError(err)
    else:
        return option
        
def get_proxies(opts, options):
    rc = RequestsCommon(opts, options)
    proxies = rc.get_proxies()
    return proxies


def selftest_function(opts):
    """
    Placeholder for selftest function. An example use would be to test package api connectivity.
    Suggested return values are be unimplemented, success, or failure.
    """
    app_configs = opts.get("fn_joe_sandbox_analysis", {})
    API_KEY = get_config_option("jsb_api_key", app_configs)
    ACCEPT_TAC = str_to_bool(get_config_option("jsb_accept_tac", app_configs))
    HTTP_PROXY = get_config_option("jsb_http_proxy", app_configs, True)
    HTTPS_PROXY = get_config_option("jsb_https_proxy", app_configs, True)
    log.info(API_KEY)
    proxies = {}
    test = False
    try:
        proxies = get_proxies(opts, app_configs)
        if (HTTP_PROXY) and (len(proxies) == 0):
            proxies["http"] = HTTP_PROXY
                
        if (HTTPS_PROXY) and (len(proxies) == 0):
            proxies["https"] = HTTPS_PROXY
                
        if (len(proxies) == 0):
            proxies = None
    except Exception as proxy_error:
        proxies = None
    joesandbox = jbxapi.JoeSandbox(apikey=API_KEY, accept_tac=ACCEPT_TAC, proxies=proxies)
    test = joesandbox.server_online()
    if test:
        return {
            "state": "success",
            "reason": "Server Online"
        }
    else:
        return {
            "state": "failure",
            "reason": "Server Offline"
        }