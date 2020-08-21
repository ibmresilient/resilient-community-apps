# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

import os

def get_proxies():
    proxies = {}

    if "MITRE_HTTPS_PROXY" in os.environ:
        proxies["http_proxy"] = os.environ["MITRE_HTTPS_PROXY"]

    if "MITRE_HTTPS_PROXY" in os.environ:
        proxies["https_proxy"] = os.environ["MITRE_HTTPS_PROXY"]

    return proxies