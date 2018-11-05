# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Generate a default configuration-file section for fn_google_cloud_functions"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_google_cloud_functions]
gcp_region = <GCP_REGION_ID>
gcp_project_id = <GCP_PROJECT_ID>
gcp_function_name = <NAME_OF_CLOUD_FUNCTION>
# Optional Config values
#gcp_http_proxy = None
#gcp_https_proxy = None
"""
    return config_data
