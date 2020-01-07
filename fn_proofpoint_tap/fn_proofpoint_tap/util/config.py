# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_proofpoint"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_proofpoint_tap]
# Required - URL and credentials to authenticate to Proofpoint TAP
base_url=https://tap-api-v2.proofpoint.com/v2
username=
password=

# Required - How often, in minutes, to check for new events
# To turn the poller off use value 0
polling_interval=

# Optional - How long, in minutes (max 60) to check for previous events at startup
# No entry will use time span equivalent to polling interval
startup_interval=

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
