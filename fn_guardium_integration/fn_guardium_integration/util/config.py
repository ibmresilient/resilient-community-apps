# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

"""Generate a default configuration-file section for fn_guardium_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_guardium_integration]
# Search results data table ID, should not be changed
search_table=guardium_search_report_data

# Search Sensitive objects table ID, should not be changed
sensitive_table=grd_sensitive_objects

# Search Outlier Details table ID, should not be changed
outlier_table=grd_outlier_details
 
# false - disable firewall authentication, true - enable firewall authentication
enable_firewall_auth=false

# Firewall Server IP Address
bso_ip=

# Firewall Auth User Name, should be given if `enable_firewall_auth=true`
bso_user=

# Firewall Auth Password, should be given if `enable_firewall_auth=true`
bso_password=

# Guardium http/https proxy server address, leave blank for no proxy
# Example https://proxy_server.com:8080
proxy=

# The  proxy command  to generate the client secret if  a proxy is being used. 
#Can be left blank if no proxy .Ex: /usr/bin/nc --proxy proxy.bar.com:8080 target_host target_port.
proxy_command=

# Guardium Host IP/DNS
guardium_host=

# Guardium Restful service port.
port=8443

# Guardium User Name
guardium_user=

# Guardium password
guardium_password=

# SSL/TLS
guardium_cert=false


# Q-Radar Block group, The group which will be used to block the user access to database
q_radar_block_group=QRadarBlockingConnection

# Q-Radar block group policy Name
block_policy_name=QRadarPolicyClone

# The following parameters 'cli_user' and 'cli_password' are used for the package selftest function.
# These parameters should be defined only when the package selftest functionality is being used.
cli_user=
cli_password=
"""
    return config_data
