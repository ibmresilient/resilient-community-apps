# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_query_tor_network"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_query_tor_network]
base_url = https://onionoo.torproject.org/details
flag = Exit  
data_fields = exit_addresses,or_addresses,host_name"""

    return config_data