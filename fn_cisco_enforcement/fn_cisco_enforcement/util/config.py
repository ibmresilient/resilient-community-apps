# -*- coding: utf-8 -*-
# Copyright IBM Corp. - Confidential Information
"""Generate a default configuration-file section for fn_cisco_enforcement"""

from __future__ import print_function

CONFIG_SECTION = "fn_cisco_enforcement"
def config_section_data():

    config_result = """
[fn_cisco_enforcement]
apikey=
cisco_deviceid=
cisco_deviceversion=
cisco_protocolversion=
    """
    return config_result
