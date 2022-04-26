# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_abuseipdb"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_abuseipdb when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_abuseipdb]
abuseipdb_url=https://api.abuseipdb.com/api/v2/check
abuseipdb_key=[your api key from your AbuseIPDB account]
ignore_white_listed=True
"""
    return config_data
