from exchangelib import Credentials, Account, DELEGATE, Configuration, EWSDateTime, EWSTimeZone, Message
from exchangelib.folders import FolderCollection
from exchangelib.attachments import FileAttachment
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter
import time, base64

class exchange_utils:
    def __init__(self, opts):
        self.verify_cert = opts.get('verify_cert') == "True"
        self.server = opts.get('server')
        self.username = opts.get('username')
        self.email = opts.get('email')
        self.password = opts.get('password')
        self.default_folder_path = opts.get('default_folder_path')
        self.default_timezone = opts.get('default_timezone')

    def connect_to_account(self, primary_smtp_address):
        """Connect to specified account and return it"""

        # Don't check certificates
        if not self.verify_cert:
            BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

        # Use credentials to get account
        credentials = Credentials(username=self.username, password=self.password)
        config = Configuration(server=self.server, credentials=credentials)
        account = Account(primary_smtp_address=primary_smtp_address, config=config,
                          autodiscover=self.verify_cert, access_type=DELEGATE)
        return account

    def go_to_folder(self, username, folder_path):
        """Navigate to specified folder path and return it"""

        account = self.connect_to_account(username)
        folder = account.root
        if folder_path is None:
            return folder
        for dir in folder_path.split('/'):
            folder = folder / dir
        return folder

    def get_emails(self, username, folder_path=None, sender=None, subject=None, body=None, start_date=None,
                   end_date=None, has_attachments=None, order_by_recency=None, num_emails=None,
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
            start_date = str(time.strftime('%Y-%m-%d', time.gmtime(start_date/1000.0)))
            start_date = [int(i) for i in start_date.split('-')]

            tz = EWSTimeZone.timezone(self.default_timezone)
            start = tz.localize(EWSDateTime(start_date[0], start_date[1], start_date[2]))
            filtered_emails = filtered_emails.filter(datetime_received__gte=start)
        if end_date:
            # get YYYY/MM/DD from epoch time in milliseconds
            end_date = str(time.strftime('%Y-%m-%d', time.gmtime(end_date/1000.0)))
            end_date = [int(i) for i in end_date.split('-')]

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