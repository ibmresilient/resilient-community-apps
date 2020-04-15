# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

"""Generate a default configuration-file section for fn_outbound_email"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """ 
    config_data = u"""[fn_outbound_email]
# SMTP SERVER (IP ADDRESS or FQDN)
smtp_server=xxx.xxx.xxx.xxx

#Blank for initial selftest, both required for TLS 
smtp_user=
smtp_password=

# SMTP PORT NUMBER, 25 or 587
smtp_port=25

# SMTP CONNECTION TIMEOUT IN SECONDS
smtp_conn_timeout=20

# SMTP SSL MODE = (starttls, None)
smtp_ssl_mode=None

# SSL Cert (not supported)
#smtp_ssl_cafile=None

# Optional - Path to a custom template file for the escalated incident.   If not defined, the integration will use
# the default that comes with the integration in the html preprocessing script.
# template_file=/usr/integration/html_template.jinja
    """
    return config_data
    
