# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_asa"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_cisco_asa when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cisco_asa]
# Comma separated list of firewalls to manage: firewall_1[,firewall_2]
firewalls=firewall_1
# Optional proxy settings
#http_proxy=
#https_proxy=

# Copy this firewall template for each firewall to be managed. 
# There should be a section for each firewall defined in the above
# [fn_cisco_asa] "firewalls" comma seperated list.
[fn_cisco_asa:firewall_1]
host=<asa_ip>
username=<asa_username>
password=<asa_password>
outbound_network_object_group=BLACKLIST_OUT
inbound_network_object_group=BLACKLIST_IN
#cafile=False
#"""
    return config_data
