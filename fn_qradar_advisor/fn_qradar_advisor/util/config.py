# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_qradar_advisor"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_qradar_advisor]
qradar_host=myhost
qradar_advisor_token=
qradar_advisor_app_id=
verify_cert=
# Use Case Manager - used to map rule to MITRE tactic
qradar_ucm_token=
# Optional parameters for search and anaylsis (in seconds)
# full_search_timeout=1200
# full_search_period=5
# offense_analysis_timeout=1200
# offense_analysis_period=5
# Settings for access to Qradar Advisor via a proxy
#http_proxy=http://proxy:80
#https_proxy=https://proxy:80
"""
    return config_data
