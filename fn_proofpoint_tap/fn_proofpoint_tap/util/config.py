# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_proofpoint"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_proofpoint_tap]
# required - URL and credentials to authenticate to Proofpoint TAP
base_url=https://tap-api-v2.proofpoint.com/v2
username=
password=

# required - how often, in minutes, to check for new events
polling_interval=

# optional - how long, in minutes (max 60) to check for previous events at startup
# no entry will use time span equivalent to polling interval
startup_interval=

# optional filtering - contain at least one of 
# comma separated list of types of events to import into Resilient
# choices:  malware, phish, spam, imposter, all
# if this configuration value is missing or blank, no filtering
type_filter=

# optional classification for the type of event based on the respective threat score
# scores are floating point values from 0 to 100 and represent minimum malware, spam, phish or imposter scores 
# to classify the type of event
# no entry will ignore the event score values and classify threat based on default TAP event classification
score_threshold=50

# optional - Jinja template to override default threat description format
threat_template=

# optional - Jinja template to override default forensic format
forensics_template=

# optional - if required by Proofpoint
cafile=

# optional - for access via a proxy
#http_proxy=http://proxyhost:8080
#https_proxy=https://proxyhost:8080
"""
    return config_data
