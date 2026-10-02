# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_microsoft_defender"""

def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_microsoft_defender when called by `resilient-circuits config [-c|-u]`
    """

    return """[fn_microsoft_defender]
# Specify the settings for your Azure and Defender access
tenant_id=xxx
client_id=xxx
app_secret=xxx
# Use alternative geo specific urls for better performance
#   api-us.securitycenter.microsoft.com
#   api-eu.securitycenter.microsoft.com
#   api-uk.securitycenter.microsoft.com
api_url=https://api.securitycenter.microsoft.com
# poller settings
#   poller lookback time first time, in minutes
polling_lookback=120
#   poller internal in seconds. Comment out to disable poller
polling_interval=60
# Comma separated list of fields to filter incidents to create
#  if more than one field is specified, all fields need to pass
#   format: "field1": value: "field2": ["list_value1", "list_value2"]
new_incident_filters="status": ["New", "Active"],"severity": ["High", "Medium","Low"]
# new to v1.1, comma separated list of alert fields to filter. At least one alert needs to meet the filter values
#alert_filters="serviceSource": ["MicrosoftDefenderForEndpoint"]
# Custom templates to replace the default map of defender incident fields to SOAR incident fields
#create_incident_template=
#update_incident_template=
#close_incident_template=
#update_defender_alert_template=
#update_defender_incident_template=
# Uncomment to specify how to handle client_certificate verification
#verify= false | /path/to/client_certificate.pem
# Uncomment as necessary for proxies
#http_proxy=http://yourproxy.com
#https_proxy=https://yourproxy.com
"""
