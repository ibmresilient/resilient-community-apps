# -*- coding: utf-8 -*-
"""Generate a default configuration-file section for fn_jira"""
from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return """
[fn_jira:global_settings]
# Maximum time in seconds to wait before timeout.
timeout=30
# Interval to poll Jira for changes (in seconds)
# When polling_interval equals 0 the poller is off
polling_interval=0
polling_lookback=60
# Search filters for Jira issue to sync with SOAR cases.
# If poller_filters under [fn_jira:global_settings] is configured, then poller_filters
#  that are configured under the individual Jira servers are ignored
#poller_filters= priority in (high, medium, low) and status in ('to do', 'in progress', done) and project in (project_name1, project_name2)
# Defaults to true. Either true or false. If true the poller creates new SOAR incidents from Jira issues that match the given filters.
create_soar_incidents = true
# Max number of issues that can be returned from Jira issue search.
# If max_issues_returned under [fn_jira:global_settings] is configured, then max_issues_returned
#  that are configured under the individual Jira servers are ignored.
max_issues_returned = 50
# Proxies to use
# If proxies are defined under [fn_jira:global_settings], then proxies defined
#  under the individual Jira servers are ignored
#https_proxy=
# OPTIONAL: override value for templates used for creating/updating/closing SOAR cases.
# If templates under the individual Jira servers are configured, then templates
#  that are configured under [fn_jira:global_settings] are ignored.
# See documentation section "Templates for SOAR Cases" for more details
#soar_create_case_template=
#soar_update_case_template=
#soar_close_case_template=

[fn_jira:jira_label1]
# Url to Jira server
url=https://<jira url>
# Authentication method (AUTH, BASIC, TOKEN, OAUTH)
auth_method=BASIC
user=<jira username or email>
password=<jira user password or API Key>
# For TOKEN authentication
#auth_token=
# For OAUTH connections, the four parameters below are required and user/password are ignored
#access_token = <oauth access token>
#access_token_secret = <oauth access token secret>
#consumer_key_name = <oauth consumer key - from Jira incoming link settings>
#private_rsa_key_file_path = <private RSA key matched with public key on Jira>
# Maximum time in seconds to wait before timeout
#timeout=30
# Data table name to hold data for tasks synced to Jira
jira_dt_name=jira_task_references
# Path to certificate. False to disable certificate verification.
verify_cert=True
# Search filters for Jira issue to sync with SOAR cases.
poller_filters= priority in (high, medium, low) and status in ('to do', 'in progress', done) and project in (project_name1, project_name2)
# Max number of issues that can be returned from Jira issue search
max_issues_returned = 50
# Proxies to use
#https_proxy=
# OPTIONAL: override value for templates used for creating/updating/closing SOAR cases.
# See documentation section "Templates for SOAR Cases" for more details
#soar_create_case_template=
#soar_update_case_template=
#soar_close_case_template=

[fn_jira:jira_label2]
# Url to Jira server
url=https://<jira url>
# Authentication method (AUTH, BASIC, TOKEN, OAUTH)
auth_method=BASIC
user=<jira username or email>
password=<jira user password or API Key>
# For TOKEN authentication
#auth_token=
# For OAUTH connections, the four parameters below are required and user/password are ignored
#access_token = <oauth access token>
#access_token_secret = <oauth access token secret>
#consumer_key_name = <oauth consumer key - from Jira incoming link settings>
#private_rsa_key_file_path = <private RSA key matched with public key on Jira>
# Maximum time in seconds to wait before timeout
#timeout=30
# Data table name to hold data for tasks synced to Jira
jira_dt_name=jira_task_references
# Path to certificate. False to disable certificate verification.
verify_cert=True
# Search filters for Jira issue to sync with SOAR cases.
poller_filters= priority in (high, medium, low) and status in ('to do', 'in progress', done) and project in (project_name1, project_name2)
# Max number of issues that can be returned from Jira issue search
max_issues_returned = 50
# Proxies to use
#https_proxy=
# OPTIONAL: override value for templates used for creating/updating/closing SOAR cases.
# See documentation section "Templates for SOAR Cases" for more details
#soar_create_case_template=
#soar_update_case_template=
#soar_close_case_template=
"""
