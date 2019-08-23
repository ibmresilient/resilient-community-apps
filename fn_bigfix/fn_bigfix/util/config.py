# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_bigfix"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_bigfix]
# Refer to BigFix Function integration guide for configuration option guidelines.
bigfix_url=https://bigfix-url.com
bigfix_port=12345
bigfix_user=BigFixAdmin
bigfix_pass=MyPassword
bigfix_polling_interval=30
bigfix_polling_timeout=600
bigfix_endpoints_wait=30
bigfix_hunt_results_limit=200
"""
    return config_data