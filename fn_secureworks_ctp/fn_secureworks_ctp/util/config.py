# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_secureworks_ctp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_secureworks_ctp]
# Required - base URL for the Secureworks API.  
# Do not place '/' at the end of the url strings.
base_url=https://api.secureworks.com/api/ticket/v3

# Required - credentials to authenticate to Secureworks CTP.
username=
password=

# Required - Specify the Secureworks CTP ticketType and groupingType pairs that should
# be used in the integration poller to query tickets from the Secureworks endpoint.  
# The possible ticketType are:
#      SERVICE_REQUEST
#      INCIDENT
#      CHANGE
# The possible groupingType are:
#      REQUEST
#      CHANGE
#      HEALTH
#      SECURITY
#
# Ticket-grouping type pairs are specified as colon separated string (no white space):
#      <ticketType>:<groupingType>
#      INCIDENT:SECURITY
#
# The format of query_ticket_grouping_types is a list of comma separated ticket:grouping type pairs.
# Examples to query for all groupingType for each ticketType use one of these string or combine different pairs
# concatenated together with comma separation between pairs:
# query_ticket_grouping_types=SERVICE_REQUEST:REQUEST, SERVICE_REQUEST:CHANGE, SERVICE_REQUEST:HEALTH, SERVICE_REQUEST:SECURITY
# query_ticket_grouping_types=INCIDENT:REQUEST, INCIDENT:CHANGE, INCIDENT:HEALTH, INCIDENT:SECURITY
# query_ticket_grouping_types=CHANGE:REQUEST, CHANGE:CHANGE, CHANGE:HEALTH, CHANGE:SECURITY
#
# Typical users will query INCIDENT ticketType and SECURITY groupingType:
query_ticket_grouping_types=INCIDENT:SECURITY

# Required - Maximum number of tickets to be returned from the /tickets/updates endpoint
query_limit=10

# Required - How often, in seconds, to check for new events
# To turn the poller off use value 0
polling_interval=600

# Optional - Define Secureworks CTP close-codes that override the default values that appear in the select list
# when the Close Incident popup appears when closing an incident. The selected menu item is sent to 
# Secureworks CTP when the ticket is closed in Secureworks. (scwx_ctp_close_codes incident field in Resilient.)
# close_codes is a comma separated list of strings.  Each string is an item in the select list.
#  
# close_codes=Authorized Activity,Confirmed Security Incident,Duplicate,Incident Misidentified,Inconclusive,Not Actionable,Not Vulnerable,Threat Mitigated
close_codes=

# Optional - Path to a custom Jinja template file for the escalated incident.   
# If not defined, the integration will use the default that comes with the integration.
template_file_escalate=

# Optional - Path to a custom Jinja template file for the close of the incident.   
# If not defined, the integration will use the default that comes with the integration.
template_file_close=

# Optional - Path to a custom Jinja template file to update custom fields of the incident.   
# If not defined, the integration will use the default that comes with the integration.
template_file_update=
#
# Optional - If required by Secureworks CTP
cafile=
"""
    return config_data