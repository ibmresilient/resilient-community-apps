# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_joesandbox"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    
    config_data = u"""
      [fn_joesandbox]
      fn_joesandbox_api_key=
      fn_joesandbox_analysis_url=https://jbxcloud.joesecurity.org/analysis
    """
    return config_data
