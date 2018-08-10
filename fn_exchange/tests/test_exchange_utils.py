# import unittest
import pytest
from exchangelib import Message, FileAttachment
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


class MockSender():
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


class MockAttachmentId:
    def __init__(self, id):
        self.id = id


class MockAccount():
    def __init__(self, root):
        self.root = root


class MockFolder():
    def __init__(self, name, subfolders):
        self.name = name
        self.subfolders = subfolders

    def __truediv__(self, subfolder):
        if self.subfolders[subfolder]:
            return self.subfolders[subfolder]
        raise FolderError('mock@address.com', 'path', subfolder, 'tree')


class TestExchangeUtils:

    # def test_parse_time(self):
    #     time1 = parse_time(1533841231000)
    #     result_time1 = [2018, 8, 9, 19, 0, 31]
    #     self.assertEquals(time1, result_time1)
    #
    #     time2 = parse_time(852076800000)
    #     result_time2 = [1997, 1, 1, 0, 0, 0]
    #     self.assertEquals(time2, result_time2)
    #
    #     time3 = parse_time(883267199999)
    #     result_time3 = [1997, 12, 27, 23, 59, 59]
    #     self.assertEquals(time3, result_time3)
    #
    #     time4 = parse_time(883267200000)
    #     result_time4 = [1997, 12, 28, 0, 0, 0]
    #     self.assertEquals(time4, result_time4)
    #
    # def test_create_email_function_results(self):
    #     test_utils = exchange_utils({})
    #
    #     emails1 = test_utils.create_email_function_results([])
    #     emails1_results = {
    #         'email_ids': [],
    #         'emails': {}
    #     }
    #     self.assertEquals(emails1, emails1_results)
    #
    #     emails2 = [MockEmail('1', 'Subject 1', 'Body', MockSender('Sen Der1', 'sender1@example.com'), [])]
    #     emails2_output = test_utils.create_email_function_results(emails2)
    #     emails2_results = {
    #         'email_ids': ['1'],
    #         'emails': {
    #             '1': {
    #                 'subject': 'Subject 1',
    #                 'body': 'Body',
    #                 'sender_name': 'Sen Der1',
    #                 'sender_email': 'sender1@example.com',
    #                 'attachment_ids': [],
    #                 'attachments': {}
    #             }
    #         }
    #     }
    #     self.assertEquals(emails2_output, emails2_results)
    #
    #     emails3 = emails2 + [MockEmail('weio', 'nzxcv', 'vds', MockSender('FIRST LAST', 'firstlast@example.com'),
    #                                    [MockAttachment(MockAttachmentId('22'), 'ATTCH', 'spreadsheet', 12, 'encode me')])]
    #     emails3_output = test_utils.create_email_function_results(emails3)
    #     emails3_results = {
    #         'email_ids': ['1', 'weio'],
    #         'emails': {
    #             '1': {
    #                 'subject': 'Subject 1',
    #                 'body': 'Body',
    #                 'sender_name': 'Sen Der1',
    #                 'sender_email': 'sender1@example.com',
    #                 'attachment_ids': [],
    #                 'attachments': {}
    #             },
    #             'weio': {
    #                 'subject': 'nzxcv',
    #                 'body': 'vds',
    #                 'sender_name': 'FIRST LAST',
    #                 'sender_email': 'firstlast@example.com',
    #                 'attachment_ids': ['22'],
    #                 'attachments': {
    #                     '22': {
    #                         'attachment_name': 'ATTCH',
    #                         'attachment_content_type': 'spreadsheet',
    #                         'attachment_size': 12,
    #                         'attachment_base64': 'ZW5jb2RlIG1l'
    #                     }
    #                 }
    #             }
    #         }
    #     }
    #     self.assertEquals(emails3_output, emails3_results)
    #
    #     emails4 = emails3 + [2, 'not an email', True]
    #     emails4_output = test_utils.create_email_function_results(emails4)
    #     self.assertEquals(emails4_output, emails3_results)

    @patch("fn_exchange.util.exchange_utils.exchange_utils.connect_to_account")
    def test_go_to_folder(self, connect_to_account):
        test_root = MockFolder('root', {
            '1': MockFolder('1', {}),
            '2': MockFolder('2', {
                '2_1': MockFolder('2_1', {}),
                '2_2': MockFolder('2_2', {
                    '2_2_1', MockFolder('2_2_1', {})
                })
            })
        })
        connect_to_account.return_value = MockAccount(test_root)
        test_utils = exchange_utils({})

        test1 = test_utils.go_to_folder('mockemail', '1')
        assert test1 == test_root / '1'
