# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
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

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 20
SMTP_DEFAULT_PORT = 25

def selftest_function(opts):
    """test if host exists, if using TLS sends an empty email"""

    try:
        smtp_config_section = opts.get(CONFIG_DATA_SECTION, {})
        smtp_user = smtp_config_section.get("smtp_user")
        from_email_address = smtp_config_section.get("from_email_address", smtp_user)

        mail_data = {}
        mail_data['mail_from'] = from_email_address
        mail_data['mail_to'] = [from_email_address]
        mail_data['mail_subject'] = 'This is a test email'
        mail_data['mail_cc'] = None
        mail_data['mail_bcc'] = None
        mail_data['mail_attachments'] = None

        send_smtp_email = SendSMTPEmail(opts, mail_data)
        mail_body_text = "This is a test body"
        error_msg = send_smtp_email.send(body_text=mail_body_text)

        if error_msg:
            return {
                "state": "failure",
                "reason": "Failed to send test email with error:{}".format(error_msg)
            }
        else:
            return {
                "state": "success",
                "reason": "Send test email Successful"
            }

    except Exception as err:
        return {
            "state": "failure",
            "status_code": err
        }
