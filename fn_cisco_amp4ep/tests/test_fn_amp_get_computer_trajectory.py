# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_computer_trajectory"

# Mock configuration-data section
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_amp_get_computer_trajectory_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_computer_trajectory", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_computer_trajectory_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetComputerTrajectory:
    """ Tests for the fn_amp_get_computer_trajectory function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_computer_trajectory.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_conn_guid, expected_results", [
        ("00da1a57-b833-43ba-8ea2-79a5ab21908f", "v1.2.0")
    ])
    def test_success(self, mock_get, circuits_app, amp_conn_guid, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["computer_trajectory", "query_execution_time"]
        keys_a = ["data", "metadata"]
        keys_a_d = ["computer", "events"]

        function_params = { 
            "amp_conn_guid": amp_conn_guid
        }
        results = call_fn_amp_get_computer_trajectory_function(circuits_app, function_params)
        assert expected_results == results["computer_trajectory"]["version"]
        assert_keys_in(results, *keys)
        activity = results["computer_trajectory"]
        assert_keys_in(activity, *keys_a)
        data = results["computer_trajectory"]["data"]
        assert_keys_in(data, *keys_a_d)
