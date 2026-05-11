# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019


"""Generate a default configuration-file section for fn_task_utils"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = """[fn_task_utils]
# Set this to true to automatically include the user's name and email
add_user_info_to_note=False
"""
    return config_data