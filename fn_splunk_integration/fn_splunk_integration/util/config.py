# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_splunk_integration"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u'''
# V1.1.0+ have the option to have multiple servers configured.
# By default two examples of servers are given, example one is labeled `splunk_label1` and example two is labeled `splunk_label2`.
# The label for a server is placed after `[fn_splunk_integration:` and then followed by `]`.
# To add additional servers copy the below example server configuration from `[fn_splunk_integration:splunk_label1]` to `verify_cert=false|/path/to/cert`.
# Then paste it at the bottom of the app.config.
# Change the server label, `splunk_label1`, to a label helpful to define that server.
# Then change the setting to those of the server you wish to add.

# If token is given then username/password will be disregarded
[fn_splunk_integration:splunk_label1]
host=localhost
port=8089
username=admin
splunkpassword=changeme
#token=
verify_cert=false|/path/to/cert

[fn_splunk_integration:splunk_label2]
host=localhost
port=8089
username=admin
splunkpassword=changeme
#token=
verify_cert=false|/path/to/cert
'''
