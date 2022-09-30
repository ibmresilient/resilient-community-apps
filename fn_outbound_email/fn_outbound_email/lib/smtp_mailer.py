# (c) Copyright IBM Corp. 2010, 2022. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import base64
from errno import ENOENT
from os import path, strerror
from smtplib import SMTP, SMTP_SSL
import logging
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ssl import Purpose, create_default_context
from jinja2 import Environment, select_autoescape
from resilient_circuits import ResilientComponent
from resilient_lib import RequestsCommon
from fn_outbound_email.lib.template_helper import TemplateHelper, CONFIG_DATA_SECTION
from fn_outbound_email.lib.oauth2 import OAuth2

log = logging.getLogger(__name__)

SMTP_DEFAULT_CONN_TIMEOUT = 20
SMTP_DEFAULT_PORT = '25'

# mail header information
MESSAGE_ID_HEADER = "Message-ID"
IN_REPLY_TO_HEADER = "In-Reply-To"
REFERENCES_HEADER = "References"
IMPORTANCE_HEADER = "Importance"
PRIORITY_HEADER = "X-Priority"
# translation between importance and x-priority setting
PRIORITY_LOOKUP = {
    "high": "1",
    "normal": "2",
    "low": "3"
}

class SendSMTPEmail(ResilientComponent):

    def __init__(self, opts, mail_context):
        self.opts = opts
        self.mail_context = mail_context

        self.from_address = self.mail_context['mail_from']
        self.to_address_list = self.mail_context['mail_to']
        self.cc_address_list = self.mail_context['mail_cc']
        self.bcc_address_list = self.mail_context['mail_bcc']
        self.mail_subject = self.mail_context['mail_subject']
        self.attachment_list = self.mail_context['mail_attachments']

        self.smtp_config_section = self.opts.get(CONFIG_DATA_SECTION, {})
        self.smtp_server = self.smtp_config_section.get("smtp_server")
        self.smtp_port = str(self.smtp_config_section.get("smtp_port", SMTP_DEFAULT_PORT))
        # cafile can be false or a path to a cafile cert
        if self.smtp_config_section.get("smtp_ssl_cafile", 'false').lower() == 'false':
            self.smtp_cafile = False
        else:
            self.smtp_cafile = self.smtp_config_section.get("smtp_ssl_cafile")
        if self.smtp_config_section.get("smtp_password", None) and self.smtp_config_section.get("oauth2_client_id", None):
            log.warning("The user and api key configuration settings are both enabled. Credentials will default to the "
                        "api key settings.")
        self.smtp_user = self.smtp_config_section.get("smtp_user")
        # Basic authentication property
        self.smtp_password = self.smtp_config_section.get("smtp_password")
        # OAuth2 authentication using OAuth2 class
        self.client_id = self.smtp_config_section.get("client_id")
        if self.client_id:
            self.oauth2 = OAuth2(opts)

        self.smtp_conn_timeout = int(self.smtp_config_section.get("smtp_conn_timeout", SMTP_DEFAULT_CONN_TIMEOUT))
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        self.jinja_env = Environment(autoescape=select_autoescape(['html']),
                                     extensions=['jinja2.ext.do'])
        self.jinja_env.globals['template_helper'] = TemplateHelper(self)
        self.rc = RequestsCommon(opts=opts, function_opts=opts.get(CONFIG_DATA_SECTION, {}))
        if self.client_id:
            # Using OAuth2 authentication.
            self.oauth2.refresh_access_token()
            self.oauth2.generate_oauth2_string()

        # headers
        self.headers = {}
        if self.mail_context.get('mail_message_id'):
            self.headers[MESSAGE_ID_HEADER] = self.mail_context['mail_message_id']
        if self.mail_context.get('mail_in_reply_to'):
            self.headers[IN_REPLY_TO_HEADER] = self.mail_context['mail_in_reply_to']
            self.headers[REFERENCES_HEADER] = self.mail_context['mail_in_reply_to']
        if self.mail_context.get('mail_importance'):
            self.headers[IMPORTANCE_HEADER] = self.mail_context['mail_importance']
            self.headers[PRIORITY_HEADER] = PRIORITY_LOOKUP.get(self.mail_context['mail_importance'].lower(), 2)

    def send(self, body_html="", body_text=""):
        if not self.opts:
            raise SimpleSendEmailException("opts required")
        if not self.from_address:
            raise SimpleSendEmailException("from_address required")
        log.info("Converting params")

        if not self.to_address_list or not isinstance(self.to_address_list, (set, list)):
            self.to_address_list = []
        if not self.cc_address_list or not isinstance(self.cc_address_list, (set, list)):
            self.cc_address_list = []
        if not self.bcc_address_list or not isinstance(self.bcc_address_list, (set, list)):
            self.bcc_address_list = []
        if not self.attachment_list or not isinstance(self.attachment_list, (set, list)):
            self.attachment_list = []

        if not any([self.to_address_list, self.cc_address_list, self.bcc_address_list]):
            raise SimpleSendEmailException('Recipients are required')

        multipart_message = MIMEMultipart()

        # set sender/recipients
        multipart_message['From'] = self.from_address
        multipart_message['To'] = ", ".join(self.to_address_list)
        multipart_message['CC'] = ", ".join(self.cc_address_list)
        multipart_message['BCC'] = ", ".join(self.bcc_address_list)

        # add headers if present
        if self.headers:
            for k,v in self.headers.items():
                multipart_message.add_header(k, v)

        log.info("Building MIME object")
        # Set subject
        multipart_message['Subject'] = self.mail_subject

        # Set body
        if body_html:
            body_part = MIMEText(body_html, _subtype="html", _charset="UTF-8")
            multipart_message.attach(body_part)
        if body_text:
            body_part = MIMEText(body_text, _subtype="plain", _charset="UTF-8")
            multipart_message.attach(body_part)

        # Add attachments
        if len(self.attachment_list) > 0:
            processed_attachments = SendSMTPEmail.process_attachments(self.attachment_list)
            for attachment in processed_attachments:
                multipart_message.attach(attachment)

        # convert to EML string
        composed = multipart_message.as_string()

        log.info("Starting email connection...")
        smtp_connection = None
        try:
            if self.smtp_config_section.get("smtp_ssl_mode") == "ssl":
                log.info("Building SSL connection object")
                smtp_connection = SMTP_SSL(host=self.smtp_server,
                                           port=self.smtp_port,
                                           certfile=self.smtp_cafile,
                                           context=self.get_smtp_ssl_context(),
                                           timeout=self.smtp_conn_timeout)
            else:
                log.info("Building generic connection object")
                smtp_connection = SMTP(host=self.smtp_server,
                                       port=self.smtp_port,
                                       timeout=self.smtp_conn_timeout)

                if self.smtp_config_section.get("smtp_ssl_mode") == "starttls":
                    log.info("Starting TLS...")
                    smtp_connection.ehlo()
                    smtp_connection.starttls()

            if self.smtp_user and not self.client_id:
                # Using Basic authentication.
                if not self.smtp_password:
                    raise SimpleSendEmailException('An SMTP user has been set; '
                                                   'the SMTP password from app.config cannot be null')
                log.info("Logging in to SMTP...")
                smtp_connection.login(user=self.smtp_user, password=self.smtp_password)

            if self.client_id:
                # Using OAuth2 authentication.
                smtp_connection.ehlo()
                log.info("Authenticating with SMTP server...")
                smtp_connection.docmd('AUTH', 'XOAUTH2 ' + base64.b64encode(bytes(self.oauth2.oauth2_string, "utf-8")).decode("utf-8"))

            log.info("Sending mail")
            smtp_connection.sendmail(self.from_address,
                                     set(list(self.to_address_list) + list(self.cc_address_list) +
                                         list(self.bcc_address_list)), composed)
            err_msg =  None
        except Exception as connection_error:
            log.error(connection_error)
            err_msg = str(connection_error)
        finally:
            try:
                if smtp_connection:
                    smtp_connection.quit()
            except Exception:
                pass

        return err_msg

    @staticmethod
    def process_attachments(attachment_list):
        attachment_result_list = []
        for attachment_path in attachment_list:
            with open(attachment_path, 'rb') as fp:
                mime_object = MIMEApplication(fp.read())

            # Set the filename parameter
            mime_object.add_header('Content-Disposition', 'attachment', filename=path.basename(attachment_path))
            attachment_result_list.append(mime_object)
        return attachment_result_list

    def get_smtp_ssl_context(self):
        ssl_context = create_default_context(purpose=Purpose.SERVER_AUTH)
        ssl_context.check_hostname = self.smtp_config_section.get("smtp_ssl_cafile") not in ['False', 'false']

        # if True set to default context
        if self.smtp_config_section.get("smtp_ssl_cafile") in ['True', 'true']:
            return ssl_context

        if not path.isfile(self.smtp_config_section.get("smtp_ssl_cafile")):
            raise FileNotFoundError(ENOENT, strerror(ENOENT),
                                    self.smtp_config_section.get("smtp_ssl_cafile"))

        ssl_context.load_verify_locations(cafile=self.smtp_config_section.get("smtp_ssl_cafile"))

        return ssl_context

    def get_incident_data(self, mail_incident_id):
        return self.rest_client().get("/incidents/{}?handle_format=names".format(mail_incident_id))

    def get_artifact_data(self, mail_incident_id):
        return self.rest_client().post("/incidents/{}/artifacts/query_paged?include_related_incident_count=true".format(mail_incident_id), payload={})

    def get_note_data(self, mail_incident_id):
        return self.rest_client().post("/incidents/{}/comments/query?include_tasks=false".format(mail_incident_id), payload={})

    def render_template(self, template_string, incident_data, mail_data, artifact_data={}, note_data={}):
        template = self.jinja_env.from_string(template_string)
        return template.render(incident=incident_data, mail=mail_data, artifact=artifact_data, note=note_data)

class SimpleSendEmailException(Exception):
    """Exception for Send Email errors"""
    def __init__(self, message):
        log.error("SimpleSendEmailException %s", message)
