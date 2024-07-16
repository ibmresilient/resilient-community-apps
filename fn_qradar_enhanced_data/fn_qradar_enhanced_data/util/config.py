# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return '''
#Settings that apply to all QRadar servers
[fn_qradar_integration:edm_global_settings]
#search_timeout=
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
# specify empty_query settings to indicate what to do when an AQL query returns empty results,
#  empty_query_max will attempt the AQL queries up to the number of times specified. Default is no retries (1)
#empty_query_max=
#  empty_query_wait_secs will pause the number of seconds before attempting the next query. Default is 0
#empty_query_wait_secs=
#  comma separated list of query types to skip retry: topevents, flows, sourceip, destinationip, categories
#empty_query_skip_types=

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
#Note, if both qradarpassword and qradartoken are given, password will be used.
# qradartoken must be configured to use the MITRE function.
qradartoken=changeme
verify_cert=false|/path/to/cert
#search_timeout=
# If true then notes that are added to QRadar offenses will be added to their linked SOAR incidents
#sync_notes=True

# Note: the QRadar instance name that you want to communicate with, must equal the
# QRadar Destination Name that is set when configuring the SOAR Plugin
# Example: SOAR_Plugin_Destination_Name2
[fn_qradar_integration:SOAR_Plugin_Destination_Name2]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used.
# qradartoken must be configured to use the MITRE function.
qradartoken=changeme
verify_cert=false|/path/to/cert
#search_timeout=
# If true then notes that are added to QRadar offenses will be added to their linked SOAR incidents
#sync_notes=True
'''
