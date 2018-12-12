# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_phish_ai"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_phish_ai]
#phishai_api_key=<phish.ai_api_key>
## Timeout to return report report in seconds, defaults to 60 seconds
#timeout_seconds=60
"""
    return config_data
