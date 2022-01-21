# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
import base64
import errno
import json
import os
import smtplib
import ssl
import logging
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ssl import Purpose
from jinja2 import Environment, select_autoescape
from resilient_circuits import ResilientComponent
from resilient_lib import RequestsCommon
from resilient_lib.components.integration_errors import IntegrationError
from fn_outbound_email.lib.template_helper import TemplateHelper

log = logging.getLogger(__name__)

CONFIG_DATA_SECTION = 'fn_outbound_email'
SMTP_DEFAULT_CONN_TIMEOUT = 15
SMTP_DEFAULT_PORT = '25'


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
        # OAuth2 authentication properties
        self.refresh_token = self.smtp_config_section.get("refresh_token")
        self.client_id = self.smtp_config_section.get("client_id")
        self.client_secret = self.smtp_config_section.get("client_secret")
        self.tenant_id = self.smtp_config_section.get("tenant_id")
        self.token_url = self.smtp_config_section.get("token_url")
        if self.tenant_id:
            self.token_url = self.token_url.format(tenant_id=self.tenant_id)
        self.scope = self.smtp_config_section.get("scope")

        self.smtp_conn_timeout = int(self.smtp_config_section.get("smtp_conn_timeout", SMTP_DEFAULT_CONN_TIMEOUT))
        self.options = opts.get(CONFIG_DATA_SECTION, {})

        self.jinja_env = Environment(autoescape=select_autoescape(['html']),
                                     extensions=['jinja2.ext.do'])
        self.jinja_env.globals['template_helper'] = TemplateHelper(self)
        self.rc = RequestsCommon(opts=opts, function_opts=opts.get(CONFIG_DATA_SECTION, {}))
        if self.client_id:
            # Using OAuth2 authentication.
            self.get_oauth2_token()
            self.generate_oauth2_string()

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
                smtp_connection = smtplib.SMTP_SSL(host=self.smtp_server,
                                                   port=self.smtp_port,
                                                   certfile=self.smtp_cafile,
                                                   context=self.get_smtp_ssl_context(),
                                                   timeout=self.smtp_conn_timeout)
            else:
                log.info("Building generic connection object")
                smtp_connection = smtplib.SMTP(host=self.smtp_server,
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
                smtp_connection.set_debuglevel(True)
                smtp_connection.ehlo()
                log.info("Authenticating with SMTP server...")
                smtp_connection.docmd('AUTH', 'XOAUTH2 ' + base64.b64encode(bytes(self.oauth2_string, "utf-8"))
                                      .decode("utf-8"))

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
            if not os.path.isfile(attachment_path):
                continue

            with open(attachment_path, 'rb') as fp:
                mime_object = MIMEApplication(fp.read())

            # Set the filename parameter
            mime_object.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
            attachment_result_list.append(mime_object)
        return attachment_result_list

    def get_smtp_ssl_context(self):
        ssl_context = ssl.create_default_context(purpose=Purpose.SERVER_AUTH)
        ssl_context.check_hostname = self.smtp_config_section.get("smtp_ssl_cafile") not in ['False', 'false']

        # if True set to default context
        if self.smtp_config_section.get("smtp_ssl_cafile") in ['True', 'true']:
            return ssl_context

        if not os.path.isfile(self.smtp_config_section.get("smtp_ssl_cafile")):
            raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT),
                                    self.smtp_config_section.get("smtp_ssl_cafile"))

        ssl_context.load_verify_locations(cafile=self.smtp_config_section.get("smtp_ssl_cafile"))

        return ssl_context

    def get_incident_data(self, mail_incident_id):
        return self.rest_client().get("/incidents/{0}?handle_format=names".format(mail_incident_id))

    def render_template(self, template_string, incident_data, mail_data):
        template = self.jinja_env.from_string(template_string)
        return template.render(incident=incident_data, mail=mail_data)

    def get_oauth2_token(self):
        """"Get a new OAuth2 token.
        If a refresh token is defined run the refresh_token flow else
        use client_credentials flow.

        Args:
            None
        Returns:
            Set OAuth2 access token attribute [str]
        Raises:
            IntegrationError: [description]
        """
        url = self.token_url

        post_data = {
            "client_id": self.client_id,
            "scope": [self.scope, "https://outlook.office.com/SMTP.Send"],
            "client_secret": self.client_secret,
        }
        if self.refresh_token:
            # Use refresh token to renew access token.
            post_data.update({"refresh_token": self.refresh_token})
            post_data.update({"grant_type": "refresh_token"})
        else:
            post_data.update({"grant_type": "client_credentials"})

        result = self.rc.execute_call_v2("POST", url, data=post_data)
        r_json = result.json()

        if "access_token" in r_json:
            self.oauth2_token = r_json['access_token']
            return True

        msg = u"Unable to authenticate: Error: {}\nDescription: {}"\
            .format(r_json.get("error"), r_json.get("error_description"))
        raise IntegrationError(msg)

    def generate_oauth2_string(self):
        """Generate an OAuth2 authentication string.

        Args:
            None
        Returns:
          Sets the string for the OAuth2 mechanism.
        """
        auth_string = "user={0}\x01auth=Bearer {1}\x01\x01".format(self.smtp_user, self.oauth2_token)
        self.oauth2_string = auth_string

class SimpleSendEmailException(Exception):
    """Exception for Send Email errors"""
    def __init__(self, message):
        log.error("SimpleSendEmailException %s", message)

