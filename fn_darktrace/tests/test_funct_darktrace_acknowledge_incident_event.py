# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_function_definition

PACKAGE_NAME = "fn_darktrace"
FUNCTION_NAME = "darktrace_acknowledge_incident_event"

# Read the default configuration-data section from the package
config_data = """[fn_darktrace]
api_key=abcd-efgh
api_secret=1234-abcd-56789-efgh
instance_url=https://fake.cloud.darktrace.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_darktrace_acknowledge_incident_event_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("darktrace_acknowledge_incident_event", function_params)

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
        event = circuits.watcher.wait("darktrace_acknowledge_incident_event_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDarktraceAcknowledgeIncidentEvent:
    """ Tests for the darktrace_acknowledge_incident_event function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "darktrace_incident_event_id": "1234"
    }

    expected_results_1 = {"aianalyst": "SUCCESS"}

    mock_inputs_2 = {
        "darktrace_incident_event_id": "already_acknowledged"
    }

    expected_results_2 = {"aianalyst": "ERROR"}

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_darktrace.components.funct_darktrace_acknowledge_incident_event.AppCommon.acknowledge_incident_event") as patch_ack:
            patch_ack.return_value = expected_results
            results = call_darktrace_acknowledge_incident_event_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
            patch_ack.assert_called
            patch_ack.assert_called_with(mock_inputs.get("darktrace_incident_event_id"))
