# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from mock import patch
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import mocked_aws_sns

PACKAGE_NAME = "fn_aws_utilities"
FUNCTION_NAME = "fn_send_sms_via_sns"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_send_sms_via_sns_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_send_sms_via_sns", function_params)

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
        event = circuits.watcher.wait("fn_send_sms_via_sns_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnSendSmsViaSns:
    """ Tests for the fn_send_sms_via_sns function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "msg_body": "This is a sample text message",
        "phone_numbers": " 1234567890  "
    }

    expected_results_1 = {"message_id": "0000"}

    mock_inputs_2 = {
        "msg_body": "This is another sample text message",
        "phone_numbers": "(123) 456-7890"
    }

    expected_results_2 = {"message_id": "0000"}

    mock_inputs_3 = {
        "msg_body": "This is another sample text message",
        "phone_numbers": " 1 2 3 4 5 6 7 8 9 0 "
    }

    expected_results_3 = {"message_id": "0000"}

    @patch("fn_aws_utilities.components.fn_send_sms_via_sns.AwsSns", side_effect=mocked_aws_sns)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3)
    ])
    def test_success(self, mock_aws_sns, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_send_sms_via_sns_function(circuits_app, mock_inputs)
        assert(expected_results == results)
