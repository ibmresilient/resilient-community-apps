# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_secureworks_ctp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_secureworks_ctp]
# Required - URL and credentials to authenticate to Secureworks CTP
base_url=https://api.secureworks.com/api/ticket/v3
username=
password=

# Required - How often, in minutes, to check for new events
# To turn the poller off use value 0
polling_interval=600
"""
    return config_data