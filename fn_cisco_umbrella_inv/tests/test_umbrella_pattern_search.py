# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_pattern_search"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_umbrella_pattern_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_pattern_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_pattern_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaPatternSearch:
    """ Tests for the umbrella_pattern_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("a5e6e21f-b9f0-4168-beb8-0a41c778705c, 2b9d77ae-efaa-45ef-a64f-8a3f763ba58d, 8834d538-cabd-4d3e-a822-c89f4f96a3d7, 9e516a4b-9785-4802-bdac-575a6a51f430, ace816e4-59f1-4df1-8356-5dfe300c35f7, expected_results", [
        ("text", 1518367008000, "text", 123, True, {"value": "xyz"}),
        ("text", 1518367008000, "text", 123, True, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, a5e6e21f-b9f0-4168-beb8-0a41c778705c, 2b9d77ae-efaa-45ef-a64f-8a3f763ba58d, 8834d538-cabd-4d3e-a822-c89f4f96a3d7, 9e516a4b-9785-4802-bdac-575a6a51f430, ace816e4-59f1-4df1-8356-5dfe300c35f7, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "a5e6e21f-b9f0-4168-beb8-0a41c778705c": a5e6e21f-b9f0-4168-beb8-0a41c778705c,
            "2b9d77ae-efaa-45ef-a64f-8a3f763ba58d": 2b9d77ae-efaa-45ef-a64f-8a3f763ba58d,
            "8834d538-cabd-4d3e-a822-c89f4f96a3d7": 8834d538-cabd-4d3e-a822-c89f4f96a3d7,
            "9e516a4b-9785-4802-bdac-575a6a51f430": 9e516a4b-9785-4802-bdac-575a6a51f430,
            "ace816e4-59f1-4df1-8356-5dfe300c35f7": ace816e4-59f1-4df1-8356-5dfe300c35f7
        }
        results = call_umbrella_pattern_search_function(circuits_app, function_params)
        assert(expected_results == results)