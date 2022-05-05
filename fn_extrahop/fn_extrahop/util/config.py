# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2021. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_extrahop"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_extrahop when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_extrahop]
# The ExtraHop rest api url.
extrahop_rx_host_url = <EXTRAHOP_RX_HOST_URL>
# Cloud service console url used to create linkbacks when executing against the
# ExtraHop cloud-based service. Not required if connecting to a standalone sensor.
extrahop_rx_cloud_console = <EXTRAHOP_RX_CLOUD_CONSOLE>
extrahop_rx_api_version = v1
# The ExtraHop functions can be executed against the ExtraHop cloud-based service
# or against an ExtraHop standalone sensor.
# Authentication settings for ExtraHop Cloud service are an api key id and key secret.
extrahop_rx_key_id = <EXTRAHOP_RX_API_KEY_ID>
extrahop_rx_key_secret = <EXTRAHOP_RX_API_KEY_SECRET>
# Authentication setting for ExtraHop standalone sensor is a single api key
extrahop_rx_api_key = <EXTRAHOP_RX_API_KEY>
# Interval to poll ExtraHop for detections (in seconds).
# To turn the poller off use value 0.
# Set value to 0 when running selftest/Test Configuration.
polling_interval = <POLLING_INTERVAL>
# Optional - Filter detection results returned to SOAR using key/value pairs. Filter keys/values are all optional.
# Example: polling_filters="risk_score_min": 80, "category": ["sec.exploit"], "status": [".none", "new", "in_progress", "acknowledged", "closed"], 
#                          "resolution": [".none", "action_taken", "no_action_taken"], 
# The security categories include the following: sec, sec.action, sec.botnet, sec.caution, sec.command, sec.cryptomining,
# sec.dos, sec.exploit, sec.exfil, sec.lateral, sec.ransomware, sec.recon
# Risk score ranges: red (80-99), orange (31-79), or yellow (1-30).
polling_filters =
# If your ExtraHop server uses a self-signed TLS certificate, or some
# other certificate that is not automatically trusted by your machine,
# you can set the CA bundle using the extrahop_cafile setting.
# If you don't want to use a cert you can set extrahop_cafile=false.
#
#extrahop_cafile=<path to cert file>|false
#http_proxy=http://proxy:80
#https_proxy=https://proxy:443
"""
    return config_data
