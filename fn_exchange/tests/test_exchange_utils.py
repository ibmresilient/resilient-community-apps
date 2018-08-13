# import unittest
import pytest
from exchangelib import Message, FileAttachment, Account, Folder
from fn_exchange.util.exchange_utils import exchange_utils, parse_time, FolderError

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

class MockEmail(Message):
    def __init__(self, message_id, subject, body, sender, attachments):
        self.message_id = message_id
        self.subject = subject
        self.body = body
        self.sender = sender
        self.attachments = attachments


class MockSender(object):
    def __init__(self, name, email_address):
        self.name = name
        self.email_address = email_address


class MockAttachment(FileAttachment):
    def __init__(self, attachment_id, name, content_type, size, content):
        self.attachment_id = attachment_id
        self.name = name
        self.content_type = content_type
        self.size = size
        self.content = content


class MockAttachmentId(object):
    def __init__(self, id):
        self.id = id


class MockAccount(Account):
    def __init__(self, root):
        self.root = root
        self.sent = MockFolder('sent', {})
        self.calendar = MockFolder('calendar', {})


class MockFolder(Folder):
    def __init__(self, name, subfolders):
        self.name = name
        self.subfolders = subfolders
        self.account = None

    def __truediv__(self, other):
        if self.subfolders.get(other):
            return self.subfolders[other]
        raise FolderError('mock@address.com', 'path', other, 'tree')
    __div__ = __truediv__

    def __eq__(self, other):
        return self.name == other.name and self.subfolders == other.subfolders


