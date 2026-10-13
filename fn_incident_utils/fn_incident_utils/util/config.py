# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_incident_utils"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_incident_utils when called by `resilient-circuits config [-c|-u]`
    """
    config_data = """[fn_incident_utils]
#values: partial, normal, full
search_result_level=full
"""

    return config_data
