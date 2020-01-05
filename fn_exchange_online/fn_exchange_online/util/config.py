# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
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
# Do not place '/' at the end of the url strings.
# In most cases the only required edits are replacing "xxx" with the Microsoft App credentials. 
#
microsoft_graph_token_url=https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
microsoft_graph_url=https://graph.microsoft.com/v1.0
tenant_id=xxx
client_id=xxx
client_secret=xxx
#
# You should edit the following parameters for performance if there are many messages and users in your tenant.
# max_messages parameter is used to limit the number of messages returned from a message query.
# max_users parameter is used to limit the number of user mailboxes searched in a message query.
# 
max_messages=100
max_users=2000
"""
    return config_data
