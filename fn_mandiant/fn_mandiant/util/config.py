# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
# Generated with resilient-sdk v50.0.108

"""Generate a default configuration-file section for fn_mandiant"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_mandiant when called by `resilient-circuits config [-c|-u]`
    """
    config_data = """

    [fn_mandiant]

    # api_key = API Key V4 required to connect to Mandiant endpoint
    # api_secret = API Secret for the above API Key

    """
    return config_data
