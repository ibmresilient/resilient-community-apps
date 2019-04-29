# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_spamhaus_query"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_spamhaus_query]
# The API endpoint URL to query Spamhaus Web Query Service
spamhaus_wqs_url = https://apibl.spamhaus.net/lookup/v1/{}/{}
spamhaus_dqs_key = 
ip_resource_list = ['SBL','XBL','PBL','SBL-XBL','ZEN','MSR','AUTHBL']
domain_resource_list = ['ZRD','DBL']
# Proxy Configuration if any by default will be None
http_proxy=
https_proxy=
"""
    return config_data
