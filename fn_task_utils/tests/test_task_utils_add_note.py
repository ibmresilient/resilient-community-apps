# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_task_utils"
FUNCTION_NAME = "task_utils_add_note"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_task_utils_add_note_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("task_utils_add_note", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("task_utils_add_note_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestTaskUtilsAddNote:
    """ Tests for the task_utils_add_note function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("task_id, task_utils_note_type, task_utils_note_body, expected_results", [
        (123, 'text', "text", {"value": "xyz"}),
        (123, 'html', "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, task_id, task_utils_note_type, task_utils_note_body, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "task_id": task_id,
            "task_utils_note_type": task_utils_note_type,
            "task_utils_note_body": task_utils_note_body
        }
        pytest.skip("Not Implemented")
        results = call_task_utils_add_note_function(circuits_app, function_params)
        assert(expected_results == results)