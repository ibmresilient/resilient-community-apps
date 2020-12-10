# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2020. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u'''[fn_qradar_integration]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
#verify_cert=falsse|/path/to/cert
#search_timeout=
'''
    return config_data