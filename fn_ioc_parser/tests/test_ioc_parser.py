# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""
# Copyright IBM Corp. - Confidential Information
from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_ioc_parser"
FUNCTION_NAME = "ioc_parser"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_ioc_parser_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("ioc_parser", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("ioc_parser_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestIocParser:
    """ Tests for the ioc_parser function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("inputType, artifactId, incidentId, expected_results", [
        ('pdf', 123, 123, {"value": "xyz"}),
        ('pdf', 123, 123, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, inputType, artifactId, incidentId, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "inputType": inputType,
            "artifactId": artifactId,
            "incidentId": incidentId
        }
        results = call_ioc_parser_function(circuits_app, function_params)
        assert(expected_results == results)