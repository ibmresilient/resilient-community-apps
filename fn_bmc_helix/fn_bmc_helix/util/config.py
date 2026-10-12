# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_bmc_helix"""

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_bmc_helix when called by `resilient-circuits config [-c|-u]`
    """

    return """[fn_bmc_helix]
# Hostname or IP for the BMC Helix instance.
helix_host=<example.domain>
# Username to use to authenticate with BMC Helix.
helix_user=<example_user>
# Password to use to authenticate with BMC Helix.
helix_password=xxx
# Max number of datatable rows to return from the SOAR API when closing an Incident.
max_datatable_rows=30
# Port number over which the BMC Helix REST API is exposed.
#helix_port=8443
# Set to true or /path/to/cerficate.crt to make verified requests to BMC Helix, else set to false
#verify=true|false|/path/to/certificate.crt
#https proxy for request traffic.
#https_proxy=
"""
