# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_ansible_tower"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_ansible_tower]
username=
password=
url=
cafile=False
"""
    return config_data
