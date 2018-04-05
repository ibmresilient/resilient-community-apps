# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cisco_enforcement"""

from __future__ import print_function

CONFIG_SECTION = "fn_cisco_enforcement"
def config_section_data():

    config_result = """
[fn_cisco_enforcement]
apikey=
    """
    return config_result