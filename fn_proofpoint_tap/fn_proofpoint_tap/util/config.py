# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_proofpoint"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_proofpoint_tap]
# URL and credentials to authenticate to Proofpoint TAP
base_url=https://tap-api-v2.proofpoint.com/v2
username=
password=

# required - how often, in minutes, to check for new incidents
polling_interval=

# optional - how long, in minutes (max 60) to check for previous events at startup
# no entry will use time span equivalent to polling interval
startup_interval=

# optional - comma separated list of types of incidents to import into Resilient
# choices:  malware, phishing, spam, other, all
# if this configuration value is missing or blank, no filtering
type_filter=

# optional - minimum Proofpoint score required to import into Resilient
# scores are floating point values from 0 to 100
# no entry specifies no score filtering
score_threshold=

# optional - Jinja template to override default threat description format
threat_template=

# optional - Jinja template to override default forensic format
#forensics_template=

# optional
cafile=
"""
    return config_data
