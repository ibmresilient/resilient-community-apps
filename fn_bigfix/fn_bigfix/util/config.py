# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
"""Generate a default configuration-file section for fn_bigfix"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""[fn_bigfix]
# Refer to BigFix Function integration guide for configuration option guidelines.
bigfix_url=https://bigfix-url.com
bigfix_port=12345
bigfix_user=BigFixAdmin
bigfix_pass=MyPassword
bigfix_polling_interval=30
bigfix_polling_timeout=600
bigfix_endpoints_wait=30
bigfix_hunt_results_limit=200
bigfix_verify=False
# Settings for access to BigFix via a proxy
#http_proxy=http://proxy:80
#https_proxy=https://proxy:80
"""
