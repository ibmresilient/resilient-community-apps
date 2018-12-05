# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_microsoft_security_graph"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_microsoft_security_graph]
# Graph URL with version number
microsoft_graph_url=https://graph.microsoft.com/v1.0/
tenant_id=<Tenant directory id>
client_id=<App client id>
client_secret=<App client secret>

## Polling options
# How often polling should happen. Value is in seconds. To disable polling, set this to zero.
msg_polling_interval=0
#incident_template=<location_of_template_file>  # If not set uses default template.

# String query to apply to the alert polling component. This will be added to the end of the url
# when searching for alerts. The example shown below would make the whole search url equal to
# https://graph.microsoft.com/v1.0/security/alerts/?$filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'
# This query string is full OData so alert query can start with 'top=', 'skip=', 'filter=', etc. Do not add a '$' at the start
# of the value as that character is reserved for environment variables
#alert_query=filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'

# Alert Time range sec - Optional value in seconds to set the start dateTime values for the createdDateTime field when filtering alerts.
# This is calculated by adding to the filter 'createdDateTime ge (current_dateTime - alert_time_range_sec)
#alert_time_range_sec=3600
"""
    return config_data
