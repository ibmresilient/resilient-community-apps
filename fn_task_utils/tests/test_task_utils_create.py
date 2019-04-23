"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import TasksResilientMock

PACKAGE_NAME = "fn_task_utils"
FUNCTION_NAME = "task_utils_create"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = TasksResilientMock
import json
mock_task = json.dumps({
              "task_name": "test"
})

def call_task_utils_create_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("task_utils_create", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("task_utils_create_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestTskUtilsCreate:
    """ Tests for the tsk_utils_create function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None


    @pytest.mark.parametrize("incident_id, task_name, task_utils_payload, expected_results", [
        (123, "text", {"type": "text", "content": mock_task}, {"value": "xyz"}),
        (123, "text", {"type": "text", "content": mock_task}, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incident_id, task_name, task_utils_payload, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_name": task_name,
            "task_utils_payload": task_utils_payload
        }
        pytest.skip("Not Implemented")
        results = call_task_utils_create_function(circuits_app, function_params)
        assert(results["content"]["task_id"])

