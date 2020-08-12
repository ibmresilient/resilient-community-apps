# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Generate a default configuration-file section for fn_send_to_staxx"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_anomali_staxx]
staxx_ip=10.10.10.10
staxx_port=8080
staxx_user=someuser
staxx_password=somepass
# uncomment for proxy settings
#https_proxy=
#http_proxy=
"""
    return config_data