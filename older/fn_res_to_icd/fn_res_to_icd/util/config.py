# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_res_to_icd"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`

    """
    config_data = u"""[fn_res_to_icd]
#Your login details for the ICD platform
icd_email=<YOUR ICD EMAIL>
icd_pass=<YOUR ICD PASSWORD>

#QRadar severity for the resilient incident, maps to an ICD priority if true
#Depends on a custom field on the details incident tab
icd_field_severity=qradar_severity

#If you wish to specify  what ICD ticket priority each resilient incident should map to
# 1 meaning highest priority with 4 being the lowest
icd_priority=<1-4>

#Current URL of icd dashboard
icd_url=https://icdaas.sccd.ibmserviceengage.com/maximo_cbs-dev2
"""
    return config_data