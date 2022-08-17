# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_outbound_email"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """ 
    return u"""[fn_outbound_email]
# SMTP SERVER (IP ADDRESS or FQDN)
smtp_server=xxx.xxx.xxx.xxx
## Basic Authentication settings
#smtp user required for TLS and OAuth2
smtp_user=
smtp_password=
## End of Basic Authentication settings

## Start of OAuth 2.0 authentication settings ##
# Leave OAuth 2.0 settings blank or commented out if using Basic Authentication.
client_id=
client_secret=
# Scopes are a way to limit the amount of access that is granted to an access token.
# For common email services from Google and Microsoft Outlook 365 use the following values: 
# Gmail: scope=https://mail.google.com/
# Outlook 365: scope=offline_access https://outlook.office365.com/SMTP.Send
scope=
# The token_url setting is used to get a new access token.
# Common email services from Google amd Microsoft Outlook 365 use the following token_url values: 
# Gmail: token_url=https://accounts.google.com/o/oauth2/token
# Outlook 365: token_url=https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/token
# Note: Microsoft uses a tenant ID in the url.
# e.g. token_url=https://login.microsoftonline.com/1234567a-abc8-90d1-2efa3-123456789abcd/oauth2/v2.0/token
# Do not place '/' at the end of the url strings.
token_url=
# The auth_url setting is used to get a new refresh token.
# An optional setting which can be used by the generate_oauth2_refresh_token utility to generate a refresh token.
# Common email services from Google amd Microsoft Outlook 365 use the following values: 
# Gmail: auth_url=https://accounts.google.com/o/oauth2/auth
# Outlook 365: auth_url=https://login.microsoftonline.com/<tenant_id>/oauth2/v2.0/authorize
# Note: Microsoft uses a tenant ID in the url.
# e.g. auth_url=https://login.microsoftonline.com/1234567a-abc8-90d1-2efa3-123456789abcd/oauth2/v2.0/authorize
auth_url=
# Applications require a refresh_token to allow access tokens to be renewed. This can be generated using
# the generate_oauth2_refresh_token utility from the oauth-utils package.
refresh_token=
## End of OAuth 2.0 authentication settings ##

#If smtp_user is not an email address then from_email_address should equal the email address
#  Also used with selftest
from_email_address=

# SMTP PORT NUMBER, 25 or 587/2525
smtp_port=587

# SMTP CONNECTION TIMEOUT IN SECONDS
smtp_conn_timeout=20

# SMTP SSL MODE = (starttls, ssl, None)
smtp_ssl_mode=starttls

# SSL Cert (not supported)
#smtp_ssl_cafile=
# Optional - Path to a custom template file for formatting HTML email.
# The integration will use this template out of the box. If removed, it will default to the pre-processing script.
# template_file=data/templates/example_send_email.jinja
template_file=data/templates/example_send_email.jinja
# enhance the 'email' tab with email conversation fields and datatable
#enable_email_conversations=true/false
    """
