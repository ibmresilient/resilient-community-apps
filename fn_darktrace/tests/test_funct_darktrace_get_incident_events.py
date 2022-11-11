# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from unittest.mock import patch

import pytest
from resilient_circuits import FunctionResult, SubmitTestFunction
from resilient_circuits.util import get_function_definition

from .test_app_common import (PATH_AIANALYST_INCIDENTEVENTS_MOCK,
                              PATH_MODELBREACHES_MOCK, load_json)

PACKAGE_NAME = "fn_darktrace"
FUNCTION_NAME = "darktrace_get_incident_events"

# Read the default configuration-data section from the package
config_data = """[fn_darktrace]
api_key=abcd-efgh
api_secret=1234-abcd-56789-efgh
instance_url=https://fake.cloud.darktrace.com
"""

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_darktrace_get_incident_events_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("darktrace_get_incident_events", function_params)

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
        event = circuits.watcher.wait("darktrace_get_incident_events_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestDarktraceGetIncidentEvents:
    """ Tests for the darktrace_get_incident_events function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "darktrace_incident_group_id": "sample text",
        "darktrace_include_model_breach_data": True
    }

    expected_results_1 = {
        "incident_events": load_json(PATH_AIANALYST_INCIDENTEVENTS_MOCK),
        "base_model_breach_url": "https://fake.cloud.darktrace.com/#modelbreach/"
    }
    # have to add in the model breaches data
    expected_results_1["incident_events"][0]["relatedBreaches"][0].update(load_json(PATH_MODELBREACHES_MOCK))

    mock_inputs_2 = {
        "darktrace_incident_group_id": "sample text",
        "darktrace_include_model_breach_data": False
    }

    expected_results_2 = {
        "incident_events": load_json(PATH_AIANALYST_INCIDENTEVENTS_MOCK),
        "base_model_breach_url": "https://fake.cloud.darktrace.com/#modelbreach/"
    }

    @patch("fn_darktrace.components.funct_darktrace_list_similar_devices.AppCommon.get_incident_events")
    @patch("fn_darktrace.components.funct_darktrace_list_similar_devices.AppCommon.get_model_breaches")
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, patch_get_model_breaches, patch_get_incident_events, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """


        patch_get_model_breaches.return_value = load_json(PATH_MODELBREACHES_MOCK)
        patch_get_incident_events.return_value = load_json(PATH_AIANALYST_INCIDENTEVENTS_MOCK)

        results = call_darktrace_get_incident_events_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content"))
        if mock_inputs.get("darktrace_include_model_breach_data", True):
            assert patch_get_model_breaches.called
        else:
            assert not patch_get_model_breaches.called
