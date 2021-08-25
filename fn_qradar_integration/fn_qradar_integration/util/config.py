# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u'''[fn_qradar_integration:QRadar.label1]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false
#search_timeout=

[fn_qradar_integration:QRadar.label2]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false
#search_timeout=

'''
    return config_data