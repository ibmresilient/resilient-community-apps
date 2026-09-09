# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_kafka"
FUNCTION_NAME = "kafka_send"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the IBM SOAR REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_kafka_send_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("kafka_send", function_params)

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
        event = circuits.watcher.wait("kafka_send_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestKafkaSend:
    """ Tests for the kafka_send function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "kafka_broker_label": "brokerA",
        "kafka_message": "sample text",
        "kafka_topic": "sample_topic"
    }
    expected_results_1 = {"value": None}

    mock_inputs_2 = {
        "kafka_broker_label": "brokerA",
        "kafka_message": "sample text",
        "kafka_topic": "sample_topic",
        "kafka_key": "a"
    }
    expected_results_2 = {"value": None}

    mock_inputs_3 = {
        "kafka_broker_label": "brokerA",
        "kafka_message": {"unicode": "Ա Բ Գ Դ Ե Զ Է Ը Թ Ժ Ի Լ"},
        "kafka_topic": "sample_unicode",
        "kafka_key": "sample_ԷԸԹԺ"
    }
    expected_results_3 = {"value": None}

    @pytest.mark.livetest
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2),
        (mock_inputs_3, expected_results_3)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_kafka_send_function(circuits_app, mock_inputs)
        assert(expected_results == results)
