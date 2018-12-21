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
#The Flag can be 'Running','Exit' for more information on flag settings - https://metrics.torproject.org/onionoo.html
flag = Exit
# The data fields should be comma separated and no space should be given in between each fields  
data_fields = exit_addresses,or_addresses,host_name"""

    return config_data