# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_proofpoint"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_proofpoint_tap]
# Required - URL used to make Proofpoint TAP REST API calls
base_url=https://tap-api-v2.proofpoint.com/v2

# Required - Credentials used to authenticate to Proofpoint TAP.
# If API Key and secrets are used, enter the API Key in the
# username parameter and the secret in the password parameter
username=
password=

# Required - How often, in minutes, to check for new events
# To turn the poller off use value 0
polling_interval=

# Optional - How long, in minutes (max 60) to check for previous events at startup
# No entry will use time span equivalent to polling interval
startup_interval=

# Optional - SIEM event type filtering
# Specify the following SIEM event types in a comma separated list:
#    clicks_blocked
#    messages_blocked
#    messages_delivered
#    siem_issues
#    siem_all
# For each event type listed, the poller will call the corresponding
# /siem endpoint to query for those events to convert to an incident/case in SOAR.
# If no event types are specified, the poller defaults to siem_all
siem_event_types=

# Optional filtering - comma separated list of types of events to import into Resilient 
# Options:  malware, phish, spam, impostor, all
# If this configuration value is missing or blank, no filtering
type_filter=

# Optional - Classification for the type of event to import based on the respective threat score
# Scores are floating point values from 0 to 100 and represent minimum malware, spam, phish or impostor scores 
# No entry will ignore the event score values and classify threat based on default TAP event classification
score_threshold=50

# Optional - Jinja template to override default threat description format
threat_template=

# Optional - Jinja template to override default forensic format
forensics_template=

# Optional - If required by Proofpoint
cafile=

# Optional - For access via a proxy
#http_proxy=http://proxyhost:8080
#https_proxy=https://proxyhost:8080
"""
    return config_data
