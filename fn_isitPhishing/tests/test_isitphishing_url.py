# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_isitPhishing"
FUNCTION_NAME = "isitphishing_url"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_isitphishing_url_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("isitphishing_url", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("isitphishing_url_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestIsitphishingUrl:
    """ Tests for the isitphishing_url function"""
    inputs = {
        "isitphishing_url": "http://www.thisisaphishingurl.com"
    }
    output = {"analysis": {"status": "PHISHING"},
              "inputs": {"URL": inputs["isitphishing_url"]}
    }
    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, isitphishing_url, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = inputs

        with patch("fn_isitPhishing.components.isitphishing_url.requests.post") as mock_requests_get:
            # Replace the return value of our mock_session with a custom function
            mock_requests_get.return_value = mocked_requests_get(success=True)

            results = call_isitphishing_url_function(circuits_app, function_params)
            assert(expected_results == results)
