# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u'''
# Note: the QRadar instance name that you want to communicate with, must equal the
# QRadar Destination Name that is set when configuring the SOAR Plugin
# Example: SOAR_Plugin_Destination_Name1
[fn_qradar_integration:SOAR_Plugin_Destination_Name1]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false|/path/to/cert
#search_timeout=

# Note: the QRadar instance name that you want to communicate with, must equal the
# QRadar Destination Name that is set when configuring the SOAR Plugin
# Example: SOAR_Plugin_Destination_Name2
[fn_qradar_integration:SOAR_Plugin_Destination_Name2]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false|/path/to/cert
#search_timeout=
'''
