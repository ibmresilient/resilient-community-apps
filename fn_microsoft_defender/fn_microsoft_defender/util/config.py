# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_microsoft_defender"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_microsoft_defender when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_microsoft_defender]
# specify the settings for your Azure and Defender access
tenant_id=xxx
client_id=xxx
app_secret=xxx
# use alternative geo specific urls for better performance
#   api-us.securitycenter.microsoft.com
#   api-eu.securitycenter.microsoft.com
#   api-uk.securitycenter.microsoft.com
api_url=https://api.securitycenter.microsoft.com
# poller settings
#   poller timeback time first time, in minutes
polling_lookback=120
#   poller internal in seconds. Comment out to disable poller
polling_interval=60
# comma separated list of fields to filter incidents to create
#  if more than one field is specified, all fields need to pass
#   format: "field1": value: "field2": ["list_value1", "list_value2"]
new_incident_filters="status": ["New", "Active"],"severity": ["High", "Medium","Low"]
# custom templates to replace the default map of defender incident fields to SOAR incident fields
#create_incident_template=
#update_incident_template=
#close_incident_template=
#update_defender_alert_template=
#update_defender_incident_template=
# uncomment as necessary for proxies
#http_proxy=http://yourproxy.com
#https_proxy=https://yourproxy.com
"""
    return config_data
