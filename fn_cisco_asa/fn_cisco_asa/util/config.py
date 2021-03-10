# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_asa"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_cisco_asa when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cisco_asa]
# Comma separated list of network object groups to manage: blacklist_in, blacklist_out
network_object_lists=BLACKLIST_IN, BLACKLIST_OUT
#
# Optional Global username and password to be used if not defined in the individual firewall
# sections.
#username=<asa_username>
#password=<asa_password> 
# Optional proxy settings
#http_proxy=
#https_proxy=

# Copy this firewall template for each firewall to be managed. 
# Each firewall_name should be unique. 
# Each firewall section requires a mandatory "host" parameter. 
[fn_cisco_asa:firewall_name]
host=<asa_ip>
username=<asa_username>
password=<asa_password>
#cafile=False
#"""
    return config_data
