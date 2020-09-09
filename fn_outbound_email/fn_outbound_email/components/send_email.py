# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
#pragma pylint: disable=unused-argument, no-self-use, line-too-long
"""Function implementation"""

from __future__ import print_function

import logging
import os
import tempfile
from resilient_circuits import ResilientComponent, function, handler, StatusMessage, FunctionResult, FunctionError
from resilient_lib import ResultPayload, validate_fields
from fn_outbound_email.lib.smtp_mailer import SendSMTPEmail


log = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 20
DEFAULT_TLS_SMTP = 'starttls'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'send_email"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)
        self.incident_data = {}
        self.mail_data = {}
        self.opts = opts
        self.smtp_config_section = self.opts.get(CONFIG_DATA_SECTION, {})
        validate_fields(["smtp_server", "smtp_port"], self.smtp_config_section)

        self.template_file_path = self.smtp_config_section.get('template_file')
        self.smtp_port_choice = str(self.smtp_config_section.get("smtp_"))
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

        def conditional_parameters(mail_body_text):
            if self.smtp_config_section.get("smtp_ssl_mode") == DEFAULT_TLS_SMTP and self.smtp_user is not None:
                mail_from = self.smtp_user
            else:
                mail_from = kwargs.get("mail_from")  # text
            if self.template_file_path and not mail_body_text:
                with open(self.template_file_path, "r") as definition:
                    mail_body_html = definition.read()
                    log.info("Using custom jinja template instead of default, path: %s", self.template_file_path)
                    if definition.name.find("example_send_email.jinja") == -1:
                        jinja = False
                    else:
                        jinja = True
            else:
                mail_body_html = kwargs.get("mail_body_html")
                jinja = False
            if self.smtp_user and not kwargs.get("mail_to"):
                mail_to = self.smtp_user
            else:
                mail_to = kwargs.get("mail_to")
            email_message = None
            text = ""
            return mail_from, mail_to, mail_body_html, jinja, email_message, text

        try:
            # Get the function parameters:
            mail_to = kwargs.get("mail_to") #text
            mail_cc = kwargs.get("mail_cc") #text
            mail_bcc = kwargs.get("mail_bcc") #text
            mail_subject = kwargs.get("mail_subject") #text
            mail_body_text = kwargs.get("mail_body_text") #text
            mail_attachments = kwargs.get("mail_attachments") #text
            mail_incident_id = kwargs.get("mail_incident_id") #number
            # Get the conditional function parameters:
            mail_from, mail_to, mail_body_html, jinja, email_message, text = conditional_parameters(mail_body_text)

            if not mail_from:
                raise Exception("no sender address specified")
            if not mail_cc:
                mail_cc = ""
            if not mail_bcc:
                mail_bcc = ""
            
            log.info("mail_from: %s", mail_from)
            log.info("mail_to: %s", mail_to)
            log.info("mail_cc: %s", mail_cc)
            log.info("mail_bcc: %s", mail_bcc)
            log.info("mail_subject: %s", mail_subject)
            log.info("mail_body_html: %s", mail_body_html)
            log.info("mail_body_text: %s", mail_body_text)
            log.info("mail_attachments: %s", mail_attachments)

            self.mail_data['mail_from'] = mail_from
            self.mail_data['mail_to'] = FunctionComponent.split_string(mail_to)
            self.mail_data['mail_cc'] = FunctionComponent.split_string(mail_cc)
            self.mail_data['mail_bcc'] = FunctionComponent.split_string(mail_bcc)
            self.mail_data['mail_subject'] = mail_subject
            self.mail_data['mail_attachments'] = self.process_attachments(inc_id=mail_incident_id, attachments=mail_attachments)

            payload = ResultPayload(CONFIG_DATA_SECTION, **kwargs)
            validate_fields(["mail_subject", "mail_incident_id"], kwargs)

            yield StatusMessage("Starting to send email...")

            send_smtp_email = SendSMTPEmail(self.opts, self.mail_data)

            if not mail_incident_id:
                raise SimpleSendEmailException("mail_incident_id cannot be empty.")

            self.incident_data = send_smtp_email.get_incident_data(mail_incident_id)

            if mail_body_html:
                log.info("Rendering template")
                mail_body_html = send_smtp_email.render_template(mail_body_html, self.incident_data, self.mail_data)

                if not mail_body_html:
                    raise Exception("Local jinja template not valid, please retry sending with valid template locally or remove file to use default")

                if not jinja:
                    error_msg = send_smtp_email.send(body_html=mail_body_html)
                    text = mail_body_html
                else:
                    mail_body_html = mail_body_html.replace('---===newline===---', '<div>')
                    error_msg = send_smtp_email.send(body_html=mail_body_html)
                    text = mail_body_html.replace('---===newline===---', '<br>')
            elif mail_body_text:
                log.info("Rendering text")
                text = mail_body_text
                error_msg = email_message = send_smtp_email.send(body_text=mail_body_text)

            if error_msg:
                yield StatusMessage("An error occurred while sending the email: {}".format(error_msg))

            yield StatusMessage("Done with sending email...")
            results = payload.done(success=True, content={
                "inputs" : [mail_from, mail_to, mail_cc, mail_bcc, mail_subject],
                "message": email_message,
                "text" : text,
                "success": (not error_msg)
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

    def temp_attach(self, inc_id, incident_attachment_list, attachments, file_list):
        updated_lists = list(file_list)
        tempdir = tempfile.mkdtemp()
        for incident_attachment in incident_attachment_list:
            file_name = incident_attachment["name"]
            if file_name in attachments:
                file_contents = self.rest_client().get_content("/incidents/{inc_id}/attachments/{attach_id}/contents".
                                                                format(inc_id=inc_id,
                                                                attach_id=incident_attachment["id"]))
                file_path = os.path.join(tempdir, file_name)
                with open(file_path, "wb+") as temp_file:
                    temp_file.write(file_contents)
                updated_lists.append(file_path)
        return set(updated_lists)

    def process_attachments(self, inc_id, attachments):
        file_list = []
        incident_attachment_list = self.rest_client().get("/incidents/{inc_id}/attachments?handle_format=objects".
                                                          format(inc_id=inc_id))
        if attachments == "*": # send all attachments
            all_attach = temp_attach(self, inc_id, incident_attachment_list, attachments, file_list)
            return all_attach
        elif attachments: # send selected attachments
            attachments = FunctionComponent.split_string(attachments)
            set_attach = temp_attach(self, inc_id, incident_attachment_list, attachments, file_list)
            return set_attach
        else: # no attachments
            return set(file_list)



class SimpleSendEmailException(Exception):
    """Exception for Send Email errors"""
    def __init__(self, message):
        log.error("SimpleSendEmailException %s", message)
