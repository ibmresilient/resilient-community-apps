# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_useragentanalysis"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""
    [fn_useragentanalysis]
    url=https://api.whatismybrowser.com/api/v2/user_agent_parse
    api_key=KEY
    """
    return config_data
