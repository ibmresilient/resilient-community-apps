# -*- coding: utf-8 -*-
"""Generate a default configuration-file section for fn_virustotal"""


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """[fn_virustotal]
api_token=
polling_interval_sec=60
max_polling_wait_sec=600
"""
