# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_tie_functions"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = '''[fn_mcafee_tie]
dxlclient_config=/home/resilient/.resilient/mcafee_tie/dxlclient.config
'''
    return config_data
