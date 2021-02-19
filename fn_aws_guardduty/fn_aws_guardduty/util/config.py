# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Generate a default configuration-file section for fn_aws_guardduty"""

# Shared/global variables used in poller/functions.
STOP_THREAD = False
REQUIRED_CONFIG_SETTINGS = ["aws_gd_access_key_id", "aws_gd_secret_access_key", "aws_gd_master_region",
                            "aws_gd_regions"]

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_aws_guardduty when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_aws_guardduty]
aws_gd_access_key_id = <AWS_GUARDDUTY_ACCESS_KEY_ID>
aws_gd_secret_access_key = <AWS_GUARDDUTY_SECRET_ACCESS_KEY>
# Default or master region for the integration e.g us-west-1.
aws_gd_master_region = <AWS_GUARDDUTY_DEFAULT_REGION>
# Filter by GuardDuty region names. Can be a string or regular expression.
# e.g. aws_gd_regions = "^(us|eu).*" for Europe and US regions or ".*" for all regions. 
# Note: Only regions which have GuardDuty enabled will be processed.
aws_gd_regions = <AWS_GUARDDUTY_REGION_REGEX>
# Interval to refresh regions information (in minutes).
aws_gd_regions_interval = <REGIONS_INTERVAL>
# Interval to poll Guardduty for findings (in minutes).
# To turn the poller off use value 0
aws_gd_polling_interval = <POLLING_INTERVAL>
# Optional - severity threshold (integer) criteria to filter findings results.
# Severity ranges: 7.0 - 8.9 -> High, 4.0 - 6.9 -> Medium, 1.0 = 3.9 -> Low
#aws_gd_severity_threshold = <SEVERITY_THRESHOLD>
# Optional - How long, to check for previous findings at startup (in minutes).
# Used in criteria for filtering findings retrieval.
#aws_gd_lookback_interval = <LOOKBACK_INTERVAL>
# Optional - User defined JSON template file for closing Resilient incidents.
#aws_gd_close_incident_template = <PATH_TO_TEMPLATE_FILE>
# Optional settings for access to GuardDuty via a proxy.
#http_proxy=http://proxy:80
#https_proxy=http://proxy:443
"""
    return config_data