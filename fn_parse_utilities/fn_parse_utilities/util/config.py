# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_parse_utilities"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_parse_utilities when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_parse_utilities]

    xml_stylesheet_dir =
    """
    return config_data
