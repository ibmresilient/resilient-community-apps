# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_falcon_sandbox"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
      when called by `resilient-circuits config [-c|-u]`
   """
    return u"""[fn_falcon_sandbox]
falcon_sandbox_api_key=
falcon_sandbox_api_host=https://www.hybrid-analysis.com/api/v2
fetch_report_status_interval=60
fetch_report_timeout=600
"""
