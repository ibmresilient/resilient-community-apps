# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_sndbox_analyzer"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_sndbox_analyzer]
# Your SNDBOX API Key                                                         
sndbox_api_key=

# Your SNDBOX Server URL, using https://api.sndbox.com if empty.
sndbox_analyzer_url=https://api.sndbox.com
             
# Amount of time in seconds to wait until checking if the report is ready again.
sndbox_analyzer_report_request_timeout=60 
"""
    return config_data