# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mxtoolbox"
FUNCTION_NAME = "fn_mxtoolbox"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_mxtoolbox_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_mxtoolbox", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_mxtoolbox_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnMxtoolbox:
    """ Tests for the fn_mxtoolbox function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "mx_param1": None,
        "mx_command": "mx",
        "mx_argument": "abc.com"
    }

    expected_results_value = {"Information": [{'IP Address': "104.47.44.36",
                                               'Hostname': "abc-com.mail.protection.outlook.com"}]
                              }

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results_value", [
        (mock_inputs_1, expected_results_value)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results_value):
        """ Test calling with sample values for the parameters """
        results = call_fn_mxtoolbox_function(circuits_app, mock_inputs)
        results_value = results.get("value")
        results_information = results_value.get("Information")
        results_hostname = results_information[0].get("Hostname")
        results_ip = results_information[0].get("IP Address")
        expected_results_information = expected_results_value.get("Information")
        expected_results_hostname = expected_results_information[0].get("Hostname")
        expected_results_ip = expected_results_information[0].get("IP Address")
        assert(expected_results_ip == results_ip)
        assert(expected_results_hostname == results_hostname)
