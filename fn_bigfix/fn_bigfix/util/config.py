# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_bigfix"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_bigfix]
bigfix_url=https://bigfix-url.com
bigfix_port=12345
bigfix_user=BigFixAdmin
bigfix_pass=MyPassword
bigfix_polling_interval=30
bigfix_polling_timeout=1800
hunt_results_limit=200
"""
#    return config_data
    return None