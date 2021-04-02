# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_remedy"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_remedy when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_remedy]
remedy_host=<example.domain>
remedy_user=<example_user>
remedy_password=xxx
#remedy_port=8443
#verify=true
#http_proxy=
#http_proxy=
"""
    return config_data
