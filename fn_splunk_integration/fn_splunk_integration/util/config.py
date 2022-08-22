# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_splunk_integration"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u'''
[fn_splunk_integration:splunk_label1]
host=localhost
port=8089
username=admin
splunkpassword=changeme
verify_cert=false|/path/to/cert

[fn_splunk_integration:splunk_label2]
host=localhost
port=8089
username=admin
splunkpassword=changeme
verify_cert=false|/path/to/cert
'''
