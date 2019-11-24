# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_exchange_online"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_exchange_online]
microsoft_graph_url=https://graph.microsoft.com/v1.0/
tenant_id=xxx
client_id=xxx
client_secret=xxx
"""
    return config_data
