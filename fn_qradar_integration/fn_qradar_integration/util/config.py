# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2018. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_qradar_integration]
host=localhost
username=admin
qradarpassword=changeme
"""
#    return config_data
    return None