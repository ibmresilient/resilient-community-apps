# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
"""Generate Mock responses to simulate Microsoft Exchange for Unit and function tests """
from exchangelib import Message, FileAttachment, Account, Folder

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
