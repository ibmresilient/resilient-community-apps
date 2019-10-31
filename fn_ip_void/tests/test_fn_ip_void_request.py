# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_ip_void"
FUNCTION_NAME = "fn_ip_void_request"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_ip_void_request_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_ip_void_request", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_ip_void_request_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnIpVoidRequest:
    """ Tests for the fn_ip_void_request function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("ip_void_request_type, ip_void_artifact_type, ip_void_artifact_value, expected_results", [
        ('Threat Log', "text", "text", {"value": "xyz"}),
        ('Domain Blacklist', "text", "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, ip_void_request_type, ip_void_artifact_type, ip_void_artifact_value, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "ip_void_request_type": ip_void_request_type,
            "ip_void_artifact_type": ip_void_artifact_type,
            "ip_void_artifact_value": ip_void_artifact_value
        }
        results = call_fn_ip_void_request_function(circuits_app, function_params)
        assert(expected_results == results)