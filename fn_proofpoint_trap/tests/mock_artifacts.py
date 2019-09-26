# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Generate Mock responses to simulate Proofpoint TRAP for Unit and function tests """
import re
import json
from sys import version_info
from requests import HTTPError
from requests.models import Response

# Responses for standalone tests


def get_list_members():

    response =  [{'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'IP to block', 'enabled': True,
                  'expiration': '2018-12-18T19:08:56Z', 'hash_reputation_id': 123,
                  'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '75.76.13.144', 'id': 20, 'resolution_state': 4, 'ttl': 0,
                           'updated_at': '2017-01-11T03:47:15Z'}, 'host_id': 20, 'id': 8, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2017-01-11T03:47:15Z', 'user_id': None},
                 {'created_at': '2018-01-11T03:43:54Z', 'deleted': False, 'description': 'Hostname to block', 'enabled': True,
                  'expiration': "2018-12-19T19:08:56Z", 'hash_reputation_id': None,
                  'host': {'created_at': '2017-12-29T04:56:13Z', 'host': 'tapdemo.evilscheme.info', 'id': 6, 'resolution_state': 4,
                           'ttl': 0,
                           'updated_at': '2018-01-13T00:45:16Z'}, 'host_id': 6, 'id': 7, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2018-01-11T03:43:54Z', 'user_id': None},
                 {'created_at': '2017-01-11T03:43:54Z', 'deleted': False, 'description': 'test', 'enabled': True,
                  'expiration': '2018-12-20T19:08:56Z', 'hash_reputation_id': None,
                  'host': {'created_at': '2016-12-29T04:56:13Z', 'host': 'string', 'id': 6, 'resolution_state': 4, 'ttl': 0,
                           'updated_at': '2017-01-13T00:45:16Z'}, 'host_id': 6, 'id': 6, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2017-01-11T03:43:54Z', 'user_id': None},
                 {'created_at': '2017-01-11T03:43:54Z', 'deleted': False, 'description': 'Unicode test ɡɢɣɤɥɦ', 'enabled': True,
                  'expiration': "2018-12-22T19:08:56Z", 'hash_reputation_id': None,
                  'host': {'created_at': '2016-12-29T04:56:13Z', 'host': 'ɡɢɣɤɥɦ', 'id': 6, 'resolution_state': 4, 'ttl': 0,
                           'updated_at': '2017-01-13T00:45:16Z'}, 'host_id': 6, 'id': 6, 'list_id': 1, 'response_id': None,
                  'reverse_user_id': None, 'updated_at': '2017-01-11T03:43:54Z', 'user_id': None}]
    return response

def add_list_member():

    response =  {'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'Test Description', 'enabled':True,
                 'expiration': '2019-09-29T23:00:00Z', 'hash_reputation_id': None,
                 'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '192.168.1.2', 'id': 20, 'resolution_state': 4, 'ttl': 5,
                          'updated_at': '2019-09-25T14:07:46Z'}, 'host_id': 22, 'id': 8, 'list_id': 1, 'response_id': None,
                 'reverse_user_id': None, 'updated_at': '2019-09-25T14:07:46Z', 'user_id': None
                }
    return response

def update_list_member():

    response =  {'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'Updated description', 'enabled': True,
                 'expiration': '2019-09-29T23:00:00Z', 'hash_reputation_id': None,
                 'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '192.168.1.2', 'id': 20, 'resolution_state': 4, 'ttl': 6,
                          'updated_at': '2019-09-25T14:17:17Z'}, 'host_id': 20, 'id': 8, 'list_id': 1, 'response_id': None,
                 'reverse_user_id': None, 'updated_at': '2019-09-25T14:17:17Z', 'user_id': None
                }
    return response

def delete_list_member():

    response = "OK"
    return response

def mocked_pptr_client(*args):

    class MockResponse:
        """Class will be used by the mock to replace pptr_client in circuits tests"""
        def __init__(self, *arg):
            self.r = Response()

        def __contains__(self, key):
            return True if key in self.__dict__.keys() else False

        def get_list_members(self, list_id=None, member_id=None, members_type=None):
            return get_list_members()

        def add_list_member(self, list_id=None, member=None, description=None, expiration=None, duration=None):
            return add_list_member()

        def update_list_member(self, list_id=None, member_id=None, description=None, expiration=None, duration=None):
            return update_list_member()

        def delete_list_member(self, list_id=None, member_id=None):
            return delete_list_member()

    return MockResponse(*args)


def get_mock_config():
    config_data = u"""[fn_proofpoint_trap]
base_url=https://traptesthost
api_key=abcd1234-a123-123a-123a-123456abcdef
polling_interval=2
startup_interval=20160
state=open
host_categories=attacker,cnc,forensics,url
"""
    return config_data
