# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
import json
from mock import patch
from mocks import remedy_dt_mock, remedy_mock


""" 
Depends on v41 of pytest-resilient-circuits where a mock
task GET endpoint was added to the appliance.
"""

PACKAGE_NAME = "fn_remedy"
FUNCTION_NAME = "remedy_close_incident"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

remedy_side_effect = [
    remedy_mock.mock_init()
]

remedy_dt_side_effect = [
    remedy_dt_mock.mock_init(),
    remedy_dt_mock.mock_init()
]


def call_remedy_close_incident_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("remedy_close_incident", function_params)

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
        event = circuits.watcher.wait("remedy_close_incident_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestRemedyCloseIncident:
    """ Tests for the remedy_close_incident function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    content = {
        "values": {                                               
            "Description" : "Rest API: Resolve Incident using RestAPI",                                               
            "Status" : "Resolved",                                               
            "Status_Reason" : "Future Enhancement",                                               
            "Resolution" : "Test Resolution Text"
        }
    }

    mock_inputs_1 = {
        "remedy_payload": json.dumps(content),
        "task_id": 1,
        "incident_id": 2
    }

    # @patch("fn_remedy.lib.remedy.RemedyAPIClient.RemedyClient", side_effect=remedy_mock)
    @patch("fn_remedy.components.funct_remedy_close_incident.RemedyClient", side_effect=remedy_side_effect)
    @patch("fn_remedy.components.funct_remedy_close_incident.Datatable", side_effect=remedy_dt_side_effect)
    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs", [
        (mock_inputs_1)
    ])
    def test_success(self, remedy_mock, remedy_dt_mock, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_remedy_close_incident_function(circuits_app, mock_inputs)
        assert(results["success"])
        assert(results["content"]["closed"])
