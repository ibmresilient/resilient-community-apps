# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import mocked_aws_iam_client, get_mock_config, get_func_responses

PACKAGE_NAME = "fn_aws_iam"
FUNCTION_NAME = "fn_aws_iam_list_users"

# Read the mock configuration-data section from the package
config_data = get_mock_config()

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_aws_iam_list_users_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_aws_iam_list_users", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_aws_iam_list_users_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestFnAwsIamListUsers:
    """ Tests for the fn_aws_iam_list_users function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_aws_iam.components.fn_aws_iam_list_users.AwsIamClient', side_effect=mocked_aws_iam_client)
    @pytest.mark.parametrize("aws_iam_user_name, aws_iam_user_filter, aws_iam_group_filter, aws_iam_policy_filter, "
                             "aws_iam_access_key_filter, aws_iam_query_type, expected_results", [
        (None, None, None, None, None, None, get_func_responses("list_users")),
        ("iam_test_User_1", None, None, None, None, None, get_func_responses("get_user")),
        (None, "iam_test_User_1", None, None, None, "users", get_func_responses("list_users_filtered_by_name_all_types")),
        (None, None, "null_group", None, None, "users",get_func_responses("list_users_filtered_by_group")),
        (None, None, None, "deny_all", None, "users", get_func_responses("list_users_filtered_by_policy")),
        (None, "not_exists", None, None, None, "users", []),
        (None, None, None, None, "123", "access_keys", get_func_responses("list_users_filtered_by_keys_with_dates")),

    ])
    def test_success(self, mock_get, circuits_app, aws_iam_user_name, aws_iam_user_filter, aws_iam_group_filter,
                     aws_iam_policy_filter, aws_iam_access_key_filter, aws_iam_query_type, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]

        function_params = {
            "aws_iam_user_name": aws_iam_user_name,
            "aws_iam_user_filter": aws_iam_user_filter,
            "aws_iam_group_filter": aws_iam_group_filter,
            "aws_iam_policy_filter": aws_iam_policy_filter,
            "aws_iam_access_key_filter": aws_iam_access_key_filter,
            "aws_iam_query_type": aws_iam_query_type
        }
        results = call_fn_aws_iam_list_users_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert expected_results == content

