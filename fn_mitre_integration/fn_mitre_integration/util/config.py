# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_mitre_integration"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_mitre_integration]
# Settings for access to Mitre via a proxy
#http_proxy=http://proxy:80
#https_proxy=https://proxy:80
"""
    return config_data