# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test Bigfix client  class"""
from __future__ import print_function
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from fn_cisco_amp4ep.lib.amp_client import *
from  mock_artifacts import mocked_session

"""
Suite of tests to test Cisco AMP client class
"""
def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_config():
    return dict({
        "bigfix_url": "https://api.amp.cisco.com/",
        "api_version": "v1",
        "client_id": "01234abcde56789efedc",
        "api_token": "abcd1234-a123-123a-123a-123456abcdef",
    })

class TestAMPClient:
    """ Test amp_client using mocked data.  """

    """ Test amp_client.get_computer """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_conn_guid, expected_results", [
        ("00da1a57-b833-43ba-8ea2-79a5ab21908f", "v1.2.0")
    ])
    def test_get_computer(self, mock_get, amp_conn_guid, expected_results):

        keys = ["data", "metadata"]
        keys_d = ["operating_system", "connector_guid", "connector_version", "hostname", "active", "links"]

        amp_client = Ampclient(get_config())
        response = amp_client.get_computer(amp_conn_guid)
        assert expected_results == response["version"]
        assert_keys_in(response, *keys)
        data = response["data"]
        assert_keys_in(data, *keys_d)

    """ Test amp_client.get_computers  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_group_guid, amp_limit, amp_hostname, amp_internal_ip, amp_external_ip, "
                             "expected_results_1, expected_results_2", [
        (None, None, None, None, None, "v1.2.0", 6)
    ])
    def test_get_computers(self, mock_get, amp_group_guid, amp_limit, amp_hostname, amp_internal_ip, amp_external_ip,
                           expected_results_1, expected_results_2):

        keys = ["data", "metadata"]
        keys_d = ["operating_system", "connector_guid", "connector_version", "hostname", "active", "links"]

        params = {
            "group_guid": amp_group_guid,
            "limit": amp_limit,
            "hostname": amp_hostname,
            "internal_ip": amp_internal_ip,
            "external_ip": amp_external_ip
        }
        amp_client = Ampclient(get_config())
        response = amp_client.get_computers(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == response["metadata"]["results"]["total"]
        data = response["data"]
        for d in data:
            assert_keys_in(d, *keys_d)

    """ Test amp_client.get_computer_trajectory  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_conn_guid, amp_limit, expected_results", [
        ("00da1a57-b833-43ba-8ea2-79a5ab21908f", None, "v1.2.0")
    ])
    def test_get_computer_trajectory(self, mock_get, amp_conn_guid, amp_limit, expected_results):

        keys = ["data", "metadata"]
        keys_d = ["computer", "events"]

        amp_client = Ampclient(get_config())
        response = amp_client.get_computer_trajectory(amp_conn_guid, amp_limit)
        assert expected_results == response["version"]
        assert_keys_in(response, *keys)
        data = response["data"]
        assert_keys_in(data, *keys_d)

    """ Test amp_client.get_activity  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_q, amp_limit, amp_offset, expected_results_1, expected_results_2", [
        ("SearchProtocolHost.exe", None, None, "v1.2.0", 4)
    ])
    def test_get_activity(self, mock_get, amp_q, amp_limit, amp_offset, expected_results_1, expected_results_2):

        keys = ["data", "metadata"]
        keys_d = ["connector_guid", "hostname", "active", "links"]

        params = {
            "q": amp_q,
            "limit": amp_limit,
            "offset": amp_offset
        }
        amp_client = Ampclient(get_config())
        response = amp_client.get_activity(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == response["metadata"]["results"]["total"]
        data = response["data"]
        for d in data:
            assert_keys_in(d, *keys_d)

    """ Test amp_client.get_file_lists  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_scd_name, amp_limit, amp_offset, expected_results_1, expected_results_2", [
        (None, None, None, "v1.2.0", 1)
    ])
    def test_get_file_lists(self, mock_get, amp_scd_name, amp_limit, amp_offset, expected_results_1, expected_results_2):

        keys = ["data", "metadata"]
        keys_d = ["guid", "links", "name", "type"]

        params = {
            "name": amp_scd_name,
            "limit": amp_limit,
            "offset": amp_offset
        }
        amp_client = Ampclient(get_config())
        response = amp_client.get_file_lists(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == response["metadata"]["results"]["total"]
        data = response["data"]
        for d in data:
            assert_keys_in(d, *keys_d)


    """ Test amp_client.get_file_list_files  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_file_list_guid, amp_file_sha256, amp_limit, amp_offset, expected_results_1, "
                             "expected_results_2, expected_results_3", [
        ("9710a198-b95a-462a-b184-9e688968fd94", None, None, None, "v1.2.0", 1, 10),
        ("9710a198-b95a-462a-b184-9e688968fd94", "e93faae7706644387cd3383aaf1bd9919f9f441acce498f15391eb60eb54288b",
         None, None, "v1.2.0", 1, "Created by entering SHA-256 via Public api.")
    ])
    def test_get_file_list_files(self, mock_get, amp_file_list_guid, amp_file_sha256, amp_limit, amp_offset, expected_results_1,
                            expected_results_2, expected_results_3):

        keys = ["data", "metadata"]
        if amp_file_sha256 is None:
            keys_d = ["guid", "items", "name", "policies"]
            keys_d_p = ["guid", "name", "links"]
        else:
            keys_d = ["links", "sha256", "source"]

        params = {
            "file_list_guid": amp_file_list_guid,
            "file_sha256": amp_file_sha256,
            "limit": amp_limit,
            "offset": amp_offset
        }
        amp_client = Ampclient(get_config())
        response = amp_client.get_file_list_files(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        if (params["file_sha256"]) is None:
            assert expected_results_2 == response["metadata"]["results"]["total"]
            data = response["data"]
            assert_keys_in(data, *keys_d)
            policies = data["policies"]
            assert expected_results_3 == len(policies)
            for p in policies:
                assert_keys_in(p, *keys_d_p)
        else:
            assert expected_results_2 == len(response["metadata"]["links"])
            data = response["data"]
            assert_keys_in(data, *keys_d)
            assert expected_results_3 == response["data"]["source"]

    """ Test amp_client.set_file_list_files  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_file_list_guid, amp_file_sha256, amp_file_description, expected_results_1, "
                             "expected_results_2, expected_results_3", [
        ("9710a198-b95a-462a-b184-9e688968fd94", "e93faae7706644387cd3383aaf1bd9919f9f441acce498f15391eb60eb54288b",
         "Test description", "v1.2.0", 1, "Test file sha256")
    ])
    def test_set_file_lists(self, mock_get, amp_file_list_guid, amp_file_sha256, amp_file_description, expected_results_1,
                            expected_results_2, expected_results_3):

        keys = ["data", "metadata"]

        keys_d = ["links", "sha256", "source", "description"]

        params = {
            "file_list_guid": amp_file_list_guid,
            "file_sha256": amp_file_sha256,
            "description": amp_file_description
        }
        amp_client = Ampclient(get_config())
        response = amp_client.set_file_list_files(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == len(response["metadata"]["links"])
        data = response["data"]
        assert_keys_in(data, *keys_d)
        description = data["description"]
        assert expected_results_3 == description

    """ Test amp_client.delete_file_list_files  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_file_list_guid, amp_file_sha256, amp_file_description, expected_results_1, "
                             "expected_results_2, expected_results_3", [
        ("9710a198-b95a-462a-b184-9e688968fd94", "e93faae7706644387cd3383aaf1bd9919f9f441acce498f15391eb60eb54288b",
         "Test description", "v1.2.0", 1, 0)
    ])
    def test_delete_file_lists(self, mock_get, amp_file_list_guid, amp_file_sha256, amp_file_description, expected_results_1,
                            expected_results_2, expected_results_3):

        keys = ["data", "metadata"]

        params = {
            "file_list_guid": amp_file_list_guid,
            "file_sha256": amp_file_sha256,
        }
        amp_client = Ampclient(get_config())
        response = amp_client.delete_file_list_files(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == len(response["metadata"]["links"])
        data = response["data"]
        assert expected_results_3 == len(data)

    """ Test amp_client.get_events  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_detection_sha256, amp_application_sha256, amp_conn_guid, amp_group_guid, "
                             " amp_start_date, amp_event_type, amp_limit, amp_offset, expected_results_1, "
                             "expected_results_2, expected_results_3", [
                                 (None, None, None, None, None, None, None, None, "v1.2.0", 1, "WIN-S1AC1PI6L5L")
                             ])
    def test_get_events(self, mock_get, amp_detection_sha256, amp_application_sha256, amp_conn_guid,
                               amp_group_guid, amp_start_date, amp_event_type, amp_limit, amp_offset,
                               expected_results_1, expected_results_2, expected_results_3):

        keys = ["data", "metadata"]
        keys_d = ["computer", "date", "detection_id", "event_type", "event_type_id", "file",
                  "group_guids", "id", "timestamp", "timestamp_nanoseconds" ]
        params = {
            "detection_sha256": amp_detection_sha256,
            "application_sha256": amp_application_sha256,
            "connector_guid": amp_conn_guid,
            "group_guid": amp_group_guid,
            "start_date": amp_start_date,
            "event_type": amp_event_type,
            "limit": amp_limit,
            "offset": amp_offset
        }
        amp_client = Ampclient(get_config())
        response = amp_client.get_events(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == response["metadata"]["results"]["total"]
        data = response["data"]
        assert_keys_in(data[0], *keys_d)
        assert expected_results_3 == response["data"][0]["computer"]["hostname"]

    """ Test amp_client.get_event_types  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("expected_results_1, expected_results_2, expected_results_3", [
        ("v1.2.0", 4, "An agent has started scanning.")
    ])
    def test_get_event_types(self, mock_get, expected_results_1, expected_results_2, expected_results_3):

        keys = ["data", "metadata"]
        keys_d = ["description", "id", "name"]

        amp_client = Ampclient(get_config())
        response = amp_client.get_event_types()
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == response["metadata"]["results"]["total"]
        data = response["data"]
        assert_keys_in(data[0], *keys_d)
        assert expected_results_3 == response["data"][0]["description"]

    """ Test amp_client.get_groups  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_group_guid, amp_group_name, amp_limit, expected_results_1, expected_results_2, "
                             "expected_results_3", [
        ("4060cf94-26e5-4176-8dea-cd3d0b68d8bc", None, 1, "v1.2.0", 2, "Audit Group"),
        (None, "Audit", 1, "v1.2.0", 1, "Audit Group for FireAMP API Docs")
    ])
    def test_get_groups(self, mock_get, amp_group_guid, amp_group_name, amp_limit, expected_results_1, expected_results_2,
                        expected_results_3):

        keys = ["data", "metadata"]
        keys_d = ["description", "guid", "links", "name", "source"]

        params = {
            "group_guid": amp_group_guid,
            "name": amp_group_name,
            "limit": amp_limit
        }
        amp_client = Ampclient(get_config())
        response = amp_client.get_groups(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        assert expected_results_2 == response["metadata"]["results"]["total"]
        data = response["data"]
        assert_keys_in(data[0], *keys_d)
        assert expected_results_3 == response["data"][0]["description"]

    """ Test amp_client.move_computer  """
    @patch('fn_cisco_amp4ep.lib.amp_client.requests.Session', side_effect=mocked_session)
    @pytest.mark.parametrize("amp_conn_guid, amp_group_guid, expected_results_1, expected_results_2", [
        ("ad29d359-dac9-4940-9c7e-c50e6d32ee6f", "b077d6bc-bbdf-42f7-8838-a06053fbd98a", "v1.2.0", "Demo_CozyDuke")
    ])
    def test_move_computer(self, mock_get, amp_conn_guid, amp_group_guid, expected_results_1, expected_results_2):

        keys = ["data", "metadata"]
        keys_d = ["active", "connector_guid", "connector_version", "external_ip", "group_guid"]

        params = {
            "connector_guid": amp_conn_guid,
            "group_guid": amp_group_guid
        }
        amp_client = Ampclient(get_config())
        response = amp_client.move_computer(**params)
        assert expected_results_1 == response["version"]
        assert_keys_in(response, *keys)
        data = response["data"]
        assert_keys_in(data, *keys_d)
        assert expected_results_2 == response["data"]["hostname"]