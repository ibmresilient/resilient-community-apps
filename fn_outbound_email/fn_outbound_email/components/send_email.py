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


LOG = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 20
DEFAULT_TLS_SMTP = 'starttls'

class FunctionComponent(ResilientComponent):
    """Component that implements Resilient function 'send_email"""

    def __init__(self, opts):
        """constructor provides access to the configuration options"""
        super(FunctionComponent, self).__init__(opts)

        self.opts = opts
        self.smtp_config_section = self.opts.get(CONFIG_DATA_SECTION, {})
        validate_fields(["smtp_server", "smtp_port"], self.smtp_config_section)

        self.template_file_path = self.smtp_config_section.get('template_file')
        self.smtp_user = self.smtp_config_section.get("smtp_user")

        if self.template_file_path and not os.path.exists(self.template_file_path):
            LOG.error(u"Template file '%s' not found.", self.template_file_path)
            self.template_file_path = None

    @handler("reload")
    def _reload(self, event, opts):
        """Configuration options have changed, save new values"""
        self.smtp_config_section = opts.get(CONFIG_DATA_SECTION, {})

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
                    LOG.info("Using custom jinja template instead of default, path: %s", self.template_file_path)
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
            validate_fields(["mail_subject", "mail_incident_id"], kwargs)

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

            LOG.info("mail_from: %s", mail_from)
            LOG.info("mail_to: %s", mail_to)
            LOG.info("mail_cc: %s", mail_cc)
            LOG.info("mail_bcc: %s", mail_bcc)
            LOG.info("mail_subject: %s", mail_subject)
            LOG.info("mail_body_html: %s", mail_body_html)
            LOG.info("mail_body_text: %s", mail_body_text)
            LOG.info("mail_attachments: %s", mail_attachments)

            yield StatusMessage("Starting to send email...")
            payload = ResultPayload(CONFIG_DATA_SECTION, **kwargs)

            mail_data = {}
            mail_data['mail_from'] = mail_from
            mail_data['mail_to'] = FunctionComponent.split_string(mail_to)
            mail_data['mail_cc'] = FunctionComponent.split_string(mail_cc)
            mail_data['mail_bcc'] = FunctionComponent.split_string(mail_bcc)
            mail_data['mail_subject'] = mail_subject
            mail_data['mail_attachments'] = self.process_attachments(inc_id=mail_incident_id, attachments=mail_attachments)

            send_smtp_email = SendSMTPEmail(self.opts, mail_data)

            incident_data = send_smtp_email.get_incident_data(mail_incident_id)

            if mail_body_html:
                LOG.info("Rendering template")
                mail_body_html = send_smtp_email.render_template(mail_body_html, incident_data, mail_data)

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
                LOG.info("Rendering text")
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

    def temp_attach(self, inc_id, incident_attachment_list, requested_attachments):
        """[match attachments found in an incident with the list provided by the function call and
            prep for sending email]

        Args:
            inc_id ([int]):
            incident_attachment_list ([json]): [results of api call to get all incident attachments ]
            requested_attachments ([list]): [list of attachments to include, or '*' for all]

        Returns:
            [set]: [file paths of attachments to send]
        """
        remaining_attachment_list = requested_attachments.copy()
        attachment_path = []
        tempdir = tempfile.mkdtemp()

        for incident_attachment in incident_attachment_list:
            file_name = incident_attachment["name"]
            if file_name in requested_attachments:
                remaining_attachment_list.remove(file_name)

                file_contents = self.rest_client().get_content("/incidents/{inc_id}/attachments/{attach_id}/contents".
                                                                format(inc_id=inc_id,
                                                                attach_id=incident_attachment["id"]))
                file_path = os.path.join(tempdir, file_name)
                with open(file_path, "wb+") as temp_file:
                    temp_file.write(file_contents)
                attachment_path.append(file_path)

        # send warnings when attachments are not found
        if remaining_attachment_list:
            LOG.warning(u"Unable to find the following attachments: %s", u",".join(remaining_attachment_list))

        return set(attachment_path)

    def process_attachments(self, inc_id, attachments):
        """[return a list of filepaths to include as attachments ]

        Args:
            inc_id ([int]): [incident id]
            attachments ([str]): [comma separated attachment list or '*' for all]

        Returns:
            [set]: [file paths for attachments]
        """
        incident_attachment_list = self.rest_client().get("/incidents/{inc_id}/attachments?handle_format=objects".
                                                          format(inc_id=inc_id))
        # convert the list of requested attachments
        if attachments and attachments == "*":
            # include all incident attachments
            attachment_list = [incident_attachment["name"] for incident_attachment in incident_attachment_list]
        else:
            attachment_list = [attach.strip() for attach in FunctionComponent.split_string(attachments)] \
                                if attachments else []

        all_attach = self.temp_attach(inc_id, incident_attachment_list, attachment_list)
        all_attach and LOG.debug(u"Attachments to include: %s", u",".join(all_attach))

        return all_attach


class SimpleSendEmailException(Exception):
    """Exception for Send Email errors"""
    def __init__(self, message):
        LOG.error("SimpleSendEmailException %s", message)
