# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Generate a default configuration-file section for fn_symantec_dlp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_symantec_dlp]
# Whether or not to start the listener
sdlp_should_poller_run=True

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
polling_lookback=120000
# set polling_interval=0 to disable. Otherwise set in seconds
polling_interval=600
# polling_lookback in minutes to look back first time poller starts
polling_lookback=120
# poller timezone to match Siemplify configuration
poller_timezone=Etc/GMT

# The Saved Report ID used to query for Incidents, must be set otherwise the integration will fail
sdlp_savedreportid=0

# An optional app.config that, if set to True will perform an additional filter on DLP Incident results 
# to ensure no Resilient incident exists with the same DLP Incident ID. 
# Uses search_ex to query for incidents with an sdlp_incident_id custom field 
sdlp_should_search_res=False

# When getting a list of Incidents from a saved report, a parameter incident_creation_date_later_than
# must be provided to make a query. This value represents the earliest date for Incidents that will be queried. 
# For this app.config, specify a number of days in the past to look back on.
# For example to pull any Incidents in the last year, set this value to 365.
# The default value used if this is not set is 14 days
#sdlp_incident_creation_date_later_than=365
"""
    return config_data
