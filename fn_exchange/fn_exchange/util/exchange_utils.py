# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import base64
import re
import logging

from exchangelib import (
    DELEGATE,IMPERSONATION, Account, CalendarItem,
    Configuration, Credentials, EWSDateTime,
    HTMLBody, Message)
from exchangelib.attachments import FileAttachment
from exchangelib.errors import (
    ErrorImpersonateUserDenied,
    ErrorNonExistentMailbox, UnauthorizedError)

from exchangelib.folders import FolderCollection
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
from exchangelib.restriction import Q

from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

from fn_exchange.lib import exchange_helper

from fn_exchange.lib.exchange_helper import (
    NoMailboxError,
    ServerConnectionError,
    CredentialsError,
    ImpersonationError)


class exchange_utils:

    def __init__(self, rc, options):
        self.options = options
        self.rc = rc
        self.log = logging.getLogger(__file__)


    def connect_to_account(self, primary_smtp_address, impersonation=False):
        """Connect to specified account and return it"""

        verify_cert = self.options.get('verify_cert')
        server = self.options.get('server')
        username = self.options.get('username')
        password = self.options.get('password')
        proxies = self.rc.get_proxies()

        if verify_cert and verify_cert.lower() == "true":
            proxy_base_adapter = HTTPAdapter
        else:
            proxy_base_adapter = NoVerifyHTTPAdapter

        BaseProtocol.HTTP_ADAPTER_CLS = exchange_helper.get_proxy_adapter(proxy_base_adapter, proxies)

        # Decide whether or not to use impersonation access
        access_type = IMPERSONATION if impersonation else DELEGATE

        # Use credentials to retrieve account
        try:
            credentials = Credentials(
                username=username,
                password=password)

            config = Configuration(
                server=server,
                credentials=credentials)

            account = Account(
                primary_smtp_address=primary_smtp_address,
                config=config,
                autodiscover=False,
                access_type=access_type)
            
        except ErrorNonExistentMailbox:
            raise NoMailboxError(primary_smtp_address)

        except ConnectionError:
            raise ServerConnectionError(server)

        except UnauthorizedError:
            raise CredentialsError()

        except ErrorImpersonateUserDenied:
            raise ImpersonationError(username, primary_smtp_address)

        return account


    def get_emails(self, function_parameters):
        """Get queried emails"""

        username    = function_parameters["username"]
        num_emails  = function_parameters["num_emails"]
        email_ids   = function_parameters["email_ids"]
        folder_path = function_parameters["folder_path"]

        start_date  = function_parameters["start_date"]
        end_date    = function_parameters["end_date"]

        sender  = function_parameters["sender"]
        subject = function_parameters["subject"]
        body    = function_parameters["body"]

        has_attachments     = function_parameters["has_attachments"]
        order_by_recency    = function_parameters["order_by_recency"]
        search_subfolders   = function_parameters["search_subfolders"]
        default_folder_path = self.options.get("default_folder_path")

        account = self.connect_to_account(username)

        folder_path = default_folder_path if folder_path is None else folder_path

        split_folder_paths = re.findall('(?:[^,"]|"(?:\\.|[^"])*")+', folder_path)
        folders = [exchange_helper.go_to_folder(username, account, folder.strip()) for folder in split_folder_paths]

        # Search subfolders
        if search_subfolders:
            subfolders = []
            for folder in folders:
                if folder.child_folder_count > 0:
                    subfolders += list(folder.walk().get_folders())
            folders += subfolders

        folder_collection = FolderCollection(account=account, folders=folders)
        filtered_emails = folder_collection.all()

        if email_ids:
            id_query = Q()
            for email_id in email_ids.split(','):
                id_query = id_query | Q(sender=email_id.strip()) 
            filtered_emails = filtered_emails.filter(id_query)

        if sender:
            filtered_emails = filtered_emails.filter(sender=sender)

        if subject:
            filtered_emails = filtered_emails.filter(subject__contains=subject)

        if body:
            filtered_emails = filtered_emails.filter(body__contains=body)

        if start_date:
            # get YYYY/MM/DD from epoch time in milliseconds
            tz = self._get_tz()
            start_date = EWSDateTime.fromtimestamp(start_date/1000, tz=tz)
            filtered_emails = filtered_emails.filter(datetime_received__gte=start_date)

        if end_date:
            tz = self._get_tz()
            end_date = EWSDateTime.fromtimestamp(end_date/1000, tz=tz)
            filtered_emails = filtered_emails.filter(datetime_received__lte=end_date)

        if has_attachments is not None:
            filtered_emails = filtered_emails.filter(has_attachments=has_attachments)

        if order_by_recency is not None:
            if order_by_recency:
                filtered_emails = filtered_emails.order_by('-datetime_received')
            else:
                filtered_emails = filtered_emails.order_by('datetime_received')

        if num_emails:
            filtered_emails = filtered_emails[:num_emails]

        return filtered_emails


    def create_email_message(self, username, subject, body, to_recipients):
        """Create an email message object"""
        account = self.connect_to_account(username, impersonation=(username != self.email))
        html_body = HTMLBody('<html><body>{}</body></html>').format(body)
        email = Message(
            account=account,
            folder=account.sent,
            subject=subject,
            body=html_body,
            to_recipients=[recipient.strip() for recipient in to_recipients.split(',')])
        return email


    def create_meeting(self, username, start_time, end_time, subject, body, required_attendees, optional_attendees):
        """Create a meeting object"""
        account = self.connect_to_account(username, impersonation=(username != self.email))

        if required_attendees:
            required_attendees = [ra.strip() for ra in required_attendees.split(',')]
        if optional_attendees:
            optional_attendees = [oa.strip() for oa in optional_attendees.split(',')]

        tz = exchange_helper.get_timezone()

        meeting = CalendarItem(
            account=account,
            folder=account.calendar,
            start=EWSDateTime.fromtimestamp(start_time/1000, tz=tz),
            end=EWSDateTime.fromtimestamp(end_time/1000, tz=tz),
            subject=subject,
            body=body,
            required_attendees=required_attendees,
            optional_attendees=optional_attendees
        )
        return meeting


    def create_email_function_results(self, emails):
        """
        Create function results from email query results

        Example function results
        ------------------------
        results = {
            'email_ids': ['id1', 'idN'],
            'emails': {
                'id1': {
                    'subject': 'Email Subject',
                    'body': 'Subject body in HTML',
                    'mime_content': mime content of message
                    'sender_name': 'FirstName LastName',
                    'sender_email': 'example@example.com',
                    'attachment_ids': ['attachment_id1', 'attachment_id2'],
                    'attachments': {
                        'attachment_id1': {
                            'attachment_name': 'attachment.xslx',
                            'attachment_content_type': 'spreadsheet',
                            'attachment_size': '8842',
                            'attachment_base64': 'attachment encoded in base 64'
                        },
                        'attachment_id2': {
                            'attachment_name': '...',
                            'attachment_content_type': '...',
                            'attachment_size': '...',
                            'attachment_base64': 'attachment encoded in base 64'
                        }
                    }
                },
                'id2': {
                    'subject': 'Email Subject',
                    'body': 'Subject body in HTML',
                    'mime_content': mime content of message
                    'sender_name': 'FirstName LastName',
                    'sender_email': 'example@example.com',
                    'attachment_ids': ['attachment_id1', 'attachment_id2'],
                    'attachments': {
                        'attachment_id1': {
                            'attachment_name': 'attachment.xslx',
                            'attachment_content_type': 'spreadsheet',
                            'attachment_size': '8842',
                            'attachment_base64': 'attachment encoded in base 64'
                        },
                        'attachment_id2': {
                            'attachment_name': '...',
                            'attachment_content_type': '...',
                            'attachment_size': '...',
                            'attachment_base64': 'attachment encoded in base 64'
                        }
                    }
                }
            }
        }
        """
        results = {
            'email_ids': [],
            'emails': {}
        }
        # Create results
        for email in emails:
            # Check to see if item is an email
            if isinstance(email, Message):
                results['email_ids'].append(email.message_id)
                results['emails'][email.message_id] = {}
                curr_email = results['emails'][email.message_id]

                # Add subject and body
                curr_email['subject'] = email.subject
                curr_email['body'] = email.body

                # Add mime content
                curr_email['mime_content'] = email.mime_content.decode('utf-8')

                # Check to see if there is a sender, might be no sender if email is a draft
                if email.sender:
                    curr_email['sender_name'] = email.sender.name
                    curr_email['sender_email'] = email.sender.email_address
                else:
                    curr_email['sender_name'] = None
                    curr_email['sender_email'] = None

                # Check attachments
                curr_email['attachments'] = {}
                curr_email['attachment_ids'] = []
                for attachment in email.attachments:
                    if isinstance(attachment, FileAttachment):
                        curr_email['attachment_ids'].append(attachment.attachment_id.id)
                        curr_email['attachments'][attachment.attachment_id.id] = {}
                        curr_attachment = curr_email['attachments'][attachment.attachment_id.id]
                        curr_attachment['attachment_name'] = attachment.name
                        curr_attachment['attachment_content_type'] = attachment.content_type
                        curr_attachment['attachment_size'] = attachment.size
                        curr_attachment['attachment_base64'] = base64.b64encode(attachment.content).decode('utf-8')
        return results
