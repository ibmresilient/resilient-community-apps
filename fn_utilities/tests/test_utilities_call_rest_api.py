# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_call_rest_api"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_call_rest_api_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestCallRestApi:
    """ Tests for the call_rest_api function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("rest_method, rest_url, rest_headers, rest_body, expected_results", [
        ('GET', "http://foo", {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, {"value": "xyz"}),
        ('OPTIONS', "text", {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, rest_method, rest_url, rest_headers, rest_body, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "rest_method": rest_method,
            "rest_url": rest_url,
            "rest_headers": rest_headers,
            "rest_body": rest_body
        }
        #results = call_call_rest_api_function(circuits_app, function_params)
        #assert(expected_results == results)