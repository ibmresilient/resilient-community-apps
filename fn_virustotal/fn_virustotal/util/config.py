# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_virustotal"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_virustotal]
api_token=
proxies=
polling_interval_sec=60
max_polling_wait_sec=600
"""
    return config_data
