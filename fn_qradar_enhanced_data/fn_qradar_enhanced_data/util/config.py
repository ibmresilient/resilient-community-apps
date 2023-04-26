# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
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
# Set the timezone off set from UTC time. This off set is used to make sure the poller time is set to the
#  same timezone as the QRadar servers timezone. Value must start with + or -, then hours followed by : and then minutes.
# If timezone_offset under [fn_qradar_enhanced_data:global_settings] is configured, then timezone_offset
#  that are configured under the individual QRadar servers will be ignored
#timezone_offset = -4:00
# Interval to poll QRadar for changes (in seconds)
# When polling_interval equals 0 the poller is off
polling_interval=0
# Amount of time in minutes to look back for changes
polling_lookback=60
# If true then data tables given in the workflows will be cleared when incident is updated by poller
clear_datatables=True
# If sync_notes under [fn_qradar_integration:edm_global_settings] is configured, then sync_notes
#  that are configured under the individual QRadar servers will be ignored
# If true then notes that are added to QRadar offenses will be added to their linked SOAR incidents
sync_notes=True

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
#search_timeout=
# If true then notes that are added to QRadar offenses will be added to their linked SOAR incidents
#sync_notes=True
# Set the timezone off set from UTC time. This off set is used to make sure the poller time is set to the
#  same timezone as the QRadar servers timezone. Value must start with + or -, then hours followed by : and then minutes.
#timezone_offset = -4:00

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
# If true then notes that are added to QRadar offenses will be added to their linked SOAR incidents
#sync_notes=True
# Set the timezone off set from UTC time. This off set is used to make sure the poller time is set to the
#  same timezone as the QRadar servers timezone. Value must start with + or -, then hours followed by : and then minutes.
#timezone_offset = -4:00
'''
