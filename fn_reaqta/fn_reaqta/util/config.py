# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_reaqta"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_reaqta when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_reaqta]
api_key=xxx
api_secret=xxx
reaqta_url=https://xxx/
api_version=rqt_api/1/
#
polling_interval=60
polling_lookback=120
# set filters for the poller. Ex: "alertStatus": "malicious", "severity": ["medium", "high"], "tag": ["hive"]
#   additional filtering can be done by groups and impact (greater or equal to numeric value):
#      poller_filters="groups": ["groupA", "groupB"], "impact": 70
#polling_filters="alertStatus": "benign", "severity": ["low", "high"], "tag": ["hive"]
cafile=/path/to/cafile.crt or false
# Optional override value for templates used for creating/updating/closing SOAR cases
#soar_create_case_template=
#soar_close_case_template=
# For an integration server, specify the proxy settings here.
# For AppHost, use the manageAppHost proxy capability.
#http_proxy=
#https_proxy=
# specify a timeout value for access to ReaQta. Default is 60 seconds
timeout=60
"""
    return config_data
