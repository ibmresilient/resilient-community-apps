# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_codegen_test"
FUNCTION_NAME = "utilities_call_rest_api"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_utilities_call_rest_api_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("utilities_call_rest_api", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("utilities_call_rest_api_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesCallRestApi:
    """ Tests for the utilities_call_rest_api function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("rest_method, rest_url, rest_headers, rest_cookies, rest_body, rest_verify, expected_results", [
        ('GET', "text", {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, True, {"value": "xyz"}),
        ('POST', "text", {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, True, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, rest_method, rest_url, rest_headers, rest_cookies, rest_body, rest_verify, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "rest_method": rest_method,
            "rest_url": rest_url,
            "rest_headers": rest_headers,
            "rest_cookies": rest_cookies,
            "rest_body": rest_body,
            "rest_verify": rest_verify
        }
        results = call_utilities_call_rest_api_function(circuits_app, function_params)
        assert(expected_results == results)