# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
"""Generate a default configuration-file section for fn_cisco_enforcement"""

from __future__ import print_function

CONFIG_SECTION = "fn_cisco_enforcement"
def config_section_data():

    config_result = """
[fn_cisco_enforcement]
url=https://s-platform.api.opendns.com/1.0
apikey=
protocolversion=1.0a
providerName=Security Platform
    """
    return config_result
