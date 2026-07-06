# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v50.1.262

"""Generate a default configuration-file section for fn_rapid7_insight_idr"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_rapid7_insight_idr when called by `resilient-circuits config [-c|-u]`
    """
    config_data = None

    config_data = u"""[fn_rapid7_insight_idr]
# Rapid7 InsightIDR API key
api_key = <api_key>
#
# Rapid7 InsightIDR API version
api_version = v2
#
# Rapid7 Insight Platform Data Storage Region
# Examples: us, us2, us3, ca, eu, ap, au
region = <your Rapid7 data region code>
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval = 60
#
# Number of minutes to lookback when querying for investigations the first time the poller runs.
polling_lookback = 1200
#
# OPTIONAL: Rapid7 InsightIDR organization token
#   The org_token is used to form the URL link from SOAR to the InsightIDR investigation.
#   If the org_token is not defined, the URL link from SOAR back to Rapid7 does not take you 
#   to the corresponding investigation in Rapid7.
#   Get the org_token by navigating to an investigation in the Rapid7 InsightIDR platform in a
#   browser. The org_token is the string that appears in between string fragments "/op/" and 
#   "/investigations" of the investigation URL.  The string ends with the # character, which 
#   you should include in the org_token string.
# 
org_token = <your org token>
#
# OPTIONAL: polling filters can be applied when querying Rapid7 InsightIDR for new investigations.
#   Each filter is a tuple containing 2 strings in the following format: ("field","values")
#   Where:
#       "field" is the Rapid7 InsightIDR investigation field to be queried
#       "values" is a comma separated string of values to include in the query results returned 
#   he following investigation "field" values that can be queried are:
#       "priorities", "statuses", "sources", "tags"
#   NOTE: Each individual filter is first constructed by joining together the field and the 
#   desired values using OR statements. Each individual filter is then combined using AND.
#   polling_filters = ("priorities","LOW,MEDIUM,HIGH,CRITICAL"),("statuses","OPEN,INVESTIGATING,WAITING,CLOSED"), ("sources","USER,ALERT")
polling_filters = ("priorities","HIGH,CRITICAL"),("statuses","OPEN,INVESTIGATING,WAITING")
#
# OPTIONAL: Flag indicating whether or not poller adds SOAR case URL in comment in the Rapid7 InsightIDR investigation.
polling_add_case_url_comment_in_rapid7 = True
#
# OPTIONAL: Specify a timeout value value for accessing the Rapid7 InsightIDR REST API
# timeout=60
#
# OPTIONAL: Override value for templates used for creating/updating/closing SOAR cases
# soar_create_case_template=
# soar_close_case_template=
# soar_update_case_template=
#
# OPTIONAL: use the 'verify' config to set a value for SSL verification
#   if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
#   will be used. if 'verify' is a path, the value of the path will override the
#   root cert bundle and the file found at the path will be used for server-side SSL.
# verify = True
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
"""
    return config_data
