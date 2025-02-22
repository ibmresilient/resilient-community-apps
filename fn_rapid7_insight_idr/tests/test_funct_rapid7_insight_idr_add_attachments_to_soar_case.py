# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.0.1.486
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_rapid7_insight_idr"
FUNCTION_NAME = "rapid7_insight_idr_add_attachments_to_soar_case"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_rapid7_insight_idr_add_attachments_to_soar_case_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("rapid7_insight_idr_add_attachments_to_soar_case", function_params)

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
        event = circuits.watcher.wait("rapid7_insight_idr_add_attachments_to_soar_case_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestRapid7InsightIdrAddAttachmentsToSoarCase:
    """ Tests for the rapid7_insight_idr_add_attachments_to_soar_case function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "rapid7_insight_idr_rrn": "rrn:investigation:us2:e4463fba-cd64-427c-8fc9-f9e1983f24e1:investigation:27R6OYMKZRB9",
        "rapid7_insight_idr_incident_id": 2298
    }

    expected_results_1 = {"rapid7_insight_idr_attachments": []}

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_rapid7_insight_idr_add_attachments_to_soar_case_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content", {}))
