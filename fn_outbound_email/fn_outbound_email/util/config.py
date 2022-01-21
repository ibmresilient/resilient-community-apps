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
#Blank for initial selftest, required for TLS
smtp_user=

## OAuth2 authentication settings
scope=
client_id=
client_secret=
# Note that the token_url below, for some applications e.g. using Microsoft, contains a placeholder 
# {tenant} for the tenant ID.
# Do not place the tenant id in the place holder as the integration will do this at run time.
# e.g. token_url=https://login.microsoftonline.com/{tenant_id}/oauth2/V2.0/token and 
# tenant_id=1234567a-abc8-90d1-2efa3-123456789abcd
# Do not place '/' at the end of the url strings.
#
token_url=
# Optional setting: A seperate value for the tenant_id parameter see {tenant_id} placeholder above.
tenant_id=
# Optional setting: Certain applications may require a refresh_token.
refresh_token=

##Basic Authentication setting
#Blank for initial selftest, required for TLS in Basic Authentication mode.
smtp_password=

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
