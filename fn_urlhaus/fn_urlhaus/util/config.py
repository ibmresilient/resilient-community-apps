# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_urlhaus"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_urlhaus]
url=https://urlhaus-api.abuse.ch/v1
# these are needed for submitting malware urls
submit_url=https://urlhaus.abuse.ch/api/
#  twitter api key
submit_api_key=
"""
    return config_data
