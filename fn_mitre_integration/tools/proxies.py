# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import os

system_http_proxy = "MITRE_HTTP_PROXY"
system_https_proxy = "MITRE_HTTPS_PROXY"

def get_proxies():
    proxies = {}

    if system_http_proxy in os.environ:
        proxies["http_proxy"] = os.environ[system_http_proxy]

    if system_https_proxy in os.environ:
        proxies["https_proxy"] = os.environ[system_https_proxy]

    return proxies