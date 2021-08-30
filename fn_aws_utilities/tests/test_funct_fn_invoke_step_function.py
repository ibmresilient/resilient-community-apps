# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from fn_aws_utilities.util.aws_step_function_api import AwsStepFunction
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from tests.mock_artifacts import mock_constants, mocked_aws_step_function

PACKAGE_NAME = "fn_aws_utilities"
FUNCTION_NAME = "fn_invoke_step_function"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_invoke_step_function_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_invoke_step_function", function_params)

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
        event = circuits.watcher.wait("fn_invoke_step_function_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnInvokeStepFunction:
    """ Tests for the fn_invoke_step_function function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "state_machine_async": True,
        "state_machine_name": "0000",
        "state_machine_payload": "\{\"test\": \"test_val\"\}"
    }

    expected_results_1 = {
        "startDate": mock_constants.get("DATE_TIME_MOCK_OBJ").strftime("%Y-%m-%d %H:%M:%S"),
        "stopDate": mock_constants.get("DATE_TIME_MOCK_OBJ").strftime("%Y-%m-%d %H:%M:%S")
    }

    mock_inputs_2 = {
        "state_machine_async": True,
        "state_machine_name": "1111",
        "state_machine_payload": "\{\"test\": \"test_val\"\}"
    }

    expected_results_2 = {
        "startDate": mock_constants.get("DATE_TIME_MOCK_OBJ").strftime("%Y-%m-%d %H:%M:%S"),
        "stopDate": None
    }

    @patch("fn_aws_utilities.components.fn_invoke_step_function.AwsStepFunction", side_effect=mocked_aws_step_function)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, mock_aws_step_function, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_invoke_step_function_function(circuits_app, mock_inputs)
        assert(expected_results == results)
