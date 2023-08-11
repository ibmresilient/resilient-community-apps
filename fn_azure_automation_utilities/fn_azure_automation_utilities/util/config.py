# -*- coding: utf-8 -*-
# Generated with resilient-sdk v49.0.4423

"""Generate a default configuration-file section for fn_azure_automation_utilities"""


def config_section_data():
    """
    Produce add the default configuration section to app.config,
    for fn_azure_automation_utilities when called by `resilient-circuits config [-c|-u]`
    """

    return u"""[fn_azure_automation_utilities]
# Azure AD Application client ID
client_id=
# Azure AD Application client secret
client_secret=
# Azure AD Application tenant ID
tenant_id=
# The token_url setting is used to get a new access token.
token_url=https://login.microsoftonline.com/(tenant_id)/oauth2/v2.0/token
# The auth_url setting is used to get a new refresh token.
auth_url=https://login.microsoftonline.com/(tenant_id)/oauth2/v2.0/authorize
# Scopes are a way to limit the amount of access that is granted to an access token.
scope=https://management.azure.com/user_impersonation openid profile offline_access
# Applications require a refresh_token to allow access tokens to be renewed. This can be generated using
# the generate_oauth2_refresh_token utility from the oauth-utils package.
refresh_token=
# Azure subscription ID
subscription_id=
#https_proxy=https://proxy:443
"""
