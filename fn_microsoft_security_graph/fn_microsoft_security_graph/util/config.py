# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_microsoft_security_graph"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_microsoft_security_graph]
microsoft_graph_url=https://graph.microsoft.com/v1.0/  # Normally should not need to change this
tenant_id=
client_id=<App client id>
client_secret=<App client secret>

# Polling options
# How often polling should happen. Value is in seconds. To disable polling, set this to zero.
msg_polling_interval=0
incident_template=<location_of_template_file>  # If not set uses default template.

# String filter to apply to the alert polling component. This will be added directly to the end of the url
# when searching for alerts, start from the '?'. An example is show below
alert_filter= # ?$filter=assignedTo eq 'analyst@m365x594651.onmicrosoft.com' and severity eq 'high'
"""
    return config_data
