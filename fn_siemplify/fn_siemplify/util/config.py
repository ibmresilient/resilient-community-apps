# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_siemplify"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_siemplify when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_siemplify]
siemplify_url=<changeme>
api_key=<changeme>
"""
    return config_data
