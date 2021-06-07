# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_virustotal"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_virustotal]
api_token=
polling_interval_sec=60
max_polling_wait_sec=600
# uncomment is proxies are needed to access VirusTotal
#http_proxy=
#https_proxy=
"""
    return config_data
