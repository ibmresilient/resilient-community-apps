# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Test Sep client  class."""
from __future__ import print_function
import datetime
from dateutil.tz import tzutc
from mock import patch
import pytest
from fn_aws_iam.lib.aws_iam_client import *
from .mock_artifacts import *

"""
Suite of tests to test AWS IAM client class
"""

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def get_config():
    return dict({
        "aws_iam_access_key_id":    "AKAABBCCDDEEFFGGHH12",
        "aws_iam_secret_access_key": "pplXXEEK/aAbBcCdDeEfFgGhHiH1234567+sssss",
        "aws_iam_region":   None
    })

class TestAWSIAMClient:
    """ Test aws_iam_client using mocked data.  """

    """ Test sep_client._get_client"""
    @pytest.mark.parametrize("service, expected_result", [
        ("iam", "botocore.client.IAM object at "),
        ("sts", "botocore.client.STS object at "),
    ])
    def test_get_client(self, service, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli._get_client(service)
        assert(expected_result in repr(response))

    """ Test sep_client.__get_type_from_response"""
    @pytest.mark.parametrize("op, type_list, expected_result", [
        ("get_user", SUPPORTED_GET_TYPES, "User"),
        ("list_user_tags", SUPPORTED_GET_TYPES, "Tags"),
        ("get_login_profile", SUPPORTED_GET_TYPES, "LoginProfile"),
    ])
    def test_get_type_from_response(self, op, type_list, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli._get_type_from_response(get_cli_raw_responses(op), type_list)
        assert(expected_result in repr(response))

    """ Test sep_client.__get_type_from_response negative case"""
    @pytest.mark.parametrize("op, type_list, expected_result", [
        ("get_user", SUPPORTED_PAGINATE_TYPES, "No supported type for integration found in AWS IAM response")
    ])
    def test_get_type_from_response_err(self, op, type_list, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        with pytest.raises(ValueError) as e:
            response = iam_cli._get_type_from_response(get_cli_raw_responses(op), type_list)
        assert str(e.value) == expected_result

    """ Test sep_client._add_user_properties"""
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient.get', side_effect=mocked_client_get_profile)
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_default_identity', side_effect=get_default_identity)
    @pytest.mark.parametrize("result, expected_result", [
        (mocked_iam_pre_results("pre_result_add_prop"), mock_client_results("expected_result_add_prop")),
        (mocked_iam_pre_results("pre_result_default_add_prop"), mock_client_results("expected_result_default_add_prop")),
        (mocked_iam_pre_results("pre_result_with_profile_add_prop"), mock_client_results("expected_result_with_profile_add_prop")),

    ])
    def test_add_user_properties(self, mock_profile, mock_id, result, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli._add_user_properties(result)
        assert(expected_result == response)

    """ Test sep_client._update_result"""
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient.get', side_effect=mocked_client_get_profile)
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_default_identity', side_effect=get_default_identity)
    @pytest.mark.parametrize("result, result_type, expected_result", [
        (mocked_iam_pre_results("get_user"), "User", mock_client_results("expected_result_default_add_prop")),
        (mocked_iam_pre_results("groups"), "groups", mock_client_results("expected_result_upd_group")),
        (mocked_iam_pre_results("access_keys"), "AccessKeyMetadata", mock_client_results("expected_result_upd_keys")),

    ])
    def test_update_result(self, mock_profile, mock_id, result, result_type, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli._update_result(result, result_type)
        assert(expected_result == response)

    """ Test sep_client._datetime_to_str"""
    @pytest.mark.parametrize("result_entry, expected_result", [
        (mocked_iam_pre_results("get_user")[0], ["2019-10-31 16:23:07", "2019-11-15 17:11:28"])
    ])
    def test_datetime_to_str(self, result_entry, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli._datetime_to_str(result_entry)
        assert(expected_result[0] == response["CreateDate"])
        assert (expected_result[1] == response["PasswordLastUsed"])


    """ Test sep_client.paginate"""
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient.get', side_effect=mocked_client_get_profile)
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_default_identity', side_effect=get_default_identity)
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._filter', side_effect=None)
    @patch('botocore.client.BaseClient.get_paginator', side_effect=mocked_client_paginator)
    @pytest.mark.parametrize("op, expected_result", [
        ("list_users", mock_client_results("expected result_pagination"))
    ])
    def test_paginate(self, mock_orofile, mock_id, mock_filter, mock_paginator, op, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli.paginate(op)
        assert (expected_result == response)

    """ Test sep_client.get"""
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_default_identity', side_effect=get_default_identity)
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_client', side_effect=mocked_iam)
    @pytest.mark.parametrize("op, expected_result", [
        ("get_user", mock_client_results("expected_result_get"))
    ])
    def test_get(self, mock_id, mock_iam, op, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli.get(op)
        assert (expected_result == response)

    """ Test sep_client.post"""
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_default_identity', side_effect=get_default_identity)
    @patch('fn_aws_iam.lib.aws_iam_client.AwsIamClient._get_client', side_effect=mocked_iam)
    @pytest.mark.parametrize("op, expected_result", [
       ( "get_user", "OK")
    ])
    def test_post(self, mock_id, mock_iam, op, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli.post(op)
        assert (expected_result == response)

    """ Test sep_client._filter"""
    @pytest.mark.parametrize("result, results_filter, expected_result", [
        (get_func_responses("list_users"), None, 4),
        (get_func_responses("list_users"), {'UserName': u'test_user'}, 0),
        (get_func_responses("list_users"), {'UserName': 'iam_list_User_1'}, 1),
        (get_func_responses("list_groups_for_user"), {'GroupName': u'test_group'}, [0, 2]),
        (get_func_responses("list_groups_for_user"), {'GroupName': 'null_group'}, [1, 2]),
        (get_func_responses("list_policies"), {'PolicyName': u'test_policy'}, [0, 3]),
        (get_func_responses("list_policies"), {'PolicyName': 'deny_all'}, [1, 3]),
    ])
    def test__filter(self, result, results_filter, expected_result):
        options = {}

        iam_cli = AwsIamClient(options, get_config())
        response = iam_cli._filter(result, results_filter)
        if isinstance(expected_result, list):
            assert (expected_result[0] == response[0])
            assert (expected_result[1] == len(response[1]))
        else:
            assert (expected_result == response[0])
            assert (expected_result == len(response[1]))