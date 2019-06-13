# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_res_to_icd"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_res_to_icd]
icd_email=<YOUR ICD EMAIL>
icd_pass=<YOUR ICD PASSWORD>
icd_qradar_severity=<True or False>
icd_priority=<1-4>
"""
    return config_data