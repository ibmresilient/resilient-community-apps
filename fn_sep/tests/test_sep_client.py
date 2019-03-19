# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test Bigfix client  class"""
from __future__ import print_function
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import pytest
from fn_sep.lib.sep_client import *
from  mock_artifacts import mocked_request
from fn_sep.lib.helpers import transform_kwargs

"""
Suite of tests to test Symantec SEP client class
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_config():
    return dict({
        "base_path":    "/sepm/api/v1",
        "auth_path":    "/sepm/api/v1/identity/authenticate",
        "host":         "192.168.1.2",
        "port":         "8446",
        "username":     "admin",
        "password":     "password",
        "domain":       "Default"
    })

class TestSEPClient:
    """ Test sep_client using mocked data.  """

    """ Test sep_client._get_token"""
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result", [
        ("abcd1234-a123-123a-123a-123456abcdef")
    ])
    def test_get_token(self, mock_post, expected_result):
        options = None
        function_params = None

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client._get_token()
        assert(response == expected_result)

    """ Test sep_client.get_version  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result_1, expected_result_2, expected_result_3", [
        ("14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_get_version(self, mock_get, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client.get_version(**params)
        assert expected_result_1 == response[keys[0]]
        assert expected_result_2 == response[keys[1]]
        assert expected_result_3 == response[keys[2]]
        assert_keys_in(response, *keys)

    """ Test sep_client.get_domains  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result_1, expected_result_2, expected_result_3", [
        ("14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_get_domains(self, mock_get, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client.get_domains(**params)
        test=1

    """ Test sep_client.get_computers  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result_1, expected_result_2, expected_result_3", [
        ("14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_get_computers(self, mock_get, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
        }

        sep_client = Sepclient(get_config())
        response = sep_client.get_computers(**params)

    """ Test sep_client.get_groups  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("expected_result_1, expected_result_2, expected_result_3", [
        ("14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_get_groups(self, mock_get, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
        }
        sep_client = Sepclient(get_config())
        response = sep_client.get_groups(**params)

    """ Test sep_client.get_policies_summary  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_domainid, sep_policy_type, expected_result_1, expected_result_2, expected_result_3", [
        ("908090000946C25D330E919313D23887", {'name': 'fw', 'id': 201}, "14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_get_policies_summary(self, mock_get, sep_domainid, sep_policy_type, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
            "sep_domainid": sep_domainid,
            "sep_policy_type": sep_policy_type
        }
        transform_kwargs(params)
        sep_client = Sepclient(get_config())
        response = sep_client.get_policies_summary(**params)

    """ Test sep_client.move_client  """
    @patch("fn_sep.lib.sep_client.RequestsSep", side_effect=mocked_request)
    @pytest.mark.parametrize("sep_group_id, sep_hardwarekey, expected_result_1, expected_result_2, expected_result_3", [
        ("8E20F39B0946C25D118925C2E28C2D59", "DC7D24D6465566D2941F35BC8D17801E", "14.2.1031.0100", "181118008", "1.0.0")
    ])
    def test_move_client(self, mock_get, sep_group_id, sep_hardwarekey, expected_result_1, expected_result_2, expected_result_3):
        keys = ["version", "API_SEQUENCE", "API_VERSION"]

        params = {
            "sep_group_id": sep_group_id,
            "sep_hardwarekey": sep_hardwarekey
        }
        transform_kwargs(params)
        sep_client = Sepclient(get_config())
        response = sep_client.move_client(**params)
        test=1
