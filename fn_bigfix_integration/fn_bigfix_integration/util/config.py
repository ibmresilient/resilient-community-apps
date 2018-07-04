# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_bigfix_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_bigfix_integration]
bigfix_int_auto_configure=False
bigfix_url=https://bigfix-url.com
bigfix_port=12345
bigfix_user=BigFixAdmin
bigfix_pass=MyPassword
hunt_results_limit=200
polling_period=120
"""
#    return config_data
    return None