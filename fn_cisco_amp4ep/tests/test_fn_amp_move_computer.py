# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_move_computer"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_amp_move_computer_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_move_computer", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_move_computer_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpMoveComputer:
    """ Tests for the fn_amp_move_computer function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_move_computer.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_conn_guid, amp_group_guid, expected_results_1, expected_results_2", [
        ("ad29d359-dac9-4940-9c7e-c50e6d32ee6f", "b077d6bc-bbdf-42f7-8838-a06053fbd98a", "v1.2.0", "Demo_CozyDuke")
    ])
    def test_success(self, mock_get, circuits_app, amp_conn_guid, amp_group_guid, expected_results_1, expected_results_2):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_mv = ["data", "metadata"]
        keys_mv_d = ["active", "connector_guid", "connector_version", "external_ip", "group_guid"]


        function_params = {
            "amp_conn_guid": amp_conn_guid,
            "amp_group_guid": amp_group_guid
        }
        results = call_fn_amp_move_computer_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        move_group = results["response"]
        assert_keys_in(move_group, *keys_mv)
        data = results["response"]["data"]
        assert_keys_in(data, *keys_mv_d)
        assert expected_results_2 == move_group["data"]["hostname"]