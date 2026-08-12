# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# Generated with resilient-sdk v51.0.1.1.824

"""Generate a default configuration-file section for fn_vmware_cbc"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_vmware_cbc when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_vmware_cbc]
# VMware Carbon Black Cloud hostname
hostname=https://xxx
# VMware Carbon Black Cloud API ID
api_id=xxx
# VMware Carbon Black Cloud API secret
api_secret=xxx
# VMware Carbon Black Cloud organization key
org_key=xxx
# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs.
# Default lookback is 2 weeks (in minutes), similar to default in Carbon Black UI. 
polling_lookback=230400
#
# OPTIONAL: polling filters criteria can be applied when querying Vmware Carbon Black Cloud for new alerts.
#   Each filter is a tuple containing key, value pairs in the following format: ("field","values")
#   Where:
#       "field" is the Carbon Black Cloud alert field to be queried
#       "values" is an int, bool, list or string object
#   some example of alert criteria "field" values that can be queried are:
#       "workflow_status", "minimum_severity", "tags"
#   See CBC documentation here: https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/alert-search-fields
#   for all possible searchable alert fields.
#   Denote lists enclosed in square brackets [].
#
polling_filters_criteria_1 = ("minimum_severity",3),("workflow_status",["OPEN","IN_PROGRESS","CLOSED"])
#
# OPTIONAL: polling filters exclusions can be applied when querying Vmware Carbon Black Cloud for new alerts.
#   Each filter is a tuple containing key, value pairs in the following format: ("field","values")
#   Where:
#       "field" is the Carbon Black Cloud alert field to be queried
#       "values" is a comma separated string of values to include in the query results returned 
#   some alert "field" values that can be queried are:
#       "workflow_status", "minimum_severity", "sources", "tags"
#   See CBC documentation here: https://developer.carbonblack.com/reference/carbon-black-cloud/platform/latest/alert-search-fields
#   for all possible searchable alert fields.
#   Denote lists enclosed in square brackets [].
# polling_filters_exclusions_1 = ("workflow_status",["CLOSED"])
#
# OPTIONAL: Allow for a second and third set of polling filter criteria and exclusions for each polling interval.
#   See above for formatting instructions.
# polling_filters_criteria_2 = ("minimum_severity",3),("workflow_status",["OPEN","IN_PROGRESS","CLOSED"]),("reputation",["KNOWN_MALWARE","PUP","SUSPECT_MALWARE","COMPANY_BLACK_LIST"]),("alert_type",["CB_ANALYTICS", "WATCHLIST"])
# polling_filters_exclusions_2 = ("workflow_status",["CLOSED"])
# polling_filters_criteria_3 = ("minimum_severity",1),("workflow_status",["OPEN","IN_PROGRESS","CLOSED"]),("target_value",["LOW","MEDIUM","HIGH","MISSION_CRITICAL"]),("alert_type",["CB_ANALYTICS"])
# polling_filters_exclusions_3 = ("workflow_status",["CLOSED"])
#
#
# OPTIONAL: default job timeout in seconds
# job_timeout = 120
#
# OPTIONAL: default job sleep interval in seconds
# job_sleep_interval = 1
# 
# OPTIONAL: Override value for templates used for creating/updating/closing SOAR cases
# soar_create_case_template=
# soar_close_case_template=
# soar_update_case_template=
#
# # Specify paths to files if client certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
# """
    return config_data