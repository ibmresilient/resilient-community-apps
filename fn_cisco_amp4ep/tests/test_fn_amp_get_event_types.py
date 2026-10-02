# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_event_types"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj


def call_fn_amp_get_event_types_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_event_types", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_event_types_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetEventTypes:
    """ Tests for the fn_amp_get_event_types function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_event_types.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("expected_results_1, expected_results_2, expected_results_3", [
        ("v1.2.0", 4, "An agent has started scanning.")
    ])
    def test_success(self, mock_get, circuits_app, expected_results_1, expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_et = ["data", "metadata"]
        keys_et_d_0 = ["description", "id", "name"]

        function_params = {
        }
        results = call_fn_amp_get_event_types_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        assert(expected_results_2 == len(results["response"]["data"]))
        event_types = results["response"]
        assert_keys_in(event_types, *keys_et)
        data = results["response"]["data"]
        assert_keys_in(data[0], *keys_et_d_0)
        assert expected_results_3 == data[0]["description"]