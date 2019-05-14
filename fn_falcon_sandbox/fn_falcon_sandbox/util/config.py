# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_falcon_sandbox"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
   """
    return u"""[fn_falcon_sandbox]
falcon_sandbox_api_key=0wc8s84sc044wwokg0g0gogw4o0sogoo08sk8k80kgo8s4oc8ksoo0g8wok04g8k
falcon_sandbox_api_host=https://www.hybrid-analysis.com/api/v2
fetch_report_timeout=600
"""
