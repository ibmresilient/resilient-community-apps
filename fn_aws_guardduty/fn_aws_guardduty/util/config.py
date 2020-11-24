# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate a default configuration-file section for fn_aws_guardduty"""

# Shared/global variables used in poller/functions.
STOP_THREAD = False
REQUIRED_CONFIG_SETTINGS = ["aws_gd_access_key_id", "aws_gd_secret_access_key", "aws_gd_region"]

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_aws_guardduty when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_aws_guardduty]
aws_gd_access_key_id=<AWS_GUARDDUTY_ACCESS_KEY_ID>
aws_gd_secret_access_key=<AWS_GUARDDUTY_SECRET_ACCESS_KEY>
aws_gd_region=<AWS_GUARDDUTY_DEFAULT_REGION>
# Interval to poll Guardduty in minutes
aws_gd_polling_interval=10
# Initial Import Look-back Interval in minutes (default: 1 hour)
aws_gd_startup_interval=60
# Optional settings for access to GuardDuty via a proxy.
#http_proxy=http://proxy:80
#https_proxy=http://proxy:80
"""
    return config_data