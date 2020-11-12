# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.
# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_incident import IncidentMock

PACKAGE_NAME = "fn_incident_utils"
FUNCTION_NAME = "incident_utils_close_incident"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = IncidentMock


def call_incident_utils_close_incident_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("incident_utils_close_incident", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("incident_utils_close_incident_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestIncidentUtilsCloseIncident:
    """ Tests for the incident_utils_close_incident function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    inputs = {
        "incident_id": 123,
        "close_fields": "{\"resolution_id\":9,\"resolution_summary\":\"resolved\"}"
    }

    output = {
        "id": 123,
        "resolution_summary": "<div class=\"rte\"><div>resolved</div></div>",
        "plan_status": "C",
        "vers": 5
    }

    @pytest.mark.parametrize("inputs, expected_results", [(inputs, output)])
    def test_success(self, circuits_app, inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_incident_utils_close_incident_function(circuits_app, inputs)
        assert(expected_results == results)
