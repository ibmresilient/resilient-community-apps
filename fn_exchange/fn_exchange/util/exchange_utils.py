# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
from exchangelib import Credentials, Account, DELEGATE, Configuration, EWSDateTime, EWSTimeZone, Message, CalendarItem, IMPERSONATION
from exchangelib.folders import FolderCollection
from exchangelib.attachments import FileAttachment
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
from exchangelib.restriction import Q
import time, base64
# Errors
from exchangelib.errors import ErrorNonExistentMailbox, UnauthorizedError, ErrorFolderNotFound, ErrorImpersonateUserDenied
from requests.exceptions import ConnectionError


class NoMailboxError(Exception):
    def __init__(self, email):
        fail_msg = 'The SMTP address {} has no mailbox associated with it'.format(email)
        super(NoMailboxError, self).__init__(fail_msg)


class ServerConnectionError(Exception):
    def __init__(self, server):
        fail_msg = 'Failed to connect to server: {}'.format(server)
        super(ServerConnectionError, self).__init__(fail_msg)


class CredentialsError(Exception):
    def __init__(self):
        fail_msg = 'The username or password specified in the config file is invalid'
        super(CredentialsError, self).__init__(fail_msg)


class FolderError(Exception):
    def __init__(self, email, folder, folder_path, tree):
        fail_msg = 'Either the user {} does not have access to the folder {} from the path ' \
                   '{}, or the folder does not exist'.format(email, folder, folder_path)
        print(tree)
        super(FolderError, self).__init__(fail_msg)

class ImpersonationError(Exception):
    def __init__(self, impersonator, impersonation_target):
        fail_msg = '{} does not have permission to impersonate {}'.format(impersonator, impersonation_target)
        super(ImpersonationError, self).__init__(fail_msg)


