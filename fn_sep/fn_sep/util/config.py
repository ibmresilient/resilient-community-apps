# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_sep"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_sep]
base_path=/sepm/api/v1
auth_path=/sepm/api/v1/identity/authenticate
host=<SEPM server dns name or ip address>
port=8446
username=<username>
password=<password>
domain=<SEP domain name>
results_limit=200

"""
    return config_data
