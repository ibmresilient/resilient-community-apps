# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

from __future__ import print_function

import logging
import os
import tempfile
from fn_outbound_email.lib.smtp_mailer import SendSMTPEmail
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields

log = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 15
DEFAULT_TLS_SMTP_PORT = '587'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'send_email"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.incident_data = {}
        self.mail_data = {}
        self.opts = opts
        self.smtp_config_section = self.opts.get(CONFIG_DATA_SECTION, {})
        self.template_file_path = self.smtp_config_section.get('template_file')
        self.smtp_port_choice = self.smtp_config_section.get("smtp_port")
        self.smtp_user = self.smtp_config_section.get("smtp_user")

        if self.template_file_path and not os.path.exists(self.template_file_path):
            log.warning(u"Template file '%s' not found.", self.template_file_path)
            self.template_file_path = None

        self.mail_context = {
            "mail_from": "",
            "mail_to": [],
            "mail_cc": [],
            "mail_bcc": [],
            'mail_subject': '',
            "attachment_list": []
        }

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.options = opts.get("fn_outbound_email", {})

    @function("send_email")
    def _send_email_function(self, event, *args, **kwargs):
        """Function: Send Email"""
        try:
            # Get the conditional function parameters:
            if self.smtp_port_choice == DEFAULT_TLS_SMTP_PORT:
                mail_from = self.smtp_user
            else:
                mail_from = kwargs.get("mail_from")  # text
            if self.template_file_path: 
                with open(self.template_file_path, "r") as definition:
                    mail_body_html = definition.read()
                    log.info("Using custom jinja template instead of default, path: %s", self.template_file_path)
            else:
                mail_body_html = kwargs.get("mail_body_html")
            # Get the function parameters:
            mail_to = kwargs.get("mail_to")  # text
            mail_cc = kwargs.get("mail_cc")  # text
            mail_bcc = kwargs.get("mail_bcc")  # text
            mail_subject = kwargs.get("mail_subject")  # text
            mail_body_text = kwargs.get("mail_body_text")  # text
            mail_incident_id = kwargs.get("mail_incident_id")  # number

            if not mail_from: mail_from = "N/A"
            if not mail_cc: mail_cc = "N/A"
            if not mail_bcc: mail_bcc = "N/A"
            if not mail_subject: mail_subject = "N/A"
            
            log.info("mail_from: %s", mail_from)
            log.info("mail_to: %s", mail_to)
            log.info("mail_cc: %s", mail_cc)
            log.info("mail_bcc: %s", mail_bcc)
            log.info("mail_subject: %s", mail_subject)
            log.info("mail_body_html: %s", mail_body_html)
            log.info("mail_body_text: %s", mail_body_text)

            self.mail_data['mail_from'] = mail_from
            self.mail_data['mail_to'] = FunctionComponent.split_string(mail_to)
            self.mail_data['mail_cc'] = FunctionComponent.split_string(mail_cc)
            self.mail_data['mail_bcc'] = FunctionComponent.split_string(mail_bcc)
            self.mail_data['mail_subject'] = mail_subject
            self.mail_data['mail_attachments'] = self.process_attachments(inc_id=mail_incident_id)

            payload = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            validate_fields(["mail_to", "mail_subject", "mail_incident_id"], kwargs)

            yield StatusMessage("Starting to send email...")

            send_smtp_email = SendSMTPEmail(self.opts, self.mail_data)

            if not mail_incident_id:
                raise SimpleSendEmailException("mail_incident_id cannot be empty.")

            self.incident_data = send_smtp_email.get_incident_data(mail_incident_id)

            success = True
            email_message = None
            text = "N/A"

            if mail_body_html:
                log.info("Rendering template")
                mail_body_html = send_smtp_email.render_template(mail_body_html, self.incident_data, self.mail_data)
                text = mail_body_html
                email_message = send_smtp_email.send(body_html=mail_body_html)
            elif mail_body_text:
                log.info("Rendering text")
                text = mail_body_text
                email_message = send_smtp_email.send(body_text=mail_body_text)

            if not email_message:
                success = False
                log.error("Email was not sent, likely due to jinja template errors")

            yield StatusMessage("Done with sending email...")
            
            results = payload.done(success=True, content={
                "inputs" : [mail_from, mail_to, mail_cc, mail_bcc, mail_subject],
                "message": email_message,
                "text" : text
            })

            # Produce a FunctionResult with the results
            yield FunctionResult(results)
        except Exception:
            yield FunctionError()

    @staticmethod
    def split_string(in_string):
        if in_string:
            return in_string.split(',')
        return []

    def process_attachments(self, inc_id):
        file_list = []
        incident_attachment_list = self.rest_client().get("/incidents/{inc_id}/attachments?handle_format=objects".
                                                          format(inc_id=inc_id))
        for incident_attachment in incident_attachment_list:
            file_name = incident_attachment["name"]
            file_contents = self.rest_client().get_content("/incidents/{inc_id}/attachments/{attach_id}/contents".
                                                           format(inc_id=inc_id,attach_id=incident_attachment["id"]))
            tempdir = tempfile.mkdtemp()
            file_path = os.path.join(tempdir, file_name)
            with open(file_path, "wb+") as temp_file:
                temp_file.write(file_contents)

            file_list.append(file_path)
        return set(file_list)


class SimpleSendEmailException(Exception):
    """Exception for Send Email errors"""
    def __init__(self, message):
        log.error("SimpleSendEmailException %s", message)
