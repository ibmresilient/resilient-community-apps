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
# Optional incidentStatuses parameter for querying threats from SentinelOne
incident_statuses=resolved,in_progress,unresolved
# Optional "limit" parameter: limit the number of threats returned from querying threats from SentinelOne
limit=25
# Optional sortBy parameter used when querying SentinelOne threats
sort_by=createdDate
# Optional sortOrder for SentinelOne threat query results. Possible values: asc or desc
sort_order=desc
# Optional: send SOAR incident URL live link via threat note to SentinelOne
send_soar_link_to_sentinelone=true
# Custom templates to replace the default map of SentinelOne threat fields to SOAR incident fields
#create_incident_template=
#update_incident_template=
#close_incident_template=
# Optional path to SSL certificate
#verify=false | /path/toclient_certificate.pem
# Optional proxy settings
#http_proxy=
#https_proxy=
"""
    return config_data
