# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_move_client"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_sep_move_client_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_move_client", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_move_client_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepMoveClient:
    """ Tests for the fn_sep_move_client function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_move_client.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_group_id, sep_hardwarekey, expected_results", [
        ("text", "text", {"value": "xyz"}),
        ("text", "text", {"value": "xyz"})
    ])
    def test_success(self, mock_patch, circuits_app, sep_group_id, sep_hardwarekey, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_c = ["data", "metadata"]
        keys_c_d = ["operating_system", "connector_guid", "connector_version", "hostname", "active", "links"]


        function_params = {
            "sep_group_id": sep_group_id,
            "sep_hardwarekey": sep_hardwarekey
        }
        results = call_fn_sep_move_client_function(circuits_app, function_params)
        assert(expected_results == results)
        assert expected_results == results["response"]["version"]
        assert_keys_in(results, *keys)
        computer = results["response"]
        assert_keys_in(computer, *keys_c)
        data = results["response"]["data"]
        assert_keys_in(data, *keys_c_d)