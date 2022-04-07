# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_remedy"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_remedy when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_remedy]
# Hostname or IP for the Remedy instance.
remedy_host=<example.domain>
# Username to use to authenticate with Remedy.
remedy_user=<example_user>
# Password to use to authenticate with Remedy.
remedy_password=xxx
# Max number of datatable rows to return from the SOAR API when closing an Incident.
max_datatable_rows=30
# Port number over which the Remedy REST API is exposed.
#remedy_port=8443
# Set to true or /path/to/cerficate.crt to make verified requests to Remedy, else set to false
#verify=true|false|/path/to/certificate.crt
#https proxy for request traffic.
#https_proxy=
"""
    return config_data
