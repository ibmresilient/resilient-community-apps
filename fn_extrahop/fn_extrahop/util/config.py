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
# The ExtraHop REST API url.
extrahop_rx_host_url = <EXTRAHOP_RX_HOST_URL>
extrahop_rx_api_version = v1
# The ExtraHop functions can be executed against the ExtraHop cloud-based service
# or against an ExtraHop standalone sensor.
# Cloud service console & authentication settings - for cloud-based ExtraHop instance
# The Cloud service console url is used to create linkbacks when executing against the
# ExtraHop cloud-based service.
extrahop_rx_cloud_console = <EXTRAHOP_RX_CLOUD_CONSOLE>
extrahop_rx_key_id = <EXTRAHOP_RX_API_KEY_ID>
extrahop_rx_key_secret = <EXTRAHOP_RX_API_KEY_SECRET>
# Standalone sensor authentication setting - for a standalone ExtraHop sensor
extrahop_rx_api_key = <EXTRAHOP_RX_API_KEY>
# If your ExtraHop server uses a self-signed TLS certificate, or some
# other certificate that is not automatically trusted by your machine,
# you can set the CA bundle using the extrahop_cafile setting.
# If you don't want to use a cert you can set extrahop_cafile=false.
# Note: This setting is mandatory for a standalone ExtraHop sensor.
extrahop_cafile=<path to cert file>|false
# Interval to poll ExtraHop for detections (in seconds).
# To turn the poller off use value 0.
# Set value to 0 when running selftest/Test Configuration.
polling_interval = <POLLING_INTERVAL>
# Optional - Filter detection results returned to SOAR using key/value pairs. Filter keys/values are all optional.
# Example: polling_filters="risk_score_min": 80, "category": ["sec.exploit"], "types": ["interactive_traffic_ssh", 
# "interactive_traffic_shell"], "status": [".none", "new", "in_progress", "acknowledged", "closed"], 
# "resolution": [".none", "action_taken", "no_action_taken"]
# The security categories include the following: sec, sec.action, sec.botnet, sec.caution, sec.command, sec.cryptomining,
# sec.dos, sec.exploit, sec.exfil, sec.lateral, sec.ransomware, sec.recon
# The detection types includes some of the following: cve_2019_0708, interactive_traffic_ssh, interactive_traffic_shell
# rdp_brute_force, ssh_brute_force.
# To get a full list of types  c.f. ExtraHop console/'Systems Settings'/'Detections'/'Detection Catalog'.
# Risk score ranges: red (80-99), orange (31-79), or yellow (1-30).
polling_filters =
#http_proxy=http://proxy:80
#https_proxy=https://proxy:443
"""
    return config_data
