# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_darktrace"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_darktrace when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_darktrace]
# enter the base URL to your Darktrace instance and
# the public and private keys you generated for this app
instance_url=https://<instance>.cloud.darktrace.com
api_key=
api_secret=

# Number of seconds between poller cycles. A value of 0 disables the poller
polling_interval=60
# Number of minutes to lookback for queries the first time the poller runs.
polling_lookback=120

# 'min_score' is used to determine the minimum score threshold to use
# when fetching incident groups to poll automatically into SOAR.
# value should be in [0-100]
min_score=0.0

# 'locale' specifies the language locale to return any summary or descriptions
# options: de_DE, en_GB, en_US, es_ES, es_419, fr_FR, it_IT, ja_JP, ko_KR, pt_BR, zh_Hans, zh_Hant
# see Darktrace customer portal for up todate list of locale options
locale=en_US

# OPTIONAL: turn off comment synchronization
# This will stop polling Darktrace for new comments on open incidents.
# By default this is turned on (i.e. True) but should be turned off if
# Darktrace comments are not needed in SOAR. Comments from SOAR can still
# be sent individually to Darktrace.
auto_sync_darktrace_comments = True

# OPTIONAL: comma-separated list of device IDs to be ignored when polling for new
# AI Analyst incidents. This is useful when a certain device repeatedly causes
# issues in the system.
# EX: exclude_did=4,120,99
exclude_did=

# OPTIONAL: specify whether to only include events with SaaS related activity.
saas_only=False

# OPTIONAL: use the 'verify' config to set a value for SSL verification
# if 'False', no SSL will be used. if 'True' or unset, the default SSL root cert
# will be used. if 'verify' is a path, the value of the path will override the
# root cert bundle and the file found at the path will be used for server-side SSL
# verify=

# OPTIONAL: Specify paths to files if client-side certs are needed to authenticate
# client_auth_cert = <path_to_cert.pem>
# client_auth_key = <path_to_cert_private_key.pem>
"""
    return config_data
