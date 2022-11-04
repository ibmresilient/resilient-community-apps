# -*- coding: utf-8 -*-
"""Generate a default configuration-file section for fn_jira"""
from __future__ import print_function

def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    return u"""
# V2.2.0+ have the option to have multiple servers configured.
# By default two examples of servers are given, example one is labeled `jira_label1` and example two is labeled `jira_label2`.
# The label for a server is placed after `[fn_jira:` and then followed by `]`.
# To add additional servers copy the below example server configuration from `[fn_jira:jira_label1]` to `#https_proxy=`.
# Then paste it at the bottom of the app.config.
# Change the server label, `jira_label1`, to a label helpful to define that server.
# Then change the setting to those of the server you wish to add.

[fn_jira:jira_label1]
url=https://<jira url>
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
timeout=10
# data Table name to hold data for tasks synced to Jira
jira_dt_name=jira_task_references 
# use verify_cert to disable untrusted certificate verification
verify_cert=True
#http_proxy=
#https_proxy=

[fn_jira:jira_label2]
url=https://<jira url>
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
timeout=10
# data Table name to hold data for tasks synced to Jira
jira_dt_name=jira_task_references 
# use verify_cert to disable untrusted certificate verification
verify_cert=True
#http_proxy=
#https_proxy=
"""
