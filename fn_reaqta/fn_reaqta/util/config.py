# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_reaqta"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_reaqta when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_reaqta]
polling_interval=60
polling_lookback=120
# comma separated list of hives to poll: poller_hives = hive_label1, hive_label2
polling_hives=
# comma separated list of hives to set a policy if not specified from the SOAR app
policy_hives=
# Optional override value for templates used for creating/updating/closing SOAR cases
#soar_create_case_template=
#soar_close_case_template=
# For an integration server, specify the proxy settings here.
# For AppHost, use the manageAppHost proxy capability.
#http_proxy=
#https_proxy=
# specify a timeout value for access to ReaQta. Default is 60 seconds
timeout=60

[fn_reaqta:your_hive_label1]
# repeat this section for as many hives as you need to specify
api_key=xxx
api_secret=xxx
reaqta_url=https://xxx/
api_version=rqt-api/1/
cafile=/path/to/cafile.crt or false
#
# set filters for the poller. Ex: "alertStatus": "malicious", "severity": ["medium", "high"], "tag": ["hive"]
#   additional filtering can be done by groups and impact (greater or equal to numeric value):
#      poller_filters="groups": ["groupA", "groupB"], "impact": 70
#polling_filters="alertStatus": "benign", "severity": ["low", "high"], "tag": ["hive"]
"""
    return config_data
