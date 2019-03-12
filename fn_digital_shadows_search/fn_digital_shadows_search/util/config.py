# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_digital_shadows_search"""

from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_digital_shadows_search]
ds_api_key=
ds_api_secret=
ds_base_url=https://portal-digitalshadows.com
"""
    return config_data
