# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_cloud_foundry"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_cloud_foundry]
cf_api_base=xxx
cf_api_apikey=xxx
cf_api_username=xxx
cf_api_password=xxx
    """
    return config_data
