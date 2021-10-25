# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2021. All Rights Reserved.
"""Generate a default configuration-file section for fn_qradar_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u'''
#Note, QRadar.label must equal the QRadar Destination Name that is set in the SOAR plugin
[fn_qradar_integration:qradar_1_1_1_1]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false
#search_timeout=

#Note, QRadar.label must equal the QRadar Destination Name that is set in the SOAR plugin
[fn_qradar_integration:qradar_192_168_0_3]
host=localhost
username=admin
qradarpassword=changeme
#Note, if both qradarpassword and qradartoken are given, password will be used
qradartoken=changeme
verify_cert=false
#search_timeout=

'''
    return config_data