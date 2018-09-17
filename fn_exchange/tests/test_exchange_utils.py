# import unittest
import pytest
from exchangelib import Message, FileAttachment, Account, Folder, FolderCollection
from exchangelib.restriction import Q
from fn_exchange.util.exchange_utils import exchange_utils, parse_time, FolderError, get_config_option, str_to_bool

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

MOCK_OPTS = {
    'verify_cert': 'false',
    'server': 'server',
    'username': 'username',
    'email': 'email',
    'password': 'password',
    'default_folder_path': 'path',
    'default_timezone': 'Etc/GMT'
}

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
        self.content = content


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


class MockFolder(Folder):
    """Mocking exchangelib Folder"""
    FIELDS = []

    def __init__(self, name, subfolders, account=None):
        self.name = name
        self.subfolders = subfolders
        self.child_folder_count = len(subfolders)
        self.account = account

    def __truediv__(self, other):
        """Overloading / operator for folder navigation"""
        if self.subfolders.get(other):
            return self.subfolders[other]
        raise FolderError('mock@address.com', 'path', other, 'tree')
    __div__ = __truediv__

    def __eq__(self, other):
        return self.name == other.name and self.subfolders == other.subfolders

    def __hash__(self):
        return hash(self.name + str(set(self.subfolders)))

    def __repr__(self):
        return '{}: {}'.format(self.name, str(self.subfolders))

    # For get_emails search_subfolders list(folder.walk().get_folders())
    def get_folders(self):
        for item in self.subfolders.values():
            yield item
            for recur_item in item.subfolders.values():
                yield recur_item


