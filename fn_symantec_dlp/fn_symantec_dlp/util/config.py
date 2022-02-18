# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Generate a default configuration-file section for fn_symantec_dlp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_symantec_dlp]
# The URL of the DLP Installation
sdlp_host=<serverip>

# SentinelOne REST API version
api_version=v2

# Username for DLP 
sdlp_username=<SDLP Username>

# Password for DLP
sdlp_password=<SDLP Password>

# false|/path/to/certificate
cafile=
# Poller interval in seconds, comment out or set to 0 to disable poller
polling_interval=60
# Poller lookback time first time, in minutes
polling_lookback=12000

# The Saved Report ID used to query for Incidents, must be set otherwise the integration will fail
sdlp_savedreportid=0
"""
    return config_data
