# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cve_search"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cve_search]
# Flag display maximum CVE Entries on the resilient table
max_results_display = 50
# Base URL of Common Vulnerability Exposures Data Base.
cve_base_url = https://cve.circl.lu/api
"""
    return config_data