class TestExchangeUtils:

    def test_parse_time(self):
        """Testing parse_time"""

        # General case test
        time1 = parse_time(1533841231000)
        result_time1 = [2018, 8, 9, 19, 0, 31]
        assert time1 == result_time1

        # Edge case tests
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
        """Testing create_email_function_results"""
        test_utils = exchange_utils(MOCK_OPTS)

        # Test when no results are returned
        emails1 = test_utils.create_email_function_results([])
        emails1_results = {
            'email_ids': [],
            'emails': {}
        }
        assert emails1 == emails1_results

        # Test one email with no attachments
        emails2 = [MockEmail('1', 'Subject 1', 'Body', MockSender('Sen Der1', 'sender1@example.com'), [], b'abc')]
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
                    'attachments': {},
                    'mime_content': 'abc'
                }
            }
        }
        assert emails2_output == emails2_results

        # Test two emails, one with attachments and one without
        emails3 = emails2 + [MockEmail('weio', 'nzxcv', 'vds', MockSender('FIRST LAST', 'firstlast@example.com'),
                                       [MockAttachment(MockAttachmentId('22'), 'ATTCH', 'spreadsheet', 12,
                                                       str.encode('encode me'))], b'def')]
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
                    'attachments': {},
                    'mime_content': 'abc'
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
                    },
                    'mime_content': 'def'
                }
            }
        }
        assert emails3_output == emails3_results

        # Test that function results only include email items
        emails4 = emails3 + [2, 'not an email', True]
        emails4_output = test_utils.create_email_function_results(emails4)
        assert emails4_output == emails3_results

    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_go_to_folder(self, connect_to_account):
        """Testing go_to_folder"""

        # Create a mock account and mock root folder with subfolders:
        # root - 1
        #      - 2 - 2_1, 2_2
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
        test_utils = exchange_utils(MOCK_OPTS)

        # Check when go to folder that doesn't exist appropriate error is raised
        with pytest.raises(FolderError):
            test_utils.go_to_folder('mockemail', '3')

        # First level navigatino check - root/1
        test1 = test_utils.go_to_folder('mockemail', '1')
        assert test1 == test_root.subfolders['1']

        # Two level navigation check - root/1/1_1
        with pytest.raises(FolderError):
            test_utils.go_to_folder('mockemail', '1/1_1')

        # First level navigation check - root/2
        test2 = test_utils.go_to_folder('mockemail', '2')
        assert test2 == test_root.subfolders['2']

        # Two level navigation check - root/2/2_1
        test2_1 = test_utils.go_to_folder('mockemail', '2/2_1')
        assert test2_1 == test_root.subfolders['2'].subfolders['2_1']

        # Two level navigation check - root/2/2_2
        test2_2 = test_utils.go_to_folder('mockemail', '2/2_2')
        assert test2_2 == test_root.subfolders['2'].subfolders['2_2']

        # Three level navigation check - root/2/2_2/2_2_1
        test2_2_1 = test_utils.go_to_folder('mockemail', '2/2_2/2_2_1')
        assert test2_2_1 == test_root.subfolders['2'].subfolders['2_2'].subfolders['2_2_1']


    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_create_email_message(self, connect_to_account):
        """Testing create_email_message"""

        test_utils = exchange_utils(MOCK_OPTS)
        mock_account = MockAccount(MockFolder('root', {}))
        connect_to_account.return_value = mock_account

        # Input parameters
        test_account1 = mock_account
        test_subject1 = 'subject1'
        test_body1 = 'body1'
        test_to_recipients1 = 'a@a.com'

        # Check returned object has correct parameters
        email1 = test_utils.create_email_message(test_account1, test_subject1, test_body1, test_to_recipients1)
        assert email1.account == mock_account
        assert email1.folder == mock_account.sent
        assert email1.subject == 'subject1'
        assert email1.body == 'body1'
        assert email1.to_recipients == ['a@a.com']

        # More input parameters
        test_account2 = mock_account
        test_subject2 = None
        test_body2 = None
        test_to_recipients2 = 'a@a.com,b@a.com'

        # Check input parameters correctly assign None
        email2 = test_utils.create_email_message(test_account2, test_subject2, test_body2, test_to_recipients2)
        assert email2.account == mock_account
        assert email2.folder == mock_account.sent
        assert email2.subject == None
        assert email2.body == None
        assert email2.to_recipients == ['a@a.com', 'b@a.com']

    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_create_meeting(self, connect_to_account):
        """Testing create meeting"""
        test_utils = exchange_utils(MOCK_OPTS)
        mock_account = MockAccount(MockFolder('root', {}))
        connect_to_account.return_value = mock_account

        # Check parameters and that optional_attendees handles None properly
        meeting1 = test_utils.create_meeting('mockemail', 1000000, 1100000, 'subject1', 'body1',
                                             'r1@example.com,r2@example.com', None)
        assert meeting1.account == mock_account
        assert meeting1.folder == mock_account.calendar
        assert meeting1.subject == 'subject1'
        assert meeting1.body == 'body1'
        assert meeting1.required_attendees == ['r1@example.com', 'r2@example.com']
        assert meeting1.optional_attendees == None

        # Check parameters and that required_attendees handles None properly
        meeting2 = test_utils.create_meeting('mockemail', 1000000, 1100000, 'qwer', 'tuio',
                                             None, 'o1@a.com,o2@a.com')
        assert meeting2.account == mock_account
        assert meeting2.folder == mock_account.calendar
        assert meeting2.subject == 'qwer'
        assert meeting2.body == 'tuio'
        assert meeting2.required_attendees == None
        assert meeting2.optional_attendees == ['o1@a.com', 'o2@a.com']

        # General use test
        meeting3 = test_utils.create_meeting('mockemail', 1000000, 1100000, None, None,
                                             'r1@example.com,r2@example.com', 'o1@a.com,o2@a.com')
        assert meeting3.account == mock_account
        assert meeting3.folder == mock_account.calendar
        assert meeting3.subject == None
        assert meeting3.body == None
        assert meeting3.required_attendees == ['r1@example.com', 'r2@example.com']
        assert meeting3.optional_attendees == ['o1@a.com', 'o2@a.com']

    @patch.object(FolderCollection, '__eq__', lambda fc1, fc2: set(fc1) == set(fc2))
    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_get_email(self, connect_to_account):
        """Testing get_email"""

        # Initialize testing variables with Mock objects
        # Mocked account and mocked root with subfolders
        opts = MOCK_OPTS
        opts['default_folder_path'] = '1'
        test_utils = exchange_utils(opts)
        mock_account = MockAccount(None)
        test_root = MockFolder('root', {
            '1': MockFolder('1', {}, mock_account),
            '2': MockFolder('2', {
                '2_1': MockFolder('2_1', {}, mock_account),
                '2_2': MockFolder('2_2', {
                    '2_2_1': MockFolder('2_2_1', {}, mock_account)
                }, mock_account)
            }, mock_account)
        }, mock_account)
        rsf = test_root.subfolders
        mock_account.set_root(test_root)
        connect_to_account.return_value = mock_account

        # Sender filter check
        emails1 = test_utils.get_emails('mockemail', sender='testsender')
        assert emails1.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails1.q == Q(sender='testsender')

        # Multiple folder check with sender
        emails2 = test_utils.get_emails('mockemail', folder_path='1,2', sender='another sender')
        assert emails2.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1'], rsf['2']])
        assert emails2.q == Q(sender='another sender')

        # Subject filter check
        emails3 = test_utils.get_emails('mockemail', subject='subject')
        assert emails3.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails3.q == Q(subject__contains='subject')

        # Body filter check
        emails4 = test_utils.get_emails('mockemail', body='body')
        assert emails4.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails4.q == Q(body__contains='body')

        # Email id filter check
        emails5 = test_utils.get_emails('mockemail', email_ids='id1,id2,idN')
        assert emails5.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails5.q == Q(message_id='id1') | Q(message_id='id2') | Q(message_id='idN')

        # has_attachments filter check
        emails6 = test_utils.get_emails('mockemail', has_attachments=True)
        assert emails6.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails6.q == Q(has_attachments= True)

        # search_subfolders filter check
        with patch.object(Folder, 'walk') as walk:
            walk.return_value = test_root.subfolders['2']
            emails7 = test_utils.get_emails('mockemail', folder_path='2', search_subfolders=True)
        assert emails7.folder_collection == FolderCollection(folders=[rsf['2'], rsf['2'].subfolders['2_1'],
                                                                      rsf['2'].subfolders['2_2'].subfolders['2_2_1'],
                                                                      rsf['2'].subfolders['2_2']], account=mock_account)
        assert emails7.q == Q()

        emails8 = test_utils.get_emails('mockemail', folder_path='1', sender='sender', subject='subject', body='body',
                                        has_attachments=False)
        assert emails8.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        print(emails8.q)
        print(Q(sender='sender', subject__contains='subject', body__contains='body', has_attachments=False))
        assert emails8.q == Q(sender='sender') & Q(subject__contains='subject') \
               & Q(body__contains='body') & Q(has_attachments=False)

    def test_str_to_bool(self):
        """Testing str_to_bool"""

        # Test true values
        assert str_to_bool('tRUe') == True
        assert str_to_bool('TRUE') == True
        assert str_to_bool('true') == True
        assert str_to_bool('True') == True

        # Test false values
        assert str_to_bool('FAlse') == False
        assert str_to_bool('false') == False
        assert str_to_bool('FALSE') == False
        assert str_to_bool('False') == False

        # Test errors
        with pytest.raises(ValueError):
            str_to_bool('error')
        with pytest.raises(ValueError):
            str_to_bool('Fakse')
        with pytest.raises(ValueError):
            str_to_bool('true ')
        with pytest.raises(ValueError):
            str_to_bool(' true')

    def test_get_config_option(self):
        """Test get_config_options"""

        assert get_config_option(MOCK_OPTS, 'verify_cert') == 'false'
        assert get_config_option(MOCK_OPTS, 'server') == 'server'
        assert get_config_option(MOCK_OPTS, 'default_timezone') == 'Etc/GMT'
        with pytest.raises(ValueError):
            get_config_option(MOCK_OPTS, 'option')