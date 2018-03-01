# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "utility_functions"
FUNCTION_NAME = "wait"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_wait_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    circuits.manager.fire(SubmitTestFunction("wait", function_params))
    event = circuits.watcher.wait("wait_result", timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestWait:
    """ Tests for the wait function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("seconds, expected_result", [
        (123, {"value": "xyz"}),
        (123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, seconds, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "seconds": seconds
        }
        result = call_wait_function(circuits_app, function_params)
        assert(result == expected_result)