class exchange_utils:
    def __init__(self, opts):
        self.verify_cert = str_to_bool(get_config_option(opts, 'verify_cert'))
        self.server = get_config_option(opts, 'server')
        self.username = get_config_option(opts, 'username')
        self.email = get_config_option(opts, 'email')
        self.password = get_config_option(opts, 'password')
        self.default_folder_path = get_config_option(opts, 'default_folder_path')
        self.default_timezone = get_config_option(opts, 'default_timezone')

    def connect_to_account(self, primary_smtp_address, impersonation=False):
        """Connect to specified account and return it"""

        # Don't check certificates
        if not self.verify_cert:
            BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

        # Decide whether or not to use impersonation access
        access_type = IMPERSONATION if impersonation else DELEGATE

        # Use credentials to get account
        try:
            credentials = Credentials(username=self.username, password=self.password)
            config = Configuration(server=self.server, credentials=credentials)
            account = Account(primary_smtp_address=primary_smtp_address, config=config,
                              autodiscover=self.verify_cert, access_type=access_type)
        except ErrorNonExistentMailbox:
            raise NoMailboxError(primary_smtp_address)
        except ConnectionError:
            raise ServerConnectionError(self.server)
        except UnauthorizedError:
            raise CredentialsError()
        except ErrorImpersonateUserDenied:
            raise ImpersonationError(self.email, primary_smtp_address)
        return account

    def go_to_folder(self, username, folder_path):
        """Navigate to specified folder path and return it"""

        account = self.connect_to_account(username)
        folder = account.root
        if folder_path is None:
            return folder
        for dir in folder_path.split('/'):
            try:
                folder = folder / dir
            except ErrorFolderNotFound:
                raise FolderError(username, dir, folder_path, account.root.tree().encode('utf-8'))
        return folder

    def get_emails(self, username, folder_path=None, email_ids = None, sender=None, subject=None, body=None,
                   start_date=None, end_date=None, has_attachments=None, order_by_recency=None, num_emails=None,
                   search_subfolders=False):
        """Get queried emails"""

        # Default folder path if no folder path is specified
        folder_path = self.default_folder_path if folder_path is None else folder_path

        # Get list of all specified folders
        folders = [self.go_to_folder(username, folder) for folder in folder_path.split(',')]

        # Subfolder query check
        if search_subfolders:
            subfolders = []
            # For each specified folder
            for folder in folders:
                if folder.child_folder_count > 0:
                    subfolders += list(folder.walk().get_folders())
            folders += subfolders

        folder_collection = FolderCollection(account=self.connect_to_account(username), folders=folders)
        filtered_emails = folder_collection.all()

        # filter by ids
        if email_ids:
            id_query = Q()
            for email_id in email_ids.split(','):
                id_query = id_query | Q(message_id=email_id)
            filtered_emails = filtered_emails.filter(id_query)

        # filter by sender
        if sender:
            filtered_emails = filtered_emails.filter(sender=sender)

        if subject:
            filtered_emails = filtered_emails.filter(subject__contains=subject)

        if body:
            filtered_emails = filtered_emails.filter(body__contains=body)

        # filter by date
        if start_date:
            # get YYYY/MM/DD from epoch time in milliseconds
            start_date = parse_time(start_date)

            tz = EWSTimeZone.timezone(self.default_timezone)
            start = tz.localize(EWSDateTime(start_date[0], start_date[1], start_date[2]))
            filtered_emails = filtered_emails.filter(datetime_received__gte=start)
        if end_date:
            # get YYYY/MM/DD from epoch time in milliseconds
            end_date = parse_time(end_date)

            tz = EWSTimeZone.timezone(self.default_timezone)
            end = tz.localize(EWSDateTime(end_date[0], end_date[1], end_date[2]))
            filtered_emails = filtered_emails.filter(datetime_received__lte=end)

        # Check attachments
        if has_attachments is not None:
            filtered_emails = filtered_emails.filter(has_attachments=has_attachments)

        # Order by date
        if order_by_recency is not None:
            if order_by_recency:
                filtered_emails = filtered_emails.order_by('-datetime_received')
            else:
                filtered_emails = filtered_emails.order_by('datetime_received')

        # Only get num_emails
        if num_emails:
            filtered_emails = filtered_emails[:num_emails]

        return filtered_emails

    def create_email_message(self, username, subject, body, to_recipients):
        """Create an email message object"""
        account = self.connect_to_account(username, impersonation=(username != self.email))
        email = Message(
            account=account,
            folder=account.sent,
            subject=subject,
            body=body,
            to_recipients=to_recipients.split(',')
        )
        return email

    def create_meeting(self, username, start_time, end_time, subject, body, required_attendees, optional_attendees):
        """Create a meeting object"""
        account = self.connect_to_account(username, impersonation=(username != self.email))
        tz = EWSTimeZone.timezone(self.default_timezone)
        start_time = parse_time(start_time)
        end_time = parse_time(end_time)

        if required_attendees:
            required_attendees = required_attendees.split(',')
        if optional_attendees:
            optional_attendees = optional_attendees.split(',')

        meeting = CalendarItem(
            account=account,
            folder=account.calendar,
            start=tz.localize(EWSDateTime(start_time[0], start_time[1], start_time[2], start_time[3], start_time[4])),
            end=tz.localize(EWSDateTime(end_time[0], end_time[1], end_time[2], end_time[3], end_time[4])),
            subject=subject,
            body=body,
            required_attendees=required_attendees,
            optional_attendees=optional_attendees
        )
        return meeting

    def create_email_function_results(self, emails):
        """Create function results from email query results"""
        results = {
            'email_ids': [],
            'emails': {}
        }

        # Example function results
        # results = {
        #     'email_ids': ['id1', 'idN'],
        #     'emails': {
        #         'id1': {
        #             'subject': 'Email Subject',
        #             'body': 'Subject body in HTML',
        #             'sender_name': 'FirstName LastName',
        #             'sender_email': 'example@example.com',
        #             'attachment_ids': ['attachment_id1', 'attachment_id2'],
        #             'attachments': {
        #                 'attachment_id1': {
        #                     'attachment_name': 'attachment.xslx',
        #                     'attachment_content_type': 'spreadsheet',
        #                     'attachment_size': '8842',
        #                     'attachment_base64': 'attachment encoded in base 64'
        #                 },
        #                 'attachment_id2': {
        #                     'attachment_name': '...',
        #                     'attachment_content_type': '...',
        #                     'attachment_size': '...',
        #                     'attachment_base64': 'attachment encoded in base 64'
        #                 }
        #             }
        #         },
        #         'idN': {
        #             'subject': 'Email Subject',
        #             'body': 'Subject body in HTML',
        #             'sender_name': 'FirstName LastName',
        #             'sender_email': 'example@example.com',
        #             'attachment_ids': ['attachment_id1', 'attachment_id2'],
        #             'attachments': {
        #                 'attachment_id1': {
        #                     'attachment_name': 'attachment.xslx',
        #                     'attachment_content_type': 'spreadsheet',
        #                     'attachment_size': '8842',
        #                     'attachment_base64': 'attachment encoded in base 64'
        #                 },
        #                 'attachment_id2': {
        #                     'attachment_name': '...',
        #                     'attachment_content_type': '...',
        #                     'attachment_size': '...',
        #                     'attachment_base64': 'attachment encoded in base 64'
        #                 }
        #             }
        #         }
        #     }
        # }

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
                        curr_attachment['attachment_base64'] = base64.b64encode(attachment.content)

        return results


def parse_time(epoch_time):
    """Convert epoch time in milliseconds to [year, month, day, hour, minute, second]"""
    date = time.strftime('%Y-%m-%d-%H-%M-%S', time.gmtime(epoch_time/1000))
    return [int(i) for i in date.split('-')]


def str_to_bool(str):
    """Convert a unicode string to equivalent boolean value and is case insensitive."""
    if str.lower() == 'true':
        return True
    elif str.lower() == 'false':
        return False
    else:
        raise ValueError("{} in the app.config file is not a boolean value".format(str))

def get_config_option(options, option_name):
    """If the specified option is in options, return it. If it isn't raise an error"""
    option = options.get(option_name)

    if option is None:
        err = "'{}' is mandatory and not set in the app.config file. This option must be set to run this function"
        raise ValueError(err.format(option_name))
    else:
        return option