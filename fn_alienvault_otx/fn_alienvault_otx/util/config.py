# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_alienvault_otx"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_alienvault_otx]
# OTX API Key to Access the Alien Vault OTX Service 
av_api_key=
#Base URL Path of Alien Vault OTX
av_base_url=https://otx.alienvault.com/api/v1
# Proxy Server by Default it will be None
proxy=
    """
    return config_data