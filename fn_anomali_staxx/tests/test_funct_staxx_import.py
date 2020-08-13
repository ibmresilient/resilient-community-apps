# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_anomali_staxx"
FUNCTION_NAME = "staxx_import"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_send_to_staxx_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        if len(exception.args) > 1:
            exception = exception.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait(FUNCTION_NAME + "_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSendToStaxx:
    """ Tests for the send_to_staxx function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "staxx_severity": "low",
        "staxx_confidence": '34',
        "staxx_indicator_type": "adware",
        "staxx_tlp": "RED",
        "staxx_indicator": "12.32.12.22",
        "staxx_auto_approve": "yes"
    }

    mock_inputs_2 = {
        "staxx_severity": "high",
        "staxx_confidence": '55',
        "staxx_indicator_type": "ddos",
        "staxx_tlp": "GREEN",
        "staxx_indicator": "abc.com",
        "staxx_auto_approve": "yes"
    }

    failure_inputs = {
        "staxx_severity": "high",
        "staxx_confidence": 'bad',
        "staxx_indicator_type": "ddos",
        "staxx_tlp": "GREEN",
        "staxx_indicator": "abc.com",
        "staxx_auto_approve": "yes"
    }


    @pytest.mark.parametrize("mock_inputs", [
        (mock_inputs_1),
        (mock_inputs_2)
    ])
    def test_success(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """

        results = call_send_to_staxx_function(circuits_app, mock_inputs)
        assert(results.get('content').startswith("Import intelligence job ID"))

    @pytest.mark.parametrize("mock_inputs", [
        (failure_inputs)
    ])
    def test_failure(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """
        with pytest.raises(ValueError):
            results = call_send_to_staxx_function(circuits_app, mock_inputs)
