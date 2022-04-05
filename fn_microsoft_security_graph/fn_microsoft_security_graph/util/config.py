# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_microsoft_security_graph"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""[fn_microsoft_security_graph]
#
# Note that the microsoft_graph_token_url below contains a placeholder {tenant} for the tenant ID.
# Do not place the tenant id in the place holder as the integration will do this at run time.
# Do not place '/' at the end of the url strings.
# In most cases the only required edits are replacing xxx with the Microsoft App credentials.
#
microsoft_graph_token_url=https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
microsoft_graph_url=https://graph.microsoft.com/v1.0
tenant_id=xxx
client_id=xxx
client_secret=xxx

## Polling options
# How often polling should happen. Value is in seconds. To disable polling, set this to zero.
msg_polling_interval=0
# Location of jinja template file to escalate incidents.
# If not set, default template is used.
incident_template=

# String query to apply to the alert polling component. This will be added to the end of the url
# when searching for alerts. The example shown below would make the whole search url equal to
# https://graph.microsoft.com/v1.0/security/alerts/?$filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'
# This query string is full OData so alert query can start with 'top=', 'skip=', 'filter=', etc. Do not add a '$' at the start
# of the value as that character is reserved for environment variables
# alert_query=filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'
# Query only alerts that are not resolved by default:
alert_query=filter=status ne 'resolved'

# Alert Time range sec - Optional value in seconds to set the start dateTime values for the createdDateTime field when filtering alerts.
# This is calculated by adding to the filter 'createdDateTime ge (current_dateTime - alert_time_range_sec)
# alert_time_range_sec=3600
alert_time_range=
"""
