# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_secureworks_ctp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_secureworks_ctp]
# Required - URL and credentials to authenticate to Secureworks CTP
base_url=https://api.secureworks.com/api/ticket/v3
username=
password=

# Required - Query Secureworks CTP tickets of type: SERVICE_REQUEST, INCIDENT, CHANGE
query_ticket_types=INCIDENT

# Required - Query Secureworks CTP tickets of group: REQUEST, CHANGE, HEALTH, SECURITY
query_grouping_types=SECURITY

# Required - Maximum number of tickets to be returned from the /tickets/updates endpoint
query_limit=10

# Required - Boolean: true: returns only tickets assigned to the client. false: returns all tickets.
assigned_to_customer=true

# Required - How often, in minutes, to check for new events
# To turn the poller off use value 0
polling_interval=600

# Optional - If required by Secureworks CTP
cafile=
"""
    return config_data