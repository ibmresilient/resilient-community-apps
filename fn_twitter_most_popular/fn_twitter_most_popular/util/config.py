# (c) Copyright IBM Corp. 2018. All Rights Reserved.

# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_twitter_most_popular"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_twitter_most_popular]
twitter_api_key=<YOUR_API_KEY>
twitter_api_secret=<YOUR_API_SECRET>
#twitter_proxy_http=<YOUR_HTTP_PROXY>
#twitter_proxy_https=<YOUR_HTTPS_PROXY>
"""
    return config_data