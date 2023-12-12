# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_parse_utilities"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_parse_utilities when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_parse_utilities]

    # This is the path to your transformation file directory. Do not include the filename.
    xml_stylesheet_dir = /path/to/stylesheet/directory/
    """
    return config_data
