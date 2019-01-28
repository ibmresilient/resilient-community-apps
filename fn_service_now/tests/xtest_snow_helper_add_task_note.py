# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_service_now"
FUNCTION_NAME = "snow_helper_add_task_note"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_snow_helper_add_task_note_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("snow_helper_add_task_note", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("snow_helper_add_task_note_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestSnowHelperAddTaskNote:
    """ Tests for the snow_helper_add_task_note function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("task_id, sn_note_text, expected_results", [
        (123, "text", {"value": "xyz"}),
        (123, "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, task_id, sn_note_text, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "task_id": task_id,
            "sn_note_text": sn_note_text
        }
        results = call_snow_helper_add_task_note_function(circuits_app, function_params)
        assert(expected_results == results)