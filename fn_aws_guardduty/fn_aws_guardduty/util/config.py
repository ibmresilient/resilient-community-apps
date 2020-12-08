# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate a default configuration-file section for fn_aws_guardduty"""

# Shared/global variables used in poller/functions.
STOP_THREAD = False
REQUIRED_CONFIG_SETTINGS = ["aws_gd_access_key_id", "aws_gd_secret_access_key", "aws_gd_regions"]

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_aws_guardduty when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_aws_guardduty]
aws_gd_access_key_id=<AWS_GUARDDUTY_ACCESS_KEY_ID>
aws_gd_secret_access_key=<AWS_GUARDDUTY_SECRET_ACCESS_KEY>
# Filter by GuardDuty region names. Can be a string or regular expression.
# e.g. aws_gd_regions=^(us|eu).* to get Europe and US regions.
aws_gd_regions=<AWS_GUARDDUTY_REGION_REGEX>
# Interval to refresh regions information (in minutes).
aws_gd_regions_interval=60
# Interval to poll Guardduty (in minutes).
aws_gd_polling_interval=10
# Optional - severity threshold (int) to use in criterion to filter findings 
# results. (default 7).
# Severity ranges: 7.0 - 8.9 -> High, 4.0 - 6.9 -> Medium, 1.0 = 3.9 -> Low
aws_gd_severity_threshold = 7
# Optional - Lookback interval in minutes to check if findings updated
# since last run. Used in criteria for filtering findings retrieval (default 60).
aws_gd_lookback_interval=60
# Optional settings for access to GuardDuty via a proxy.
#http_proxy=http://proxy:80
#https_proxy=http://proxy:80
"""
    return config_data