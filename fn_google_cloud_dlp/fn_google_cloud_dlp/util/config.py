# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_google_cloud_dlp"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_google_cloud_dlp]
gcp_project=<YOUR_GOOGLE_PROJECT_ID>
gcp_dlp_masking_char=#
"""
    return config_data
