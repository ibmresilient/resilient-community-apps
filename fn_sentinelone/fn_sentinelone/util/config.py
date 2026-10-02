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
# OPTIONAL: Comma separated list of SentinelOne account Ids to query for threats by poller
account_ids=
# OPTIONAL: Comma separated list of SentinelOne site Ids to query for threats by poller
site_ids=
# OPTIONAL: "query" parameter for querying threats in SentinelOne
query_param=
# OPTIONAL: incidentStatuses parameter for querying threats from SentinelOne
incident_statuses=resolved,in_progress,unresolved
# OPTIONAL: "limit" parameter: limit the number of threats returned from querying threats from SentinelOne
limit=25
# OPTIONAL: sortBy parameter used when querying SentinelOne threats
sort_by=createdDate
# OPTIONAL: sortOrder for SentinelOne threat query results. Possible values: asc or desc
sort_order=desc
# OPTIONAL: send SOAR case URL live link via threat note to SentinelOne
send_soar_link_to_sentinelone=true
# OPTIONAL: Override value for templates used for creating/updating/closing SOAR cases
# soar_create_case_template=
# soar_close_case_template=
# soar_update_case_template=
# OPTIONAL: use the 'verify' config to set a value for SSL verification
# if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
# will be used. if 'verify' is a path, the value of the path will override the
# root cert bundle and the file found at the path will be used for server-side SSL.
# verify = True
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
"""
    return config_data
