# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import mocked_aws_lambda

PACKAGE_NAME = "fn_aws_utilities"
FUNCTION_NAME = "fn_invoke_lambda"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_invoke_lambda_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_invoke_lambda", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=evt, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_invoke_lambda_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnInvokeLambda:
    """ Tests for the fn_invoke_lambda function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    # test if handles sum two ints
    mock_inputs_1 = {
        "lambda_payload": {"x": 1, "y": 2},
        "lambda_function_name": "two_int_sum"
    }

    expected_results_1 = '3'

    # test if handles strings the same as ints
    mock_inputs_2 = {
        "lambda_payload": {"x": "1", "y": "2"},
        "lambda_function_name": "two_int_sum"
    }

    expected_results_2 = '3'

    mock_inputs_3 = {
        "lambda_payload": {"str1": "two", "str2": "words"},
        "lambda_function_name": "concat_strings"
    }

    expected_results_3 = "twowords"

    @patch("fn_aws_utilities.components.fn_invoke_lambda.AWSLambda", side_effect=mocked_aws_lambda)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3)
    ])
    def test_success(self, mock_aws_lambda, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_invoke_lambda_function(circuits_app, mock_inputs).get("response_payload")
        assert(expected_results == results)
