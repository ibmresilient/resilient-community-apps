# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_sentinelone"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_sentinelone when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_sentinelone]
# SentinelOne server
sentinelone_server=usea1-partners.sentinelone.net
# SentinelOne REST API version
api_version=2.1
# SentinelOne site token
api_token=bkhAs8WdkRfxVA3jsBT7CIOsgrBqFeWVsMVJwio8FsQ9YwKYPnMcA3JOtTTBgjze3gz7goz72rNY8NLl
# poller timeback time first time, in minutes
polling_lookback=120
# Poller settings
# poller interval in seconds, comment out or set to 0 to disable poller
polling_interval=60
#cafile=<path to certificate file>
#http_proxy=http://proxy:80
#https_proxy=https://proxy:443
"""
    return config_data
