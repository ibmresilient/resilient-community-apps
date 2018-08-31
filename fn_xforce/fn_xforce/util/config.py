# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Generate a default configuration-file section for fn_xforce"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_xforce]
xforce_apikey = <YOUR_API_KEY>
xforce_password = <YOUR_API_PASSWORD>
xforce_https_proxy = <YOUR_PROXY_URL>
xforce_http_proxy = <YOUR_PROXY_URL>
xforce_baseurl = https://api.xforce.ibmcloud.com
"""
    return config_data
