# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.

"""Generate a default configuration-file section for fn_ipinfo"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ipinfo]
ipinfo_access_token=my_access_token
"""
    return config_data