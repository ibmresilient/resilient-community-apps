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
    # The URL or the DLP Installation
    sdlp_host=https://<serverip>:<port>
    # The location of your WSDL file used to construct requests when dealing with the Incident and Reporting API
    sdlp_wsdl=https://<serverip>:<port>/ProtectManager/services/v2011/incidents?wsdl
    # The URL of the Incident and Reporting API for your DLP Installation
    sdlp_incident_endpoint=https://<serverip>:<port>/ProtectManager/services/v2011/incidents
    # Username for DLP 
    sdlp_username=<SDLP Username>
    # Password for DLP
    sdlp_password=<SDLP Password>
    # Location of the CA file for DLP, leave Blank or ‘comment out’ for unverified requests
    #sdlp_cafile=./dlp.cer
    # Used to set how often the Listener should poll, default is 10 mins (600)
    sdlp_listener_timer=600
    # The Saved Report ID used to query for Incidents, must be set otherwise the integration will fail
    sdlp_savedreportid=0
    # An optional app.config that, if set to True will perform an additional filter on DLP Incident results 
    # to ensure no Resilient incident exists with the same DLP Incident ID. 
    # Uses search_ex to query for incidents with an sdlp_incident_id custom field 
    sdlp_should_search_res=False
    """
    return config_data
