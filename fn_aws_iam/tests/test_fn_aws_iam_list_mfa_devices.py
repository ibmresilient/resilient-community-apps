# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import mocked_aws_iam_client, get_mock_config, get_func_responses

PACKAGE_NAME = "fn_aws_iam"
FUNCTION_NAME = "fn_aws_iam_list_mfa_devices"

# Read the mock configuration-data section from the package
config_data = get_mock_config()

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_aws_iam_list_mfa_devices_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_aws_iam_list_mfa_devices", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_aws_iam_list_mfa_devices_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnAwsIamListMfaDevices:
    """ Tests for the fn_aws_iam_list_mfa_devices function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch("fn_aws_iam.components.fn_aws_iam_list_mfa_devices.AwsIamClient", side_effect=mocked_aws_iam_client)
    @pytest.mark.parametrize("aws_iam_user_name, expected_results", [
        ("iam_test_user", [{'EnableDate': '2015-06-16T22:36:37Z',
                              'SerialNumber': 'arn:aws:iam::123456789012:mfa/iam_test_user_1',
                              'UserName': 'iam_test_user'}]),
        ("iam_test_user_has_virt", [{'EnableDate': '2015-06-16T22:36:37Z',
                                     'SerialNumber': 'arn:aws:iam::123456789012:mfa/iam_test_user_has_virt',
                                     'UserName': 'iam_test_user_has_virt',
                                     'is_virtual': True}]),
        ("iam_test_user_no_devs", []),
        ("iam_test_user_not_exists", {'Status': 'NoSuchEntity'}),
    ])
    def test_success(self, mock_get, circuits_app, aws_iam_user_name, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]

        function_params = {
            "aws_iam_user_name": aws_iam_user_name
        }

        results = call_fn_aws_iam_list_mfa_devices_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert expected_results == content
