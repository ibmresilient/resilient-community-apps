# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
	test with: resilient-circuits selftest -l fn_outbound_email
"""

import smtplib
import logging
from resilient_lib.components.resilient_common import validate_fields
from fn_outbound_email.lib.smtp_mailer import SendSMTPEmail

LOG = logging.getLogger(__name__)
LOG.addHandler(logging.StreamHandler())

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 20
SMTP_DEFAULT_PORT = 25

def selftest_function(opts):
    """test if host exists, if using TLS sends an empty email"""

    try:
        smtp_config_section = opts.get(CONFIG_DATA_SECTION, {})
        smtp_server = smtp_config_section.get("smtp_server")
        smtp_port = str(smtp_config_section.get("smtp_port", SMTP_DEFAULT_PORT))
        smtp_cafile = smtp_config_section.get("smtp_ssl_cafile", False)
        smtp_user = smtp_config_section.get("smtp_user")
        smtp_password = smtp_config_section.get("smtp_password")

        smtp_conn_timeout = int(smtp_config_section.get("smtp_conn_timeout", SMTP_DEFAULT_CONN_TIMEOUT))

        validate_fields(["smtp_server", "smtp_port"], smtp_config_section)
        LOG.info("Validating connection to mail server")

        if smtp_config_section.get("smtp_ssl_mode") == "ssl":
            LOG.info("Building SSL connection object")
            smtp_connection = smtplib.SMTP_SSL(host=smtp_server,
                                                        port=smtp_port,
                                                        certfile=smtp_cafile,
                                                        context=SendSMTPEmail.get_smtp_ssl_context,
                                                        timeout=smtp_conn_timeout)
        else:
            LOG.info("Building generic connection object")
            smtp_connection = smtplib.SMTP(host=smtp_server,
                                                    port=smtp_port,
                                                    timeout=smtp_conn_timeout)
            if smtp_config_section.get("smtp_ssl_mode") == "starttls" and smtp_user is not None:
                LOG.info("Starting TLS...")
                smtp_connection.ehlo()
                smtp_connection.starttls()
                smtp_connection.ehlo()
                LOG.info("Logging in to SMTP...")
                if not smtp_password:
                    raise Exception('An SMTP user has been set; the SMTP password from app.config cannot be null')
                else:
                    smtp_connection.login(user=smtp_user, password=smtp_password)
                    smtp_connection.sendmail(smtp_user, smtp_user, 'this is a test email')

        return {"state": "success"}
    except Exception as err:
        LOG.error(err)
        return {"state": "failure"}
    finally:
        if smtp_connection:
            smtp_connection.quit()
