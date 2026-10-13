# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import json
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests.mock_incident import IncidentMock

PACKAGE_NAME = "fn_soar_utils"
FUNCTION_NAME = "soar_utils_search_incidents"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = IncidentMock

def call_soar_utils_search_incidents_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("soar_utils_search_incidents", function_params)

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
        event = circuits.watcher.wait("soar_utils_search_incidents_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSoarUtilsSearchIncidents:
    """ Tests for the soar_utils_search_incidents function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "soar_utils_filter_conditions": json.dumps(
            [
                {"field_name":"name", "method":"contains", "value":"sample"},
                {"field_name":"create_date", "method":"gte", "value":1621111014529}
            ]
        ),
        "soar_utils_sort_fields": None
    }

    mock_inputs_2 = {
        "soar_utils_filter_conditions": None,
        "soar_utils_sort_fields": json.dumps(
            [
                {"field_name":"discovered_date", "type": "asc"}
            ]
        )
    }

    @pytest.mark.parametrize("mock_inputs", [
        (mock_inputs_1),
        (mock_inputs_2)
    ])
    def test_success(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_soar_utils_search_incidents_function(circuits_app, mock_inputs)
        assert(results.get("inputs").get("soar_utils_filter_conditions") == mock_inputs.get("soar_utils_filter_conditions"))