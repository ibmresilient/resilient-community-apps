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
    sdlp_listener_toggle=True
    # The URL or the DLP Installation
    sdlp_host=https://<serverip>:<port>
    # The location of your wsdl file 
    sdlp_wsdl=https://<serverip>:<port>/ProtectManager/services/v2011/incidents?wsdl
    # Username for DLP 
    sdlp_username=admin
    # Password for DLP
    sdlp_password=admin
    # Location of the CA file for DLP, leave blank for unverified
    #sdlp_cafile=./dlp.cer
    # Used to set how often the Listener should poll, default is 10 mins (600)
    sdlp_listener_timer=600
    # The Saved Report ID used to query for Incidents, must be set otherwise the integration will fail
    sdlp_savedreportid=0
    """
    return config_data
