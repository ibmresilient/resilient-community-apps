# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_domain_status_and_category"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_umbrella_domain_status_and_category_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_domain_status_and_category", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_domain_status_and_category_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaDomainStatusAndCategory:
    """ Tests for the umbrella_domain_status_and_category function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("a193c91a-66fa-43f1-a67c-3f080f51f894, fbf6a1a1-31a2-4ff4-ad53-3756657c841f, e5fdd9e4-3dfe-471d-8677-75242b78dc55, expected_results", [
        ("text", True, 'categorization', {"value": "xyz"}),
        ("text", True, 'categorization', {"value": "xyz"})
    ])
    def test_success(self, circuits_app, a193c91a-66fa-43f1-a67c-3f080f51f894, fbf6a1a1-31a2-4ff4-ad53-3756657c841f, e5fdd9e4-3dfe-471d-8677-75242b78dc55, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "a193c91a-66fa-43f1-a67c-3f080f51f894": a193c91a-66fa-43f1-a67c-3f080f51f894,
            "fbf6a1a1-31a2-4ff4-ad53-3756657c841f": fbf6a1a1-31a2-4ff4-ad53-3756657c841f,
            "e5fdd9e4-3dfe-471d-8677-75242b78dc55": e5fdd9e4-3dfe-471d-8677-75242b78dc55
        }
        results = call_umbrella_domain_status_and_category_function(circuits_app, function_params)
        assert(expected_results == results)