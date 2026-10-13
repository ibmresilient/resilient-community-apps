# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import json
from mock import patch
import os
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from fn_hibp.lib.common import Hibp

PACKAGE_NAME = "fn_hibp"
FUNCTION_NAME = "have_i_been_pwned_get_breaches"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_have_i_been_pwned_get_breaches_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("have_i_been_pwned_get_breaches", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    event = circuits.watcher.wait("have_i_been_pwned_get_breaches_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def call_have_i_been_pwned_get_pastes_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("have_i_been_pwned_get_pastes", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    event = circuits.watcher.wait("have_i_been_pwned_get_pastes_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

def get_mock_data(file_name):
    test_dir = os.path.dirname(__file__)
    file_path = os.path.join(test_dir, "mock_data/{}".format(file_name))
    with open(file_path) as f:
        result = json.load(f)
    return result

class TestHaveIBeenPwnedGetBreaches:
    """ Tests for the have_i_been_pwned_get_breaches function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "email_address": "test@example.com"
    }
    expected_results_1 = get_mock_data("breaches.json")

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    @patch.object(Hibp, 'execute_call')
    def test_breaches_success(self, mock_method, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        mock_method.return_value = expected_results

        results = call_have_i_been_pwned_get_breaches_function(circuits_app, mock_inputs)
        assert expected_results == results['content'].get('Breaches', None)

    mock_inputs_2 = {
        "email_address": "test@example.com"
    }
    expected_results_2 = get_mock_data("pastes.json")

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_2, expected_results_2)
    ])
    @patch.object(Hibp, 'execute_call')
    def test_pastes(self, mock_method, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        mock_method.return_value = expected_results

        results = call_have_i_been_pwned_get_pastes_function(circuits_app, mock_inputs)
        assert expected_results == results['content'].get('Pastes', None)
