# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_shodan"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_shodan when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_shodan]
shodan_apikey=<your-api-key>
http_proxy=
https_proxy=
"""
    return config_data
