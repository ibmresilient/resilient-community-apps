# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import re
import base64
import logging
import exchangelib

from resilient_lib import IntegrationError

from exchangelib import (
    DELEGATE, IMPERSONATION, Account, CalendarItem,
    Configuration, Credentials, EWSDateTime,
    HTMLBody, Message)

from exchangelib.attachments import FileAttachment
from exchangelib.errors import (
    ErrorImpersonateUserDenied,
    ErrorNonExistentMailbox, UnauthorizedError)

from exchangelib.folders import FolderCollection
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
from exchangelib.restriction import Q
from exchangelib.items import SEND_TO_ALL_AND_SAVE_COPY

from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

from fn_exchange.lib import exchange_helper

from fn_exchange.lib.exchange_helper import (
    NoMailboxError,
    ServerConnectionError,
    CredentialsError,
    ImpersonationError)


class exchange_interface:

    def __init__(self, rc, options):
        self.options = options
        self.rc = rc
        self.log = logging.getLogger(__file__)


    def connect_to_account(self, primary_smtp_address, impersonation=False) -> exchangelib.Account:
        """Connect to specified account and return it"""

        verify_cert = self.options.get('verify_cert')
        server   = self.options.get('server')
        username = self.options.get('username')
        password = self.options.get('password')
        proxies  = self.rc.get_proxies()

        if verify_cert and verify_cert.lower() == "true":
            proxy_base_adapter = HTTPAdapter
            self.log.info("Verify certificate enabled")
        else:
            proxy_base_adapter = NoVerifyHTTPAdapter
            self.log.info("Verify certificate enabled")

        BaseProtocol.HTTP_ADAPTER_CLS = exchange_helper.get_proxy_adapter(proxy_base_adapter, proxies)

        # Decide whether or not to use impersonation access
        if impersonation:
            self.log.info("Access type set to IMPERSONATE")
            access_type = IMPERSONATION
        else:
            self.log.info("Access type set to DELEGATE")
            access_type = DELEGATE

        # Use credentials to retrieve account
        try:
            self.log.info("Using provided credentials to establish a connection")
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
            self.log.info("Successfully connected!")
            
        except ErrorNonExistentMailbox:
            raise NoMailboxError(primary_smtp_address)

        except ConnectionError:
            raise ServerConnectionError(server)

        except UnauthorizedError:
            raise CredentialsError()

        except ErrorImpersonateUserDenied:
            raise ImpersonationError(username, primary_smtp_address)

        return account


    def get_emails(self, function_parameters) -> exchangelib.restriction.Q:
        """Get queried emails"""

        username   = function_parameters.get("username")
        num_emails = function_parameters.get("num_emails")
        email_ids  = function_parameters.get("email_ids")
        src_folder = function_parameters.get("src_folder")
        start_date = function_parameters.get("start_date")
        end_date   = function_parameters.get("end_date")
        sender  = function_parameters.get("sender")
        subject = function_parameters.get("subject")
        body    = function_parameters.get("body")
        has_attachments     = function_parameters.get("has_attachments")
        order_by_recency    = function_parameters.get("order_by_recency")
        search_subfolders   = function_parameters.get("search_subfolders")
        default_folder_path = self.options.get("default_folder_path")

        account = self.connect_to_account(username)

        src_folder = default_folder_path if src_folder is None else src_folder

        split_folder_paths = re.findall('(?:[^,"]|"(?:\\.|[^"])*")+', src_folder)
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
                id_query = id_query | Q(message_id=email_id.strip()) 
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

        if has_attachments:
            filtered_emails = filtered_emails.filter(has_attachments=has_attachments)

        if not order_by_recency:
            if order_by_recency:
                filtered_emails = filtered_emails.order_by('-datetime_received')
            else:
                filtered_emails = filtered_emails.order_by('datetime_received')

        if num_emails:
            filtered_emails = filtered_emails[:num_emails]

        return filtered_emails


    def create_email_message(self, function_parameters) -> dict:
        """Create an email message object"""
        username    = function_parameters.get("username")
        msg_subject = function_parameters.get("msg_subject")
        msg_body    = function_parameters.get("msg_body")
        recipients  = function_parameters.get("recipients")

        account = self.connect_to_account(username, impersonation=(username.lower() != self.options.get("email").lower()))
        
        self.log.info("Composing email")
        html_body = HTMLBody('<html><body>{}</body></html>').format(msg_body)
        email = Message(
            account=account,
            folder=account.sent,
            subject=msg_subject,
            body=html_body,
            to_recipients=[recipient.strip() for recipient in recipients.split(',')])

        self.log.info("Sending email and saving to SENT folder")
        email.send_and_save()

        return {
            'recipients' : function_parameters["recipients"],
            'sender'     : function_parameters["username"],
            'msg_subject': function_parameters["msg_subject"],
            'msg_body'   : function_parameters["msg_body"]}


    def create_meeting(self, function_parameters) -> dict:
        """Create an email message object"""    
        username = function_parameters.get("username")
        start_time = function_parameters.get("start_time")
        end_time = function_parameters.get("end_time")
        meeting_subject = function_parameters.get("subject")
        meeting_body = function_parameters.get("body")
        required_attendees = function_parameters.get("required_attendees")
        optional_attendees = function_parameters.get("optional_attendees")

        account = self.connect_to_account(username, impersonation=(username.lower() != self.options.get("email").lower()))

        if required_attendees:
            required_attendees = [ra.strip() for ra in required_attendees.split(',')]
        if optional_attendees:
            optional_attendees = [oa.strip() for oa in optional_attendees.split(',')]

        tz = exchange_helper.get_timezone()

        self.log.info("Creating meeting using the provided parameters")
        meeting = CalendarItem(
            account=account,
            folder=account.calendar,
            start=EWSDateTime.fromtimestamp(start_time/1000, tz=tz),
            end=EWSDateTime.fromtimestamp(end_time/1000, tz=tz),
            subject=meeting_subject,
            body=meeting_body,
            required_attendees=required_attendees,
            optional_attendees=optional_attendees)

        self.log.info("Sending out meeting invite and saving a copy")
        meeting.save(send_meeting_invitations=SEND_TO_ALL_AND_SAVE_COPY)

        return {
            'required_attendees': required_attendees,
            'optional_attendees': optional_attendees,
            'sender': username,
            'subject': meeting_subject,
            'body': meeting_body,
            'start_time': start_time,
            'end_time': end_time}


    def move_emails(self, function_parameters, delete_src_folder=False) -> tuple:
        """Moving mails to a specified folder"""
        username   = function_parameters.get("username")
        src_folder = function_parameters.get("src_folder")
        dst_folder = function_parameters.get("dst_folder")
        account    = self.connect_to_account(username)
        
        if not delete_src_folder:
            self.log.info("Querying emails base on provided attributes")
            retrieved_emails = self.get_emails(function_parameters)
        else:
            self.log.info(f"Finding all emails in the {src_folder} and moving them to {dst_folder}")
            force_delete = function_parameters.get("force_delete")

            if not force_delete:
                self.log.info("Folder will not be deleted if subfolders detected")
                _src_folder = exchange_helper.go_to_folder(username, account, src_folder)
                if _src_folder.child_folder_count != 0:
                    msg = f'{src_folder} has subfolders'
                    self.log.error(msg)
                    raise IntegrationError(msg)
                else:
                    self.log.error("No subfolders found. Source folder will be deleted after moving files")
                    retrieved_emails = _src_folder.all()
            else:
                self.log.info("Folder will be deleted even if subfolders detected")
                retrieved_emails = self.get_emails({
                    "username"  : username,
                    "src_folder" : src_folder,
                    "search_subfolders" : True})

        num_moved = retrieved_emails.count()
        self.log.info(f"Search email operation complete, {num_moved} emails found")
        results = self.create_email_function_results(retrieved_emails)

        self.log.info(f"Moving emails to {dst_folder}")
        results["src_folder"] = exchange_helper.go_to_folder(username, account, src_folder)
        results["dst_folder"] = exchange_helper.go_to_folder(username, account, dst_folder)

        return results, retrieved_emails


    def create_email_function_results(self, emails) -> dict:
        """
        Create function results from email query results

        Example :
        -------
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
                            'attachment_name': 'attachment.xlsx',
                            'attachment_content_type': 'spreadsheet',
                            'attachment_size': '8842',
                            'attachment_base64': 'attachment encoded in base 64'}}}
        """
        results = {
            'email_ids': [],
            'emails': {}}

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
