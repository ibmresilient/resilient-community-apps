# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_zia"""

REQUIRED_CONFIG_SETTINGS = ["zia_api_base_url", "zia_username", "zia_password",
                            "zia_api_key"]

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_zia when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_zia]
zia_api_base_url = <ZIA_API_BASE_URL>
zia_username = <ZIA_USER_NAME>
zia_password = <ZIA_PASSWORD>
zia_api_key = <ZIA_API_KEY>
#http_proxy=http://proxy:80
#https_proxy=https://proxy:443
"""
    return config_data
