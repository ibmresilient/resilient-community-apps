
import pytest
from exchangelib import Account, Folder, FolderCollection, EWSTimeZone
from exchangelib.folders import Root
from exchangelib.restriction import Q

from fn_exchange.lib.exchange_utils import exchange_interface
from fn_exchange.lib.exchange_helper import (
    FolderError, parse_time, go_to_folder, get_proxy_adapter, get_timezone)

from mock_artifacts import (
    MOCK_INT_OPTS, MOCK_OPTS, MockAccount, return_none,
    MockAttachment, MockAttachmentId, MockEmail,
    MockFolder, MockSender, connect_to_account, send_emails, calendar_item)

try:
    from unittest.mock import patch
except ImportError:
    from mock import MagicMock, patch


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
        test_utils = exchange_interface(MOCK_OPTS, MOCK_INT_OPTS)

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

    @patch("fn_exchange.lib.exchange_utils.exchange_interface.connect_to_account")
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
        account = MockAccount(test_root)
        account.root.refresh = return_none
        

        # Check when go to folder that doesn't exist appropriate error is raised
        with pytest.raises(FolderError):
            go_to_folder('mockemail', account, '3')

        # First level navigatino check - root/1
        test1 = go_to_folder('mockemail', account, '1')
        assert test1 == test_root._subfolders['1']

        # Two level navigation check - root/1/1_1
        with pytest.raises(FolderError):
            go_to_folder('mockemail', account, '1/1_1')

        # First level navigation check - root/2
        test2 = go_to_folder('mockemail', account, '2')
        assert test2 == test_root._subfolders['2']

        # Two level navigation check - root/2/2_1
        test2_1 = go_to_folder('mockemail', account, '2/2_1')
        assert test2_1 == test_root._subfolders['2']._subfolders['2_1']

        # Two level navigation check - root/2/2_2
        test2_2 = go_to_folder('mockemail', account, '2/2_2')
        assert test2_2 == test_root._subfolders['2']._subfolders['2_2']

        # Three level navigation check - root/2/2_2/2_2_1
        test2_2_1 = go_to_folder('mockemail', account, '2/2_2/2_2_1')
        assert test2_2_1 == test_root._subfolders['2']._subfolders['2_2']._subfolders['2_2_1']


    @patch("fn_exchange.lib.exchange_utils.exchange_interface.connect_to_account")
    @patch('fn_exchange.lib.exchange_utils.Message', side_effect=send_emails)
    def test_create_email_message(self, connect_to_account, send_emails):
        """Testing create_email_message"""

        function_parameters = {}
        test_utils = exchange_interface(MOCK_OPTS, {"email":"user1@a.com"})
        mock_account = MockAccount(MockFolder('root', {}))
        connect_to_account.return_value = mock_account

        # Input parameters
        function_parameters["username"] = "user1@a.com"
        function_parameters["msg_subject"] = 'subject1'
        function_parameters["msg_body"] = 'body1'
        function_parameters["recipients"] = 'a@a.com'

        # Check returned object has correct parameters
        email1 = test_utils.create_email_message(function_parameters)
        expected_results = {
            'recipients' : function_parameters["recipients"],
            'sender'     : function_parameters["username"],
            'msg_subject': function_parameters["msg_subject"],
            'msg_body'   : function_parameters["msg_body"]}
        assert email1 == expected_results

        # More input parameters
        function_parameters["recipients"] = 'a@a.com,b@a.com'

        # Check input parameters correctly assign None
        email2 = test_utils.create_email_message(function_parameters)
        expected_results = {
            'recipients' : function_parameters["recipients"],
            'sender'     : function_parameters["username"],
            'msg_subject': function_parameters["msg_subject"],
            'msg_body'   : function_parameters["msg_body"]}
        assert email2 == expected_results

    @patch("fn_exchange.lib.exchange_utils.exchange_interface.connect_to_account", side_effect=connect_to_account)
    @patch("fn_exchange.lib.exchange_utils.CalendarItem", side_effect=calendar_item)
    def test_create_meeting(self, connect_to_account, calendar_item):
        """Testing create meeting"""
        test_utils = exchange_interface(MOCK_OPTS, {"email":"mockemail"})

        function_parameters = {}
        function_parameters["username"] = "empty_user@exch.com"
        function_parameters["start_time"] = 1000000
        function_parameters["end_time"] = 1100000
        function_parameters["meeting_subject"] = "subject1"
        function_parameters["meeting_body"] = "body1"
        function_parameters["required_attendees"] = 'r1@example.com,r2@example.com'
        function_parameters["optional_attendees"] = None

        # Check parameters and that optional_attendees handles None properly
        meeting1 = test_utils.create_meeting(function_parameters)
        assert meeting1.get("sender") == "empty_user@exch.com"
        assert meeting1.get("subject") == 'subject1'
        assert meeting1.get("body") == 'body1'
        assert meeting1.get("required_attendees") == ['r1@example.com', 'r2@example.com']
        assert meeting1.get("optional_attendees") == None

        # Check parameters and that required_attendees handles None properly

        function_parameters["required_attendees"] = None
        function_parameters["optional_attendees"] = 'o1@a.com,o2@a.com'
        meeting2 = test_utils.create_meeting(function_parameters)
        assert meeting2.get("sender") == "empty_user@exch.com"
        assert meeting2.get("subject") == 'subject1'
        assert meeting2.get("body") == 'body1'
        assert meeting2.get("required_attendees") == None
        assert meeting2.get("optional_attendees") == ['o1@a.com', 'o2@a.com']

        # General use test
        function_parameters["required_attendees"] = 'r1@example.com,r2@example.com'
        function_parameters["optional_attendees"] = 'o1@a.com,o2@a.com'
        meeting3 = test_utils.create_meeting(function_parameters)
        assert meeting3.get("sender") == "empty_user@exch.com"
        assert meeting3.get("subject") == 'subject1'
        assert meeting3.get("body") == 'body1'
        assert meeting3.get("required_attendees") == ['r1@example.com', 'r2@example.com']
        assert meeting3.get("optional_attendees") == ['o1@a.com', 'o2@a.com']

    @patch.object(FolderCollection, '__eq__', lambda fc1, fc2: set(fc1) == set(fc2))
    @patch("fn_exchange.lib.exchange_utils.exchange_interface.connect_to_account")
    def test_get_email(self, connect_to_account):
        """Testing get_email"""

        # Initialize testing variables with Mock objects
        # Mocked account and mocked root with subfolders
        opts = MOCK_OPTS
        opts['default_folder_path'] = '1'
        test_utils = exchange_interface(None, opts)
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
        rsf = test_root._subfolders
        mock_account.set_root(test_root)
        mock_account.root.refresh = return_none
        connect_to_account.return_value = mock_account

        # Sender filter check
        emails1 = test_utils.get_emails({"username":'mockemail', "sender" :'testsender'})
        assert emails1.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails1.q == Q(sender='testsender')

        # Multiple folder check with sender
        emails2 = test_utils.get_emails({"username":'mockemail', "src_folder":'1,2', "sender":'another sender'})
        assert emails2.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1'], rsf['2']])
        assert emails2.q == Q(sender='another sender')

        # Subject filter check
        emails3 = test_utils.get_emails({"username":'mockemail', "msg_subject" :'testsender'})
        assert emails3.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails3.q == Q(subject__contains='testsender')

        # Body filter check
        emails4 = test_utils.get_emails({"username":'mockemail', "msg_body" :'testbody'})
        assert emails4.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails4.q == Q(body__contains='testbody')

        # Email id filter check
        emails5 = test_utils.get_emails({"username":'mockemail', "email_ids":'id1,id2,idN'})
        assert emails5.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails5.q == Q(message_id='id1') | Q(message_id='id2') | Q(message_id='idN')

        # has_attachments filter check
        emails6 = test_utils.get_emails({"username":'mockemail', "has_attachments":True})
        assert emails6.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails6.q == Q(has_attachments= True)

        # search_subfolders filter check
        with patch.object(Folder, 'walk') as walk:
            walk.return_value = test_root._subfolders['2']
            emails7 = test_utils.get_emails({"username":'mockemail', "src_folder":'2', "search_subfolders":True})

        fc_expected = FolderCollection(folders=[rsf['2']], account=mock_account)
        assert emails7.folder_collection.folders == fc_expected.folders
        assert emails7.folder_collection.account == fc_expected.account
        assert emails7.q == Q()

        emails8 = test_utils.get_emails({"username":'mockemail', "src_folder":'1', "sender":'sender',
                                         "msg_subject":'subject', "msg_body":'body', "has_attachments":False})
        assert emails8.folder_collection == FolderCollection(account=mock_account, folders=[rsf['1']])
        assert emails8.q == Q(sender='sender') & Q(subject__contains='subject') \
               & Q(body__contains='body') & Q(has_attachments=False)

    def test_get_tz(self):
        tz = get_timezone()
        assert isinstance(tz, EWSTimeZone)
