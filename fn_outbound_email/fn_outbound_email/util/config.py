# -*- coding: utf-8 -*-

"""Generate a default configuration-file section for fn_outbound_email"""

from __future__ import print_function


def config_section_data():
    """Produce the default configuration section for app.config,
       when called by `resilient-circuits config [-c|-u]`
    """
    config_data = u"""[fn_outbound_email]
# SMTP SERVER (IP ADDRESS or FQDN)
smtp_server=xxx.xxx.xxx.xxx

smtp_user=xxx
smtp_password=xxx

# SMTP PORT NUMBER, 25 or 587
smtp_port=25

# SMTP CONNECTION TIMEOUT IN SECONDS
smtp_conn_timeout=20

# SMTP SSL MODE = (starttls, ssl, None)
smtp_ssl_mode=None

# SSL Cert
# If your email server uses a self-signed SSL/TLS certificate, or some
# other certificate that is not automatically trusted by your machine,
# specify the file below, e.g. 'path/to/certificate.pem' OR
# set to true if using system cert store OR
# set to false if disabling SSL verification
#smtp_ssl_cafile=~/path/to/email_cert.cer
    """
    return config_data
    
