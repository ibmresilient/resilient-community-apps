# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import mocked_aws_iam_client, get_mock_config, get_func_responses

PACKAGE_NAME = "fn_aws_iam"
FUNCTION_NAME = "fn_aws_iam_list_user_policies"

# Read the mock configuration-data section from the package
config_data = get_mock_config()

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_aws_iam_list_user_policies_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_aws_iam_list_user_policies", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_aws_iam_list_user_policies_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAwsIamListUserPolicies:
    """ Tests for the fn_aws_iam_list_user_policies function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_aws_iam.components.fn_aws_iam_list_user_policies.AwsIamClient', side_effect=mocked_aws_iam_client)
    @pytest.mark.parametrize("aws_iam_user_name, expected_results", [
        ("iam_test_User", [get_func_responses("list_user_policies"),
         get_func_responses("list_attached_user_policies")]),
        ("iam_test_User_empty", get_func_responses("list_attached_user_policies_empty"))
    ])
    def test_success(self, mock_post, circuits_app, aws_iam_user_name, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]

        function_params = {
            "aws_iam_user_name": aws_iam_user_name
        }
        expected_result = []
        if expected_results:
            for user_policy in expected_results[0]:
                expected_result[:0] = [{"PolicyName": user_policy}]
            expected_result.extend(expected_results[1])
        results = call_fn_aws_iam_list_user_policies_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert expected_result == content
        pass