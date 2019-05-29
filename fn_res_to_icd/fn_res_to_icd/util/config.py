# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_res_to_icd"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_res_to_icd]
# Timezone choice, defaults to GMT
time_zone=Etc/GMT
"""
    return config_data
#    return None