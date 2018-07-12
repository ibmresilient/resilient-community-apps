# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for rc_cts_urlscanio"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[urlscanio]
# API key for urlscan.io
urlscanio_api_key=xxx

# Optional timeout (seconds)
# timeout=300
    """
    return config_data
