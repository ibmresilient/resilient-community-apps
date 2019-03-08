# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_rsa_netwitness"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_rsa_netwitness]
nw_packet_server_url=<http://test.nw_packet_server.com:50104>
nw_packet_server_port=<port for communication>
nw_packet_server_user=<nw_packet_server_username>
nw_packet_server_password=<nw_packet_server_password>
nw_packet_server_cafile=[true|false]

nw_log_server_url=<http://test.nw_log_server.com:50102>
nw_log_server_port=<port for communication>
nw_log_server_user=<nw_log_server_username>
nw_log_server_password=<nw_log_server_password>
nw_log_server_cafile=[true|false]
"""
    return config_data
