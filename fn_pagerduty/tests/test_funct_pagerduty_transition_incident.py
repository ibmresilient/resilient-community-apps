# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.1.824
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_pagerduty"
FUNCTION_NAME = "pagerduty_transition_incident"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_pagerduty_transition_incident_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("pagerduty_transition_incident", function_params)

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
        event = circuits.watcher.wait("pagerduty_transition_incident_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestPagerdutyTransitionIncident:
    """ Tests for the pagerduty_transition_incident function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func

    mock_inputs_1 = {
        "pd_incident_id": "Q06KVFVBOFHPI7",
        "pd_priority": "p2",
        "pd_description": "<div class=\"rte\"><div>test</div></div>",
        "pd_status": "resolved",
        "pd_severity": "low"
    }

    expected_results_1 = helper.mock_update_incident()

    @patch("fn_pagerduty.components.funct_pagerduty_transition_incident.PDClient", helper.MockClient)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_pagerduty_transition_incident_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content", {}))
