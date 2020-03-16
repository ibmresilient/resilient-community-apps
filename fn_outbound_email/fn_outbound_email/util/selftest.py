# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Function implementation
   test with: resilient-circuits selftest -l fn_outbound_email
"""
import errno
import os
import logging
import requests
import smtplib
import ssl
from ssl import Purpose
from fn_outbound_email.lib.smtp_mailer import SendSMTPEmail
from resilient_lib.components.resilient_common import validate_fields

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 10
SMTP_DEFAULT_PORT = 25
      
def selftest_function(opts):

   try:
      smtp_config_section = opts.get(CONFIG_DATA_SECTION, {})
      smtp_server = smtp_config_section.get("smtp_server")
      smtp_port = str(smtp_config_section.get("smtp_port", SMTP_DEFAULT_PORT))
      smtp_cafile = smtp_config_section.get("smtp_ssl_cafile", False)
      smtp_user = smtp_config_section.get("smtp_user")
      smtp_password = smtp_config_section.get("smtp_password")

      smtp_conn_timeout = int(smtp_config_section.get("smtp_conn_timeout", SMTP_DEFAULT_CONN_TIMEOUT))

      validate_fields(["smtp_server", "smtp_port", "smtp_ssl_cafile", "smtp_user", "smtp_password"], smtp_config_section)
      log.info("Validating connection to mail server")

      if smtp_config_section.get("smtp_ssl_mode") == "ssl":
            log.info("Building SSL connection object")
            smtp_connection = smtplib.SMTP_SSL(host=smtp_server,
                                             port=smtp_port,
                                             certfile=smtp_cafile,
                                             context=SendSMTPEmail.get_smtp_ssl_context,
                                             timeout=smtp_conn_timeout)
      else:
            log.info("Building generic connection object")
            smtp_connection = smtplib.SMTP(host=smtp_server,
                                          port=smtp_port,
                                          timeout=smtp_conn_timeout)

            if smtp_config_section.get("smtp_ssl_mode") == "starttls":
               log.info("Starting TLS...")
               smtp_connection.starttls(context=SendSMTPEmail.get_smtp_ssl_context)

      if smtp_user:
            log.info("Logging in to SMTP...")
            if not smtp_password:
               raise Exception('An SMTP user has been set; the SMTP password from app.config cannot be null')
            else:
               smtp_connection.login(user=smtp_user, password=smtp_password)
      return {"state": "success"}
   except Exception as err:
      log.error(err)
      return {"state": "failure"}

