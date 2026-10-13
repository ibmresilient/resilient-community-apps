# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_whois"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_whois]
#whois_https_proxy=http://0.0.0.0:3128/
"""
    return config_data