# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_splunk_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u'''[fn_splunk_integration]
host=localhost
port=8089
username=admin
splunkpassword=changeme
#'''
    return config_data
