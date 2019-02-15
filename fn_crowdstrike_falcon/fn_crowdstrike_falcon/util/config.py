# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_crowdstrike_falcon"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_crowdstrike_falcon]
# API Client Authentication, CrowdStrike's newer standard based on OAuth2. See README doc on how to obtain credentials
cs_falcon_oauth2_base_url=https://api.crowdstrike.com
cs_falcon_oauth2_cid=
cs_falcon_oauth2_key=

# API Key Authentication, CrowdStrike's legacy authentication standard
cs_falcon_bauth_base_url=https://falconapi.crowdstrike.com
cs_falcon_bauth_api_uuid=
cs_falcon_bauth_api_key=

# Number of seconds to wait before next request to CrowdStrike. Default=5
cs_falcon_ping_delay=

# Max number of seconds to wait to get response from CrowdStrike. Default=120
cs_falcon_ping_timeout=
"""
    return config_data
