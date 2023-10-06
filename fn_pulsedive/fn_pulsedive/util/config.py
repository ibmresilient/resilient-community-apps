# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_pulsedive"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_pulsedive]
pulsedive_api_key=<my api key>
pulsedive_api_url=https://pulsedive.com/api/
"""
    return config_data
