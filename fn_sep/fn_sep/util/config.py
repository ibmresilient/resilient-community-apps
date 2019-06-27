# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_sep"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_sep]
sep_base_path=/sepm/api/v1
sep_auth_path=/sepm/api/v1/identity/authenticate
sep_host=<SEPM server dns name or ip address>
sep_port=8446
sep_username=<username>
sep_password=<password>
sep_domain=<SEP domain name>
# Limit result sent to Resilient, add full result as an attachment.
sep_results_limit=200
# Period of time to wait for all endpoints to return a scan result.
sep_scan_timeout=1800
"""
    return config_data
