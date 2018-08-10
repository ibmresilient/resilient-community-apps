# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_computer"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_amp_get_computer_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_computer", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_computer_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetComputer:
    """ Tests for the fn_amp_get_computer function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("amp_conn_guid, expected_results", [
        ("text", {"value": "xyz"}),
        ("text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, amp_conn_guid, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "amp_conn_guid": amp_conn_guid
        }
        results = call_fn_amp_get_computer_function(circuits_app, function_params)
        assert(expected_results == results)