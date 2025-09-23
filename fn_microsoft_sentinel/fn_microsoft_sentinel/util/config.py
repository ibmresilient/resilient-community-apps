# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Generate a default configuration-file section for fn_microsoft_sentinel"""

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_microsoft_sentinel when called by `resilient-circuits config [-c|-u]`
    """

    return """[fn_microsoft_sentinel]
azure_url = https://management.azure.com
# comma separated list of labels to poll for incidents: [label1, label2]
ms_sentinel_labels = label1
# Poller settings
# Time in minutes for the poller to look back
polling_lookback = 120
# poller interval in seconds, comment out or set to 0 to disable poller
polling_interval = 60
# API version to use when making API call to Microsoft Sentinel (optional)
# If api_version is configured under fn_microsoft_sentinel than api_version
#  that are configured under the individual labels will be ignored.
# Sentinel API versions can be found https://learn.microsoft.com/en-us/rest/api/securityinsights/api-versions
api_version = 2023-11-01-preview
# Clear the Alerts and Entities datatable before new data is added. True or False
clear_datatable = false
# If verify is configured under fn_microsoft_sentinel, then verify
#  that are configured under the individual labels will be ignored.
# verify = false | /path/to/client_certificate.pem
verify = true
# If https_proxy is configured under fn_microsoft_sentinel, then https_proxy
#  that are configured under the individual labels will be ignored.
# add proxy settings as needed
#https_proxy =

[fn_microsoft_sentinel:label1]
# copy this label template for each different incident environment
# the name of the label, (ex: label1) is anything of your choosing
# enter your own tenant_id, client_id (app_id) and app_secret
tenant_id = aaa-bbb-ccc
client_id = aaa-bbb-ddd
app_secret = aaa-bbb-eee
# enter your subscription_id, workspace name and resource_groupname
subscription_id = aaa-bbb-fff
workspace_name = AzureExampleWorkspace
resource_groupname = ExampleGroupName
# API version to use when making API call to Microsoft Sentinel (optional)
# Sentinel API versions can be found https://learn.microsoft.com/en-us/rest/api/securityinsights/api-versions
api_version = 2023-11-01-preview
# limit the number of alerts per sentinel incident returned, in ascending order. If not assigned, will get all alerts
max_alerts =
# Can specify either new_incident_filters or poller_filters_template. The example poller_filters_template is used by
#  default if neither of these settings are specified.
# comma separated list of fields to filter incidents to create
#  if more than one field is specified, all fields need to pass
#  format: "field1": "value", "field2": ["list_value1", "list_value2"]
new_incident_filters = "status": ["New", "Active"], "severity": ["High", "Medium","Low"]
# custom template to replace the default example poller filters template.
#poller_filters_template =
# Either True or False if the SOAR case should be closed when its linked Sentinel incident is closed.
# If set to False, the linked SOAR case will be updated, but not closed.
close_soar_case=true
# verify = false | /path/to/client_certificate.pem
verify = true
# add proxy settings as needed
#https_proxy =
# custom templates to replace the default map of sentinel fields to SOAR incident fields
#create_incident_template=
#update_incident_template=
#close_incident_template=
#sentinel_update_incident_template=
#sentinel_close_incident_template=
"""
