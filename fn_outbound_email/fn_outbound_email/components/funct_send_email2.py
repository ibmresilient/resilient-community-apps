# -*- coding: utf-8 -*-

"""AppFunction implementation"""
from bs4 import BeautifulSoup
import logging
from resilient_circuits import AppFunctionComponent, app_function, FunctionResult
from resilient_lib import validate_fields, str_to_bool
from fn_outbound_email.lib.soar_helper import SoarHelper, split_string
from fn_outbound_email.lib.configure_tab import init_email_tab
from fn_outbound_email.lib.smtp_mailer import SendSMTPEmail
from fn_outbound_email.lib.template_helper import get_template

PACKAGE_NAME = "fn_outbound_email"
FN_NAME = "send_email2"
LOG = logging.getLogger(__name__)

class FunctionComponent(AppFunctionComponent):
    """Component that implements function 'send_email2'"""

    def __init__(self, opts):
        super(FunctionComponent, self).__init__(opts, PACKAGE_NAME)

        # configure tab?
        app_config = opts.get(PACKAGE_NAME)
        if str_to_bool(app_config.get("enable_email_conversations", "false")):
            init_email_tab()

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
            -   fn_inputs.mail_template_name
        """

        yield self.status_message("Starting App Function: '{0}'".format(FN_NAME))

        mail_data = fn_inputs._asdict()
        # validations
        validate_fields(["smtp_server"], self.app_configs)
        validate_fields(["mail_incident_id", "mail_to", "mail_from"], fn_inputs)

        if mail_data.get("mail_inline_template") and mail_data.get("mail_template_name"):
            raise ValueError("Specify either mail_inline_template or mail_template_name but not both")

        if mail_data.get("mail_body") and \
           (mail_data.get("mail_template_name") or mail_data.get("mail_inline_template")):
            raise ValueError("Special either mail_body or one of mail_inline_template or mail_template_name")

        # configuration setup
        soar_helper = SoarHelper(self.rest_client())
        mail_incident_id = fn_inputs.mail_incident_id

        mail_data['mail_to'] = split_string(mail_data.get('mail_to'))
        mail_data['mail_cc'] = split_string(mail_data.get('mail_cc'))
        mail_data['mail_bcc'] = split_string(mail_data.get('mail_bcc'))
        mail_data['mail_attachments'] = soar_helper.process_attachments(inc_id=mail_data.get('mail_incident_id'),
                                                                        attachments=mail_data.get('mail_attachments'))

        send_smtp_email = SendSMTPEmail(self.opts, mail_data)

        # if templates are specified, get the template data
        if mail_data.get('mail_inline_template') or mail_data.get('mail_template_name'):
            incident_data = soar_helper.get_incident_data(mail_incident_id)
            artifact_data = soar_helper.get_artifact_data(mail_incident_id)
            note_data = soar_helper.get_note_data(mail_incident_id)

            # inline template?
            if mail_data.get('mail_inline_template'):
                LOG.info("Rendering mail_inline_template")
                template_data = mail_data.get('mail_inline_template')
            else:
                LOG.info("Rendering template: %s", mail_data.get('mail_template_name'))
                template_data = get_template(self.app_configs._asdict(),
                                             mail_data.get('mail_template_name'))

            rendered_mail_body = send_smtp_email.render_template(template_data,
                                                                 incident_data,
                                                                 mail_data,
                                                                 artifact_data,
                                                                 note_data)
            LOG.debug("Rendered mail body: %s", rendered_mail_body)

            error_msg = send_msg(send_smtp_email, rendered_mail_body)
        elif mail_data.get('mail_body'):
            LOG.info("Non-rendered mail_body")
            rendered_mail_body = mail_data.get('mail_body')
            error_msg = send_msg(send_smtp_email, rendered_mail_body)
        else:
            raise ValueError("No email body or template specified")

        if error_msg:
            yield self.status_message("An error occurred while sending the email: {}".format(error_msg))

        results = {
            "mail_body": rendered_mail_body
        }

        yield self.status_message("Finished running App Function: '{0}'".format(FN_NAME))

        # Produce a FunctionResult with the results
        yield FunctionResult(results,
                             success=not bool(error_msg),
                             reason=error_msg)

def send_msg(send_smtp_email, content):
    """send the message, using the context of the content to send as html or plain text

    Args:
        send_smtp_email (SMTPMailer): mailer object
        content (str): body of email

    Returns:
        str: any error which occured
    """
    if isHTML(content):
        return send_smtp_email.send(body_html=content)
    else:
        return send_smtp_email.send(body_text=content.replace('\n', '\r\n'))


def isHTML(content):
    """Use BeautifulSoup to determine if content contains HTML

    Args:
        content (str): body of email

    Returns:
        bool: true if html detected
    """
    soup = BeautifulSoup(content, 'html.parser')
    return bool(soup.find())
