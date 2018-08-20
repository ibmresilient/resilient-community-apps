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
