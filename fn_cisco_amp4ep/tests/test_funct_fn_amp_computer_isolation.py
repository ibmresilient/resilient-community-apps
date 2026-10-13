# -*- coding: utf-8 -*-
# Generated with resilient-sdk v52.0.0.0.927
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from resilient_lib import IntegrationError
from mock_artifacts import get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_computer_isolation"

# Read the default configuration-data section from the package
# config_data = get_config_data(PACKAGE_NAME)
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_amp_computer_isolation_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_amp_computer_isolation", function_params)

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
        event = circuits.watcher.wait("fn_amp_computer_isolation_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestAmpComputerIsolation:
    """ Tests for the fn_amp_computer_isolation function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "amp_computer_isolation": "Isolate",
        "amp_conn_guid": "abcdefg"
    }

    expected_called_with_1 = {
        "amp_conn_guid": "abcdefg",
        "isolation_method": "PUT"
    }

    mock_inputs_2 = {
        "amp_computer_isolation": "De-Isolate",
        "amp_conn_guid": "abcdefg"
    }

    expected_called_with_2 = {
        "amp_conn_guid": "abcdefg",
        "isolation_method": "DELETE"
    }

    mock_inputs_3 = {
        "amp_computer_isolation": "Refresh",
        "amp_conn_guid": "abcdefg"
    }

    expected_called_with_3 = {
        "amp_conn_guid": "abcdefg",
        "isolation_method": "GET"
    }

    mock_inputs_4 = {
        "amp_computer_isolation": "nothing",
        "amp_conn_guid": "abcdefg"
    }

    @pytest.mark.parametrize("mock_inputs, expected_called_with", [
        (mock_inputs_1, expected_called_with_1),
        (mock_inputs_2, expected_called_with_2),
        (mock_inputs_3, expected_called_with_3)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_called_with):
        """ Test calling with sample values for the parameters """
        with patch("fn_cisco_amp4ep.components.funct_fn_amp_computer_isolation.Ampclient.manage_isolations") as mock_amp_client:
            mock_amp_client.return_value = {"test": "response"}

            results = call_amp_computer_isolation_function(circuits_app, mock_inputs)
            mock_amp_client.assert_called_with(expected_called_with["amp_conn_guid"],
                                               method=expected_called_with["isolation_method"])

    @pytest.mark.parametrize("mock_inputs", [
        (mock_inputs_4)
    ])
    def test_failure(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """
        with patch("fn_cisco_amp4ep.components.funct_fn_amp_computer_isolation.Ampclient.manage_isolations") as mock_amp_client:
            with pytest.raises(IntegrationError) as interror:
                mock_amp_client.return_value = {"test": "response"}
                results = call_amp_computer_isolation_function(circuits_app, mock_inputs)
            assert "Invalid request" in interror.value.value
