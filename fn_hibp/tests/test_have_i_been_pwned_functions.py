# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_hibp"
FUNCTION_NAME = "have_i_been_pwned_get_breaches"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_have_i_been_pwned_get_breaches_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("have_i_been_pwned_get_breaches", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("have_i_been_pwned_get_breaches_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def call_have_i_been_pwned_get_pastes_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("have_i_been_pwned_get_pastes", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("have_i_been_pwned_get_pastes_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestHaveIBeenPwnedGetBreaches:
    """ Tests for the have_i_been_pwned_get_breaches function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("email_address, expected_results", [
        ("test@email.com", {"Inputs": {"email_address": "test@email.com"}, "Breaches": 46}),
        ("safe@email2.com", {"Inputs": {"email_address": "safe@email2.com"}, "Breaches": None})
    ])
    def test_breaches(self, circuits_app, email_address, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "email_address": email_address
        }
        results = call_have_i_been_pwned_get_breaches_function(circuits_app, function_params)

        assert(expected_results.get("Inputs") == results.get("Inputs"))
        if not results.get("Breaches"):
            assert results.get("Breaches") is None
        else:
            assert(expected_results.get("Breaches") == len(results.get("Breaches")))

    @pytest.mark.parametrize("email_address, expected_results", [
        ("test@email.com", {"Inputs": {"email_address": "test@email.com"}, "Pastes": 32}),
        ("safe@email2.com", {"Inputs": {"email_address": "safe@email2.com"}, "Pastes": None})
    ])
    def test_pastes(self, circuits_app, email_address, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "email_address": email_address
        }
        results = call_have_i_been_pwned_get_breaches_function(circuits_app, function_params)

        assert(expected_results.get("Inputs") == results.get("Inputs"))
        if not results.get("Pastes"):
            assert results.get("Pastes") is None
        else:
            assert(expected_results.get("Pastes") == len(results.get("Pastes")))