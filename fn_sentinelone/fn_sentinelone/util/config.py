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
sentinelone_server=
# SentinelOne REST API version
api_version=2.1
# SentinelOne API token
api_token=

# SentinelOne poller settings
# Poller interval in seconds, comment out or set to 0 to disable poller
polling_interval=60
# Poller timeback time first time, in minutes
polling_lookback=120
# Comma separated list of SentinelOne account Ids to query for threats by poller
account_ids=
# Comma separated list of SentinelOne site Ids to query for threats by poller
site_ids=
# Optional "query" parameter for querying threats in SentinelOne
query_param=
# Optional "resolved" parameter for querying threats from SentinelOne
# If set to False "resolved" threats will not be escalated to SOAR 
resolved=False
# Optional timeout in seconds for downloading threat file from SentinelOne
# timeout=300
#verify=false | /path/toclient_certificate.pem
#http_proxy=
#https_proxy=
"""
    return config_data
