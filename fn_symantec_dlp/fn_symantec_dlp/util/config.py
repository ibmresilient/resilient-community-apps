# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Generate a default configuration-file section for fn_symantec_dlp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_symantec_dlp]
# The URL of the Symantec SLP Enforce Server
sdlp_host=<serverip>
# Symantec DLP REST API version
api_version=v2
# Username for DLP account
sdlp_username=<SDLP Username>
# Password for DLP account
sdlp_password=<SDLP Password>
# The Saved Report ID used to query for Incidents, must be set otherwise the integration will fail
sdlp_savedreportid=0
# Poller interval in seconds, comment out or set to 0 to disable poller
polling_interval=60
# Poller lookback time first time, in minutes
polling_lookback=1200
# false|/path/to/certificate
cafile=
# Override default jinja templates files as necessary for case creation, closing and updating.
create_case_template=
close_case_template=
update_case_template=
"""
    return config_data
