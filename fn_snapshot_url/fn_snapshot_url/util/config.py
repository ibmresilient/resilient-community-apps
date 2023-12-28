# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, line-too-long
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.

"""Generate a default configuration-file section for fn_snapshot_url"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_snapshot_url when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_snapshot_url]
# IP address for proxy server
proxy_server=
"""
    return config_data
