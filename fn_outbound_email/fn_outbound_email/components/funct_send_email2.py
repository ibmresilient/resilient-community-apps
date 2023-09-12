# -*- coding: utf-8 -*-
#(c) Copyright IBM Corp. 2010, 2023. All Rights Reserved.
#pragma pylint: disable=line-too-long

"""AppFunction implementation"""
from bs4 import BeautifulSoup
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, str_to_bool, s_to_b
from fn_outbound_email.lib.soar_helper import SoarHelper, split_string
from fn_outbound_email.lib.configure_tab import init_email_tab
from fn_outbound_email.lib.smtp_mailer import SendSMTPEmail
from fn_outbound_email.lib.template_helper import get_template, get_template_names, CONFIG_DATA_SECTION

FN_NAME = "send_email2"
MAIL_TEMPLATE_SELECT = "mail_template_select" # activity field to change update the select list

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'send_email2'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, CONFIG_DATA_SECTION)

        # configure tab?
        app_config = opts.get(CONFIG_DATA_SECTION)
        if str_to_bool(app_config.get("enable_email_conversations", "false")):
            init_email_tab()

        # read the template names to include in the selection list

        select_list = get_template_names(opts)
        if select_list:
            soar_helper = SoarHelper(self.rest_client())
            soar_helper.update_select_list(MAIL_TEMPLATE_SELECT, select_list)


    @app_function(FN_NAME)
    def _app_function(self, fn_inputs):
        """
        Function: Send a plain text or HTML-formatted email with Resilient Incident details in the email body as well as incident attachments added to this outgoing email.
        Inputs:
            -   fn_inputs.mail_incident_id
            -   fn_inputs.mail_to
            -   fn_inputs.mail_from
            -   fn_inputs.mail_cc
            -   fn_inputs.mail_bcc
            -   fn_inputs.mail_subject
            -   fn_inputs.mail_body
            -   fn_inputs.mail_message_id
            -   fn_inputs.mail_in_reply_to
            -   fn_inputs.mail_attachments
            -   fn_inputs.mail_importance
            -   fn_inputs.mail_inline_template
            -   fn_inputs.mail_template_label
            -   fn_inputs.mail_merge_body
            -   fn_inputs.mail_encryption_recipients
        """

        yield self.status_message(f"Starting App Function: '{FN_NAME}'")

        mail_data = fn_inputs._asdict()
        # validations
        validate_fields(["smtp_server"], self.app_configs)
        validate_fields(["mail_incident_id", "mail_to"], fn_inputs)

        if mail_data.get("mail_inline_template") and mail_data.get("mail_template_label"):
            raise ValueError("Specify either mail_inline_template or mail_template_label but not both")

        # configuration setup
        soar_helper = SoarHelper(self.rest_client())
        mail_incident_id = fn_inputs.mail_incident_id

        mail_data['mail_to'] = split_string(mail_data.get('mail_to'))
        mail_data['mail_cc'] = split_string(mail_data.get('mail_cc'))
        mail_data['mail_bcc'] = split_string(mail_data.get('mail_bcc'))
        mail_data['mail_attachments'] = soar_helper.process_attachments(inc_id=mail_data.get('mail_incident_id'),
                                                                        attachments=mail_data.get('mail_attachments'))

        if not mail_data.get('mail_from'):
            mail_data['mail_from'] = getattr(self.app_configs, "from_email_address")

        send_smtp_email = SendSMTPEmail(self.opts, mail_data)

        # if templates are specified, get the template data
        if mail_data.get('mail_inline_template') or mail_data.get('mail_template_label'):
            incident_data = soar_helper.get_incident_data(mail_incident_id)
            artifact_data = soar_helper.get_artifact_data(mail_incident_id)
            note_data = soar_helper.get_note_data(mail_incident_id)

            # inline template?
            if mail_data.get('mail_inline_template'):
                self.LOG.info("Rendering mail_inline_template")
                template_data = mail_data.get('mail_inline_template')
            else:
                self.LOG.info("Rendering template: %s", mail_data.get('mail_template_label'))
                template_data = get_template(self.opts,
                                             mail_data.get('mail_template_label'))

            if not template_data:
                rendered_mail_body = None
                error_msg = f"No template found: {mail_data.get('mail_template_label')}"
                yield self.status_message(error_msg)
            else:
                rendered_mail_body = send_smtp_email.render_template(template_data,
                                                                     incident_data,
                                                                     mail_data,
                                                                     artifact_data,
                                                                     note_data)
                self.LOG.debug("Rendered mail body: %s", rendered_mail_body)

                # is there the original email to include?
                if mail_data.get('mail_merge_body', False) and mail_data.get('mail_body'):
                    rendered_mail_body= f"{rendered_mail_body}\n{mail_data.get('mail_body')}"

                error_msg = send_msg(send_smtp_email,
                                     rendered_mail_body,
                                     encryption_certs=getattr(fn_inputs, 'mail_encryption_recipients'))
        elif mail_data.get('mail_body'):
            self.LOG.info("Non-rendered mail_body")
            rendered_mail_body = mail_data.get('mail_body')
            error_msg = send_msg(send_smtp_email,
                                 rendered_mail_body,
                                 encryption_certs=getattr(fn_inputs, 'mail_encryption_recipients'))
        else:
            error_msg = "No email body or template specified"

        if error_msg:
            rendered_mail_body = None
            yield self.status_message(f"An error occurred while sending the email: {error_msg}")

        results = {
            "mail_body": rendered_mail_body,
            "mail_from": mail_data.get('mail_from')
        }

        yield self.status_message(f"Finished running App Function: '{FN_NAME}'")

        # Produce a FunctionResult with the results
        yield FunctionResult(results,
                             success=not bool(error_msg),
                             reason=error_msg)

def send_msg(send_smtp_email, content, encryption_certs=None):
    """send the message, using the context of the content to send as html or plain text

    Args:
        send_smtp_email (SMTPMailer): mailer object
        content (str): body of email

    Returns:
        str: any error which occurred
    """
    encryption_certs_list = [s_to_b(cert) for cert in encryption_certs.split(',')] if encryption_certs else None

    if isHTML(content):
        return send_smtp_email.send(body_html=content, encryption_certs=encryption_certs_list)

    return send_smtp_email.send(body_text=content.replace('\n', '\r\n'), encryption_certs=encryption_certs_list)


def isHTML(content):
    """Use BeautifulSoup to determine if content contains HTML

    Args:
        content (str): body of email

    Returns:
        bool: true if html detected
    """
    soup = BeautifulSoup(content, 'html.parser')
    return bool(soup.find())
