# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_api_void"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_api_void when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_api_void]
apivoid_base_url=https://endpoint.apivoid.com
apivoid_sub_url=v1/pay-as-you-go
apivoid_api_key=<your-api-key>
"""
    return config_data
