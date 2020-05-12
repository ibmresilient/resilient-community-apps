# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
# (c) Copyright IBM Corp. 2020. All Rights Reserved.

BASE_URL = "https://haveibeenpwned.com/api/v3"
HAVE_I_BEEN_PWNED_BREACH_URL = "/".join((BASE_URL, "breachedaccount"))
HAVE_I_BEEN_PWNED_PASTES_URL = "/".join((BASE_URL, "pasteaccount"))

def get_config_option(options, option_name, optional=False):
    """Given option_name, checks if it is in appconfig. Raises ValueError if a mandatory option is missing"""
    option = options.get(option_name)

    if not option and optional is False:
        err = "'{0}' is mandatory and is not set in the app.config file. You must set this value to run this " \
              "function".format(option_name)
        raise ValueError(err)

    return option

def make_headers(hibp_api_key):
    """
    build the headers for API calls
    :param hibp_api_key:
    :return: json headers
    """
    return {
        'User-Agent': 'Resilient HIBP/2.0',
        'hibp-api-key': hibp_api_key
    }

def get_proxies(opts):
    """
    build the proxy list
    :param opts:
    :return: dict of proxies
    """
    proxies = {}
    # Get proxies
    proxy_http = get_config_option(opts, "hibp_proxy_http", True)
    proxy_https = get_config_option(opts, "hibp_proxy_https", True)

    if proxy_http is not None:
        proxies["http"] = proxy_http

    if proxy_https is not None:
        proxies["https"] = proxy_https
