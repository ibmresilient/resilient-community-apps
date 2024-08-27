# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2020
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_guardium_insights_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_guardium_insights_integration]
# Resilient classification table ID, should not be modified.
datatable_id=guardium_insights_classification_report

# Guardium Insights IP/DNS
insights_host=

# Guardium Insights Restful Service port, By Default 8443
rest_service_port=8443

# Guardium Insights Restful service API Key Configuration.
insights_encoded_token=

# Periodic time interval to fetch anomalies from GI, poll time should be configured in seconds.
analytics_poll_time=

# delta time range between start time & stop time to retrieve anomalies to create incident, it should be in hrs.
delta_poll_range=2

# classification report period, to populate breach data types data.
# values can be `Now minus 3 hours`,`Now minus 24 hours`, `Now minus 7 days`,`Now minus 14 days`
report_period=Now minus 7 days

# Maximum report records size.
report_fetch_size=500

# This field is optional, To add incident member for created anomaly incidents value can be group name, individual user account.
# If multiple values are specified each should be separated by comma ex: user@domain.com, group_name.
incident_member=

# Guardium http/https proxy server address, leave blank for no proxy
proxy=

# Mention certificate path for SSL/TSL. Default Disabled.
insights_ca_file=false

# false - disable firewall authentication, true - enable firewall authentication
enable_firewall_auth=false

# Firewall Server IP Address
bso_ip=

# Firewall Auth User Name, should be given if `enable_firewall_auth=true`
bso_user=

# Firewall Auth Password, should be given if `enable_firewall_auth=true`
bso_password=
"""
    return config_data