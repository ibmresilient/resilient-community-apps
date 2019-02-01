# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_rsa_netwitness"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_rsa_netwitness]
nw_url=<https://test.nw_server.com>
nw_port=<default port for communication>
nw_user=<nw_username>
nw_password=<nw_password>
cafile=[true|false]
"""
    return config_data
