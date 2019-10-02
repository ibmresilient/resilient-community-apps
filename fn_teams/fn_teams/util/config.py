# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_teams"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_teams]
# add multiple parameters for the channels to access and their webhook. 
# The channel name is used in the function input: teams_channel
#<channel_name>=<teams channel webhook>
"""
    return config_data