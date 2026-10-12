# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_clamav"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_clamav]
# hostname or ip address of Clamav server
host=localhost
# The TCP port Clamav listens on
port=3310
# Define socket timeout
timeout=500
"""
    return config_data