# -*- coding: utf-8 -*-
# (c) Copyright IBM Corporation 2010, 2019. All Rights Reserved.

"""Generate a default configuration-file section for fn_bluecoat_site_review"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_bluecoat_site_review]
url=https://sitereview.bluecoat.com/resource/lookup
"""
    return config_data

