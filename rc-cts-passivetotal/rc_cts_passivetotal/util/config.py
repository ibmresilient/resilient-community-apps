# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_cts_urlscanio"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[passivetotal]
# API key for passivetotal
passive_api_key=xxx

# Username
passive_user=me@my.com

# Tags that result in a hit
passive_tags=Compromised,Ransomware
    """
    return config_data
