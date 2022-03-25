# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_shadowserver"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_shadowserver when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_shadowserver]
shadow_server_url=http://bin-test.shadowserver.org/api
"""
    return config_data
