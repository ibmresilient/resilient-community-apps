# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mcafee_opendxl"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mcafee_opendxl]
dxlclient_config=/home/integration/.resilient/mcafee/dxlclient.config
"""
    return config_data
