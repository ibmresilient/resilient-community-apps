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
# uncomment as necessary for proxies
#http_proxy=http://yourproxy.com
#https_proxy=https://yourproxy.com
"""
    return config_data
