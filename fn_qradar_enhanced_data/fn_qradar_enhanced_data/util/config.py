# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2022. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u'''
#Settings that apply to all QRadar servers
[fn_qradar_integration:edm_global_settings]
#search_timeout=
# Interval to poll QRadar for changes (in minutes)
# To turn the poller off user value 0
polling_interval = 120
polling_lookback = 60

# Note: If [fn_qradar_integration] is present without a label then all labeled servers will
# be disregarded and only the server under [fn_qradar_integration] will be used
#
# The QRadar instance name that you want to communicate with, must equal the
# QRadar Destination Name that is set when configuring the SOAR Plugin
# Example: SOAR_Plugin_Destination_Name1
[fn_qradar_integration:SOAR_Plugin_Destination_Name1]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false|/path/to/cert

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
'''
