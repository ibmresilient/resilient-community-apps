# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
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
#Smtp User required for TLS and OAuth2
smtp_user=

## OAuth2 authentication settings
# Leave OAuth2 settings blank or commented out if using Basic Authentication.
# For common email services from Google amd Microsoft Outlook 365 use the following values: 
# Gmail: scope=https://mail.google.com/
# Outlook365: scope=offline_access https://outlook.office365.com/SMTP.Send
scope=
client_id=
client_secret=
# For common email services from Google amd Microsoft Outlook 365 use the following values: 
# Gmail: token_url=https://accounts.google.com/o/oauth2/token
# Outlook365: token_url=https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token
# Note that the token_url, for some applications e.g. using Microsoft, contains a placeholder 
# {tenant_id} for the tenant ID.
# Do not place the tenant id in the place holder as the integration will do this at run time.
# e.g. tenant_id=1234567a-abc8-90d1-2efa3-123456789abcd
# Do not place '/' at the end of the url strings.
#
token_url=
# The auth_url is used in the oauth2_token utility.
# For common email services from Google amd Microsoft Outlook 365 use the following values: 
# Gmail: https://accounts.google.com/o/oauth2/auth
# Outlook365: https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/authorize
auth_url=
# Optional setting: A separate value for the tenant_id parameter see {tenant_id} placeholder above.
tenant_id=
# Applications require a refresh_token to allow access tokens to be renewed.
refresh_token=
## End of OAuth2 authentication settings

## Basic Authentication settings
smtp_password=
## End of Basic Authentication settings

#If smtp_user is not an email address then from_email_address should equal the email address
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
# template_file=data/example_send_email.jinja
template_file=data/example_send_email.jinja
    """
