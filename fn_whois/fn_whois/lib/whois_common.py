# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

import whois
import socks
import socket

try:
    import urllib.parse as urlparse
except ImportError:
    import urlparse

def whois_query(whois_query, whois_https_proxy):
    """
    make the whois query, setting up the proxy as necessary
    :param whois_https_proxy:
    :param whois_query:
    :return: json result
    """
    # setup proxy settings, if found
    setup_proxy(whois_https_proxy)
    return whois.whois(whois_query)

def setup_proxy(whois_https_proxy):
    """
    is a proxy needed?
    :param whois_https_proxy:
    :return:
    """
    if whois_https_proxy:
        uri = urlparse.urlparse(whois_https_proxy)
        socks.set_default_proxy(socks.PROXY_TYPE_HTTP, uri.hostname, uri.port)
        socket.socket = socks.socksocket

def get_config_option(opts, option_name, optional=False):
    """Given option_name, checks if it is in app.config. Raises ValueError if a mandatory option is missing"""
    option = opts.get(option_name)

    if not option and optional is False:
        err = "'{0}' is mandatory and is not set in app.config file. You must set this value to run this function".format(
            option_name)
        raise ValueError(err)
    else:
        return option
