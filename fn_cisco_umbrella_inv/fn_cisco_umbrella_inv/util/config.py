# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_umbrella_inv"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cisco_umbrella_inv]
base_url=https://investigate.api.umbrella.com/
# The api_token will be supplied by Cisco will be in uuid format.
api_token=<api token>
results_limit=200
"""
    return config_data