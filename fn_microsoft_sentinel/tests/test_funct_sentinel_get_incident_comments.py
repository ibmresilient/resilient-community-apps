# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.0.2.575
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch
import pytest, helper
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

FUNCTION_NAME = "sentinel_get_incident_comments"

# Read the default configuration-data section from the package
config_data = helper.config_data

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_sentinel_get_incident_comments_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("sentinel_get_incident_comments", function_params)

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
        event = circuits.watcher.wait("sentinel_get_incident_comments_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSentinelGetIncidentComments:
    """ Tests for the sentinel_get_incident_comments function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(helper.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "sentinel_profile": "profile_a",
        "sentinel_incident_id": "6c98642b-7248-4b4d-994e-32443f100e78",
        "incident_id": 2178
    }

    expected_results_1 = helper.get_incident_comments_results()

    @patch("fn_microsoft_sentinel.components.funct_sentinel_get_incident_comments.SentinelAPI", helper.MockClient)
    @patch("fn_microsoft_sentinel.components.funct_sentinel_get_incident_comments.ResilientCommon", helper.MockSOAR)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_sentinel_get_incident_comments_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content", {}))
