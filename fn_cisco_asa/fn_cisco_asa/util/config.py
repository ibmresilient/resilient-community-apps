# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_asa"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_cisco_asa when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cisco_asa]
host=
username=
password=
outbound_network_object_group=BLACKLIST_OUT
inbound_network_object_group=BLACKLIST_IN
is_asav=True
#cafile=False
# Optional proxy settings
#http_proxy=
#https_proxy=
#"""
    return config_data
