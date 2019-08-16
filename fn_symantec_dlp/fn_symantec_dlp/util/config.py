# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Generate a default configuration-file section for fn_symantec_dlp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_symantec_dlp]
    sdlp_listener_toggle=True
    sdlp_host=https://<serverip>:<port>
    sdlp_wsdl=https://<serverip>:<port>/ProtectManager/services/v2011/incidents?wsdl
    sdlp_username=admin
    sdlp_password=admin
    """
    return config_data
