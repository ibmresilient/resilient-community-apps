# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_urlscanio"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[urlscanio]
# API key for urlscan.io
urlscanio_api_key=xxx
# Base URL for the urlscanio API
urlscanio_report_url=https://urlscan.io/api/v1
# Base URL to access screenshots in urlscanio
urlscanio_screenshot_url=https://urlscan.io/screenshots

# Optional timeout (seconds)
# timeout=300
    """
    return config_data

