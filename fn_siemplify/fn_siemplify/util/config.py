# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_siemplify"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_siemplify when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_siemplify]
base_url=<changeme>
api_key=<changeme>
# false|/path/to/certificate
cafile=
# specify the environment for creating cases and entities
default_case_environment=Default Environment
# override default Siemplify and SOAR templates as necessary
siemplify_create_case_template=
siemplify_close_case_template=
"""
    return config_data
