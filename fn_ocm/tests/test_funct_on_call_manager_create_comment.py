# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.5.0.1475
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from helper import get_mock_config_data, PACKAGE_NAME, create_comment
from mock import patch

FUNCTION_NAME = "on_call_manager_create_comment"

# Read the default configuration-data section from the package
config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_on_call_manager_create_comment_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("on_call_manager_create_comment", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("on_call_manager_create_comment_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestOnCallManagerCreateComment:
    """ Tests for the on_call_manager_create_comment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "ocm_comment_author": "john.doe@example.com",
        "ocm_incident_id": "1234",
        "ocm_incident_comment": "Hello World"
    }

    expected_results_1 = {}

    @patch('fn_ocm.util.helper.ocm_client.create_comment', create_comment)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_on_call_manager_create_comment_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content", {}))