class TestExchangeUtils:

    def test_parse_time(self):
        time1 = parse_time(1533841231000)
        result_time1 = [2018, 8, 9, 19, 0, 31]
        assert time1 == result_time1

        time2 = parse_time(852076800000)
        result_time2 = [1997, 1, 1, 0, 0, 0]
        assert time2 == result_time2

        time3 = parse_time(883267199999)
        result_time3 = [1997, 12, 27, 23, 59, 59]
        assert time3 == result_time3

        time4 = parse_time(883267200000)
        result_time4 = [1997, 12, 28, 0, 0, 0]
        assert time4 == result_time4

    def test_create_email_function_results(self):
        test_utils = exchange_utils({})

        emails1 = test_utils.create_email_function_results([])
        emails1_results = {
            'email_ids': [],
            'emails': {}
        }
        assert emails1 == emails1_results

        emails2 = [MockEmail('1', 'Subject 1', 'Body', MockSender('Sen Der1', 'sender1@example.com'), [])]
        emails2_output = test_utils.create_email_function_results(emails2)
        emails2_results = {
            'email_ids': ['1'],
            'emails': {
                '1': {
                    'subject': 'Subject 1',
                    'body': 'Body',
                    'sender_name': 'Sen Der1',
                    'sender_email': 'sender1@example.com',
                    'attachment_ids': [],
                    'attachments': {}
                }
            }
        }
        assert emails2_output == emails2_results

        emails3 = emails2 + [MockEmail('weio', 'nzxcv', 'vds', MockSender('FIRST LAST', 'firstlast@example.com'),
                                       [MockAttachment(MockAttachmentId('22'), 'ATTCH', 'spreadsheet', 12, 'encode me')])]
        emails3_output = test_utils.create_email_function_results(emails3)
        emails3_results = {
            'email_ids': ['1', 'weio'],
            'emails': {
                '1': {
                    'subject': 'Subject 1',
                    'body': 'Body',
                    'sender_name': 'Sen Der1',
                    'sender_email': 'sender1@example.com',
                    'attachment_ids': [],
                    'attachments': {}
                },
                'weio': {
                    'subject': 'nzxcv',
                    'body': 'vds',
                    'sender_name': 'FIRST LAST',
                    'sender_email': 'firstlast@example.com',
                    'attachment_ids': ['22'],
                    'attachments': {
                        '22': {
                            'attachment_name': 'ATTCH',
                            'attachment_content_type': 'spreadsheet',
                            'attachment_size': 12,
                            'attachment_base64': 'ZW5jb2RlIG1l'
                        }
                    }
                }
            }
        }
        assert emails3_output == emails3_results

        emails4 = emails3 + [2, 'not an email', True]
        emails4_output = test_utils.create_email_function_results(emails4)
        assert emails4_output == emails3_results

    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_go_to_folder(self, connect_to_account):
        test_root = MockFolder('root', {
            '1': MockFolder('1', {}),
            '2': MockFolder('2', {
                '2_1': MockFolder('2_1', {}),
                '2_2': MockFolder('2_2', {
                    '2_2_1': MockFolder('2_2_1', {})
                })
            })
        })
        connect_to_account.return_value = MockAccount(test_root)
        test_utils = exchange_utils({})

        with pytest.raises(FolderError):
            test_utils.go_to_folder('mockemail', '3')

        test1 = test_utils.go_to_folder('mockemail', '1')
        assert test1 == test_root.subfolders['1']

        with pytest.raises(FolderError):
            test_utils.go_to_folder('mockemail', '1/1_1')

        test2 = test_utils.go_to_folder('mockemail', '2')
        assert test2 == test_root.subfolders['2']

        test2_1 = test_utils.go_to_folder('mockemail', '2/2_1')
        assert test2_1 == test_root.subfolders['2'].subfolders['2_1']

        test2_2 = test_utils.go_to_folder('mockemail', '2/2_2')
        assert test2_2 == test_root.subfolders['2'].subfolders['2_2']

        test2_2_1 = test_utils.go_to_folder('mockemail', '2/2_2/2_2_1')
        assert test2_2_1 == test_root.subfolders['2'].subfolders['2_2'].subfolders['2_2_1']


    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_create_email_message(self, connect_to_account):
        test_utils = exchange_utils({})
        mock_account = MockAccount(MockFolder('root', {}))
        connect_to_account.return_value = mock_account

        test_account1 = mock_account
        test_subject1 = 'subject1'
        test_body1 = 'body1'
        test_to_recipients1 = 'a@a.com'

        email1 = test_utils.create_email_message(test_account1, test_subject1, test_body1, test_to_recipients1)
        assert email1.account == mock_account
        assert email1.folder == mock_account.sent
        assert email1.subject == 'subject1'
        assert email1.body == 'body1'
        assert email1.to_recipients == ['a@a.com']

        test_account2 = mock_account
        test_subject2 = None
        test_body2 = None
        test_to_recipients2 = 'a@a.com,b@a.com'

        email2 = test_utils.create_email_message(test_account2, test_subject2, test_body2, test_to_recipients2)
        assert email2.account == mock_account
        assert email2.folder == mock_account.sent
        assert email2.subject == None
        assert email2.body == None
        assert email2.to_recipients == ['a@a.com', 'b@a.com']

    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_create_meeting(self, connect_to_account):
        test_utils = exchange_utils({'default_timezone': 'America/New_York'})
        mock_account = MockAccount(MockFolder('root', {}))
        connect_to_account.return_value = mock_account

        meeting1 = test_utils.create_meeting('mockemail', 1000000, 1100000, 'subject1', 'body1',
                                             'r1@example.com,r2@example.com', None)
        assert meeting1.account == mock_account
        assert meeting1.folder == mock_account.calendar
        assert meeting1.subject == 'subject1'
        assert meeting1.body == 'body1'
        assert meeting1.required_attendees == ['r1@example.com', 'r2@example.com']
        assert meeting1.optional_attendees == None

        meeting2 = test_utils.create_meeting('mockemail', 1000000, 1100000, 'qwer', 'tuio',
                                             None, 'o1@a.com,o2@a.com')
        assert meeting2.account == mock_account
        assert meeting2.folder == mock_account.calendar
        assert meeting2.subject == 'qwer'
        assert meeting2.body == 'tuio'
        assert meeting2.required_attendees == None
        assert meeting2.optional_attendees == ['o1@a.com', 'o2@a.com']

        meeting3 = test_utils.create_meeting('mockemail', 1000000, 1100000, None, None,
                                             'r1@example.com,r2@example.com', 'o1@a.com,o2@a.com')
        assert meeting3.account == mock_account
        assert meeting3.folder == mock_account.calendar
        assert meeting3.subject == None
        assert meeting3.body == None
        assert meeting3.required_attendees == ['r1@example.com', 'r2@example.com']
        assert meeting3.optional_attendees == ['o1@a.com', 'o2@a.com']
