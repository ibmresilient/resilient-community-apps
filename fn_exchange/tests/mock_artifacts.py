# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Generate Mock responses to simulate Microsoft Exchange for Unit and function tests """
import sys

from exchangelib.queryset import QuerySet
from mock import MagicMock
from exchangelib import Message, FileAttachment, Account, Folder, CalendarItem, EWSDateTime, EWSTimeZone, Q, Mailbox
from fn_exchange.util.exchange_utils import exchange_utils, FolderError

from exchangelib.folders import RootOfHierarchy

DELEGATE = 'delegate'
TEST_TZ = EWSTimeZone.timezone('Etc/GMT')
# Function opts
MOCK_OPTS = {
    'verify_cert': 'false',
    'server': 'server',
    'username': 'username',
    'email': 'email',
    'password': 'password',
    'default_folder_path': 'path',
    'default_timezone': 'Etc/GMT'
}
# Integration opts
MOCK_INT_OPTS = {}

class MockEmail(Message):
    """Mocking exchangelib Email"""
    def __init__(self, message_id, subject, body, sender, attachments, mime_content):
        self.message_id = message_id
        self.subject = subject
        self.body = body
        self.sender = sender
        self.attachments = attachments
        self.mime_content = mime_content


class MockSender(object):
    """Mocking exchangelib Sender"""
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address


class MockAttachment(FileAttachment):
    """Mocking exchangelib FileAttachment"""
    def __init__(self, attachment_id, name, content_type, size, content):
        self.attachment_id = attachment_id
        self.name = name
        self.content_type = content_type
        self.size = size
        self._content = content


class MockAttachmentId(object):
    """Mocking exchangelib AttachmentId"""
    def __init__(self, id):
        self.id = id


class MockAccount(Account):
    """Mocking exchangelib Account"""
    def __init__(self, root):
        self.root = root
        self.sent = MockFolder('sent', {}, account=self)
        self.calendar = MockFolder('calendar', {}, account=self)

    def set_root(self, root):
        self.root = root


class MockFolder(RootOfHierarchy):
    """Mocking exchangelib Folder"""
    FIELDS = []

    def __init__(self, name, subfolders, account=None):
        self.name = name
        self._subfolders = subfolders
        self.child_folder_count = len(subfolders)
        self._account = account

    def __truediv__(self, other):
        """Overloading / operator for folder navigation"""
        if self._subfolders.get(other):
            return self._subfolders[other]
        raise FolderError('mock@address.com', 'path', other, 'tree')
    __div__ = __truediv__

    def __eq__(self, other):
        return self.name == other.name and self._subfolders == other._subfolders

    def __hash__(self):
        return hash(self.name + str(set(self._subfolders)))

    def __repr__(self):
        return '{}: {}'.format(self.name, str(self._subfolders))

    # For get_emails search_subfolders list(folder.walk().get_folders())
    def get_folders(self):
        for item in self.subfolders.values():
            yield item
            for recur_item in item.subfolders.values():
                yield recur_item
def get_sender():
    sender = MagicMock(spec=Mailbox)
    sender.name = "John Doe"
    sender.email_address = "jdoe@exch.com"
    sender.routing_type = "SMTP"
    sender.mailbox_type = "Mailbox"
    return sender

def get_mime_content():

    mime_content = """Received: from exch.exch.com (2002:925:1d2d::925:1d2d) by\r\n exch.exch.com (2002:925:1d2d::925:1d2d) with Microsoft SMTP Server\r\n (TLS) id 15.0.1395.4 via Mailbox Transport; Tue,
       10 Nov 2020 11:52:21 +0000\r\nReceived: from exch.exch.com (2002:925:1d2d::925:1d2d) by\r\n exch.exch.com (2002:925:1d2d::925:1d2d) with Microsoft SMTP Server\r\n (TLS) id 15.0.1395.4; Tue,
       10 Nov 2020 11:46:35 +0000\r\nReceived: from exch.exch.com ([
        fe80::4f8:e4ed:8276:c2c7
      ]) by\r\n exch.exch.com ([
        fe80::4f8:e4ed:8276:c2c7%12
      ]) with mapi id\r\n 15.00.1395.000; Tue,
       10 Nov 2020 11:46:35 +0000\r\nFrom: \"John Doe\" <jdoe@exch.com>\r\nTo: \"User\" <user@exch.com>\r\nSubject: Example Subject\r\nThread-Topic: Example Subject\r\nThread-Index: AQHWt1Wr3ksBSsdJkUatZX7q6rcC3A==\r\nDate: Tue,
       10 Nov 2020 11:36:02 +0000\r\nMessage-ID: <ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>\r\nAccept-Language: en-US\r\nContent-Language: en-US\r\nX-MS-Exchange-Organization-AuthAs: Internal\r\nX-MS-Exchange-Organization-AuthMechanism: 04\r\nX-MS-Exchange-Organization-AuthSource: exch.exch.com\r\nX-MS-Has-Attach:\r\nX-MS-Exchange-Organization-SCL: -1\r\nX-MS-TNEF-Correlator:\r\nContent-Type: multipart\/alternative;\r\n\tboundary=\"_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\"\r\nMIME-Version: 1.0\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\r\nContent-Type: text\/plain; charset=\"us-ascii\"\r\n\r\nTest\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_\r\nContent-Type: text\/html; charset=\"us-ascii\"\r\n\r\n<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text\/html; charset=us-ascii\">\r\n<\/head>\r\n<body>\r\nTest\r\n<\/body>\r\n<\/html>\r\n\r\n--_000_ed6f175b4ef84ceaa921ba8bfdd37739exchexchcom_--\r\n"""

    return mime_content


