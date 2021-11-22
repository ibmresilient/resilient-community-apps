# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_microsoft_sentinel"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_microsoft_sentinel when called by `resilient-circuits config [-c|-u]`
    """

    config_data = u"""[fn_microsoft_sentinel]
azure_url=https://management.azure.com
# enter your own tenant_id, client_id (app_id) and app_secret
tenant_id=aaa-bbb-ccc
client_id=aaa-bbb-ddd
app_secret=aaa-bbb-eee
# poller timeback time first time, in minutes
polling_lookback=120
# Poller settings
# poller interval in seconds, comment out or set to 0 to disable poller
polling_interval=60
# comma separated list of profiles to poll for incidents: profile_a[,profile_b]
sentinel_profiles=profile_a
# add proxy settings as needed
#https_proxy=
#http_proxy=

[fn_microsoft_sentinel:profile_a]
# copy this profile template for each different incident environment
# the name of the profile, (ex: profile_a) is anything of your choosing
#
# enter your subscription_id, workspace name and resource_groupname
subscription_id=aaa-bbb-fff
workspace_name=
resource_groupname=
# limit the number of alerts per sentinel incident returned, in ascending order
max_alerts=
# comma separated list of fields to filter incidents to create
#  if more than one field is specified, all fields need to pass
#   format: "field1": "value", "field2": ["list_value1", "list_value2"]
new_incident_filters="status": ["New", "Active"],"severity": ["High", "Medium","Low"]
# custom templates to replace the default map of sentinel fields to resilient incident fields
#create_incident_template=
#update_incident_template=
#close_incident_template=
#update_sentinel_incident_template=
#close_sentinel_incident_template=
"""
    return config_data
