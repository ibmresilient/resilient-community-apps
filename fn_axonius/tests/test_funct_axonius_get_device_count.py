# -*- coding: utf-8 -*-
# Generated with resilient-sdk v51.0.1.0.695
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_axonius"
FUNCTION_NAME = "axonius_get_device_count"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_axonius_get_device_count_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("axonius_get_device_count", function_params)

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
        event = circuits.watcher.wait("axonius_get_device_count_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestAxoniusGetDeviceCount:
    """ Tests for the axonius_get_device_count function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "axonius_query_string": "(\"specific_data.data.os.type\" == \"Windows\")",
        "axonius_saved_query_name": None
    }

    expected_results_1 = {"value": 1050}

    mock_inputs_2 = {
        "axonius_query_string": None,
        "axonius_saved_query_name": "Shirley"
    }

    expected_results_2 = {"value": 10}

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_axonius_get_device_count_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("content"))
