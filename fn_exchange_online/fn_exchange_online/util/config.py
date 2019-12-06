# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_exchange_online"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_exchange_online]
#
# Note that the microsoft_graph_token_url below contains a placeholder {tenant} for the tenant ID.
# Do not place the tenant id in the place holder as the integration will do this at run time.
# In most cases the only required edits are replacing "xxx" with the Microsoft App credentials. 
# 
microsoft_graph_token_url=https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
microsoft_graph_url=https://graph.microsoft.com/v1.0/
tenant_id=xxx
client_id=xxx
client_secret=xxx
"""
    return config_data
