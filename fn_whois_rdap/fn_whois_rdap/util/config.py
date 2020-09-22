# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_whois_rdap"""

from __future__ import print_function


def config_section_data():
    return """[fn_whois_rdap]
# uncomment to include proxy support
#https_proxy=https://some_proxy.com
#http_proxy=http://some_proxy.com
"""
    