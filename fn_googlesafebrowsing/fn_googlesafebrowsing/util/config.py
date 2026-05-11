# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_googlesafebrowsing"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_googlesafebrowsing when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_googlesafebrowsing]
googlesafebrowsing_url=https://safebrowsing.googleapis.com/v4/threatMatches:find?key=
googlesafebrowsing_api_key=
"""
    return config_data
