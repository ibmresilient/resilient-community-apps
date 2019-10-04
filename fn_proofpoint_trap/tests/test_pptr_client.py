# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test Sep client  class."""
from __future__ import print_function
from mock import patch
import pytest

from fn_proofpoint_trap.lib.pptr_client import *
from fn_proofpoint_trap.lib.helpers import transform_kwargs
from  mock_artifacts import mocked_request
"""
Suite of tests to test Symantec SEP client class
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def assert_value_not_none(json_obj, *keys):
    for key in keys:
        assert json_obj[key] is not None

def assert_values(json_obj, expected_results):
    for key in json_obj:
        assert json_obj[key] == expected_results[key]
        if type(json_obj[key]) == dict:
            for subkey in json_obj[key]:
                assert json_obj[key][subkey] == expected_results[key][subkey]

def get_config():
    return dict({
        "base_url": "https://traptesthost",
        "api_key": "abcd1234-a123-123a-123a-123456abcdef",
        "polling_interval": 2,
        "startup_interval": 20160,
        "state": "open",
        "host_categories": "attacker,cnc,forensics,url"
    })

class TestPPTRClient:
    """ Test pptr client using mocked data.  """

    """ Test pptr.get_list_members """
    @patch("fn_proofpoint_trap.lib.pptr_client.RequestsCommon", side_effect=mocked_request)
    @pytest.mark.parametrize("trap_list_id, trap_members_type, trap_member_id, expected_results", [
        (1, 'members.json', None, None)
    ])
    def test_get_list_members(self, mock_get, trap_list_id, trap_members_type, trap_member_id, expected_results):

        keys_host_1 = ["created_at", "deleted", "description", "enabled", "expiration", "host",
                     "host_id", "id", "list_id", "updated_at"]
        keys_host_2 = ["hash_reputation_id", "response_id", "reverse_user_id", "user_id"]

        test_kwargs = {
            "trap_list_id": trap_list_id,
            "trap_members_type": trap_members_type,
            "trap_member_id": trap_member_id
        }

        params = transform_kwargs(test_kwargs)
        pptr = PPTRClient(None, get_config())
        response = pptr.get_list_members(**params)
        for host in response:
            assert_keys_in(host, *keys_host_1)
            assert_keys_in(host, *keys_host_2)
            assert_value_not_none(host, *keys_host_1)

    """ Test pptr.add_list_member """
    @patch("fn_proofpoint_trap.lib.pptr_client.RequestsCommon", side_effect=mocked_request)
    @pytest.mark.parametrize("trap_list_id, trap_member, trap_description, trap_expiration, trap_duration, expected_results", [
        (1, "192.168.1.2", "Test Description", 1569798000000, 5, None)
    ])
    def test_add_list_member(self, mock_get, trap_list_id, trap_member, trap_description, trap_expiration, trap_duration,
                              expected_results):

        keys_host_1 = ["created_at", "deleted", "description", "enabled", "expiration", "host",
                     "host_id", "id", "list_id", "updated_at"]
        keys_host_2 = ["hash_reputation_id", "response_id", "reverse_user_id", "user_id"]

        expected_results = {
            'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'Test Description',
            'enabled': True, 'expiration': '2019-09-29T23:00:00Z', 'hash_reputation_id': None,
            'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '192.168.1.2', 'id': 20,
                     'resolution_state': 4, 'ttl': 5, 'updated_at': '2019-09-25T14:07:46Z'},
            'host_id': 22, 'id': 8, 'list_id': 1, 'response_id': None, 'reverse_user_id': None,
            'updated_at': '2019-09-25T14:07:46Z', 'user_id': None
        }
        test_kwargs = {
            "trap_list_id": trap_list_id,
            "trap_member": trap_member,
            "trap_description": trap_description,
            "trap_expiration": trap_expiration,
            "trap_duration": trap_duration
        }

        params = transform_kwargs(test_kwargs)
        pptr = PPTRClient(None, get_config())
        response = pptr.add_list_member(**params)
        assert_keys_in(response, *keys_host_1)
        assert_keys_in(response, *keys_host_2)
        assert_values(response, expected_results)

    """ Test pptr.update_list_member """
    @patch("fn_proofpoint_trap.lib.pptr_client.RequestsCommon", side_effect=mocked_request)
    @pytest.mark.parametrize("trap_list_id, trap_member_id, trap_description, trap_expiration, trap_duration, expected_results", [
        (1, "192.168.1.2", "Test Description", 1569798000000, 5, None)
    ])
    def test_update_list_member(self, mock_get, trap_list_id, trap_member_id, trap_description, trap_expiration, trap_duration,
                              expected_results):

        keys_host_1 = ["created_at", "deleted", "description", "enabled", "expiration", "host",
                     "host_id", "id", "list_id", "updated_at"]
        keys_host_2 = ["hash_reputation_id", "response_id", "reverse_user_id", "user_id"]

        expected_results = {
            'created_at': '2017-01-11T03:47:15Z', 'deleted': False, 'description': 'Updated description',
            'enabled': True, 'expiration': '2019-09-29T23:00:00Z', 'hash_reputation_id': None,
            'host': {'created_at': '2017-01-11T03:47:15Z', 'host': '192.168.1.2', 'id': 20, 'resolution_state': 4,
                     'ttl': 6, 'updated_at': '2019-09-25T14:17:17Z'}, 'host_id': 20, 'id': 8, 'list_id': 1,
            'response_id': None, 'reverse_user_id': None, 'updated_at': '2019-09-25T14:17:17Z', 'user_id': None
        }
        test_kwargs = {
            "trap_list_id": trap_list_id,
            "trap_member_id": trap_member_id,
            "trap_description": trap_description,
            "trap_expiration": trap_expiration,
            "trap_duration": trap_duration
        }

        params = transform_kwargs(test_kwargs)
        pptr = PPTRClient(None, get_config())
        response = pptr.update_list_member(**params)
        assert_keys_in(response, *keys_host_1)
        assert_keys_in(response, *keys_host_2)
        assert_values(response, expected_results)

    """ Test pptr.delete_list_member """
    @patch("fn_proofpoint_trap.lib.pptr_client.RequestsCommon", side_effect=mocked_request)
    @pytest.mark.parametrize("trap_list_id, trap_member_id, expected_results", [
        (1, 8, "OK")
    ])
    def test_delete_list_member(self, mock_get, trap_list_id, trap_member_id, expected_results):

        test_kwargs = {
            "trap_list_id": trap_list_id,
            "trap_member_id": trap_member_id
        }

        params = transform_kwargs(test_kwargs)
        pptr = PPTRClient(None, get_config())
        response = pptr.delete_list_member(**params)
        assert (expected_results == response)

    """ Test pptr.get_incident_details """
    @patch("fn_proofpoint_trap.lib.pptr_client.RequestsCommon", side_effect=mocked_request)
    @pytest.mark.parametrize("trap_incident_id, expected_result", [
        (123, "https://traptesthost/incidents/123.json")
    ])
    def test_get_incident_details(self, mock_get, trap_incident_id, expected_result):

        keys = ["data", "href"]
        keys_data = ["assignee", "created_at", "description", "hosts", "event_count", "events", "score", "type"]

        test_kwargs = {
            "trap_incident_id": trap_incident_id
        }

        params = transform_kwargs(test_kwargs)
        pptr = PPTRClient(None, get_config())
        response = pptr.get_incident_details(**params)
        assert_keys_in(response, *keys)
        assert expected_result == response["href"]
        data = response["data"]
        assert_keys_in(data, *keys_data)