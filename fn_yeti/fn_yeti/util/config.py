# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_yeti"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_yeti when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_yeti]
urlbase=<yeti_server_url>
username=yeti
password=
api_key=<api_key_value>
"""
    return config_data