def get_emails():
    emails = MagicMock(spec=QuerySet)
    email = MagicMock(spec=Message)
    email.message_id = "<ed6f175b4ef84ceaa921ba8bfdd37739@exch.exch.com>"
    email.subject = "Example Subject"
    email.body = "<html>\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text\/html; charset=utf-8\">\r\n<\/head>\r\n<body>\r\nExample Body\r\n<\/body>\r\n<\/html>\r\n"
    if sys.version_info.major < 3:
        email.mime_content = get_mime_content()
    else:
        email.mime_content = get_mime_content().encode('utf-8', 'ignore')
    email.sender_name = "John Doe"
    email.sender_email = "jdoe@exch.com"
    email.attachments = {}
    email.attachment_ids = []
    email.sender = get_sender()
    email.move_to_trash = MagicMock()
    emails.count = MagicMock()
    emails.count.return_value = 1
    emails.__iter__.return_value = [email]
    return emails

def create_meeting():
    meeting = MagicMock(spec=CalendarItem)
    meeting.subject = "Test"
    meeting.body = "Just a test"
    meeting.attachments = []
    meeting.start = EWSDateTime(2020, 11, 10, 14, 0, tzinfo=TEST_TZ)
    meeting.end = EWSDateTime(2020, 11, 10, 15, 0, tzinfo=TEST_TZ)
    meeting.required_attendees = ['user@exch.com']
    return meeting

def resolve_names():
    user = MagicMock(spec=Mailbox)
    user.name = "User"
    user.email_address = "user@exch.com"
    user.routing_type = "SMTP"
    user.mailbox_type = "Mailbox"
    info = [user]
    return info

def connect_to_account(username):

    account = MagicMock(spec=Account)
    if username != "empty_user@exch.com":
        account.access_type = "delegate"
        account.domain = "exch.com"
        account.Identity = ("user@exch.com", None, None, None)
        account.username = "user@exch.com"
        account.get_user = "user@exch.com"
        account.protocol = MagicMock()
        account.protocol.resolve_names = MagicMock()
        account.protocol.resolve_names.return_value = resolve_names()
    else:
        account.protocol = MagicMock()
        account.protocol.resolve_names = MagicMock()
        account.protocol.resolve_names.return_value = []
    return account

def create_email_message():
    sent_email = MagicMock(spec=Message)
    sent_email.subject="Example Subject"
    sent_email.body="<html><body>Testing</body></html>"
    sent_email.attachments=[]
    sent_email.to_recipients=["jdoe@exch.com"]
    sent_email.send_and_save = MagicMock()
    return sent_email

def  go_to_folder(folder_name):
     folder = MagicMock(spec=Message)
     folder.name = folder_name
     folder.child_folder_count = 0
     folder.all = MagicMock()
     folder.all.return_value = get_emails()
     return folder

def mocked_exchange_utils(*args):

    class MockResponse:
        """Class will be used by the mock to replace exchange_utils in circuits tests"""
        def __init__(self, *arg):
            self.utils = exchange_utils(MOCK_OPTS, {})

        def create_meeting(self, exchange_email, exchange_meeting_start_time, exchange_meeting_end_time,
                           exchange_meeting_subject, exchange_meeting_body,
                           exchange_required_attendees, exchange_optional_attendees):
            return create_meeting()

        def get_emails(self, username, folder_path=None, email_ids = None, sender=None, subject=None, body=None,
                   start_date=None, end_date=None, has_attachments=None, order_by_recency=None, num_emails=None,
                   search_subfolders=False):
            return get_emails()

        def create_email_function_results(self, emails):
            return self.utils.create_email_function_results(emails)

        def connect_to_account(self, username):
            return connect_to_account(username)

        def create_email_message(self, username, subject, body, to_recipients):
            return create_email_message()

        def go_to_folder(self, exchange_email, exchange_destination_folder_path) :
             return go_to_folder(exchange_destination_folder_path)

    return MockResponse(*args)


def get_mock_config(email="email@example.com"):
    config_data = u"""[fn_exchange]
verify_cert=False
server=example.com
username=domain\\username
email={}
password=password
default_folder_path=Top of Information Store/Inbox
# Uncomment to specify proxy settings
#https_proxy=https://your.proxy.com
#http_proxy=http://your.proxy.com
""".format(email)
    return config_data
