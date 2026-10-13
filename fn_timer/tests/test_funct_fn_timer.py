# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
import time
from .mock_workflow_status import WorkflowStatus
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
try:
    from unittest.mock import patch, Mock, MagicMock
except:
    from mock import patch, Mock, MagicMock

PACKAGE_NAME = "fn_timer"
FUNCTION_NAME = "fn_timer"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_timer_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_timer", function_params)

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
        event = circuits.watcher.wait("fn_timer_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnTimer:
    """ Tests for the fn_timer function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "timer_epoch": int(time.time()) + 15,
        "timer_time": None
    }

    expected_results = True

    mock_inputs_2 = {
        "timer_epoch": None,
        "timer_time": "15s"
    }

    mock_inputs_3 = {
        "timer_epoch": 1518367008000,
        "timer_time": "15s"
    }

    @patch('fn_timer.components.funct_fn_timer.get_workflow_status')
    @patch('fn_timer.components.funct_fn_timer.get_sleep_time_from_epoch')
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results)
    ])
    def test_success_epoch(self, mock_sleep_time, mock_workflow_status, circuits_app ,mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        mock_sleep_time.return_value = 2
        mock_workflow_status.return_value = WorkflowStatus()
        results = call_fn_timer_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("success"))

    @patch('fn_timer.components.funct_fn_timer.get_workflow_status')
    @patch('fn_timer.components.funct_fn_timer.get_sleep_time_in_seconds')
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_2, expected_results)
    ])
    def test_success_time(self, mock_sleep_time, mock_workflow_status, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        mock_sleep_time.return_value = 2
        mock_workflow_status.return_value = WorkflowStatus()
        results = call_fn_timer_function(circuits_app, mock_inputs)
        assert(expected_results == results.get("success"))

    @pytest.mark.parametrize("mock_inputs", [
    (mock_inputs_3)
    ])
    def test_error(self, circuits_app, mock_inputs):
        """ Test calling with sample values for the parameters """
        try:
            results = call_fn_timer_function(circuits_app, mock_inputs)
            assert False
        except:
            assert True