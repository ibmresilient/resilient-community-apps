# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_jira"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_jira]
url=https://<jira url>
auth_method=BASIC
user=<jira username or email>
password=<jira user password or API Key>
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
    return config_data