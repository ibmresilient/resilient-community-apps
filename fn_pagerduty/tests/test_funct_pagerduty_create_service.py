# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.1.824
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_pagerduty"
FUNCTION_NAME = "pagerduty_create_service"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_pagerduty_create_service_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("pagerduty_create_service", function_params)

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
        event = circuits.watcher.wait("pagerduty_create_service_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestPagerdutyCreateService:
    """ Tests for the pagerduty_create_service function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "pd_description": "something ",
        "pd_escalation_policy": " testService1-ep",
        "pd_title": "test1"
    }

    expected_results_1 = { "pd": helper.mock_create_service() }

    @patch("fn_pagerduty.components.funct_pagerduty_create_service.PDClient", helper.MockClient)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_pagerduty_create_service_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content"))
