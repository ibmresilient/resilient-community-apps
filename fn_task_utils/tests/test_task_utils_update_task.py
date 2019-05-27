# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import TasksResilientMock


PACKAGE_NAME = "fn_task_utils"
FUNCTION_NAME = "task_utils_update_task"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = TasksResilientMock


def call_task_utils_update_task_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("task_utils_update_task", function_params)
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

        # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("task_utils_update_task_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestTaskUtilsUpdateTask:
    """ Tests for the task_utils_update_task function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, task_id, task_utils_payload", [
        (2096, 123, {"type": "text", "content": '{\n"required": false\n}'}),
        (2097, 123, {"type": "text", "content": '{\n"required": true\n}'})
    ])
    def test_success(self, circuits_app, incident_id, task_id, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_utils_payload": task_utils_payload
        }
        results = call_task_utils_update_task_function(circuits_app, function_params)
        assert(task_id == results["content"]["task_id"])

    @pytest.mark.parametrize("incident_id, task_id, task_utils_payload", [
        (2096, 123, {"type": "text", "content": '{\n"required": false\n}'}),
        (2097, 444, {"type": "text", "content": '{\n"required": true\n}'})
    ])
    def test_modifying_required(self, circuits_app, incident_id, task_id, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_utils_payload": task_utils_payload
        }
        results = call_task_utils_update_task_function(circuits_app, function_params)

        assert (results["content"]["task"]["required"] in (True, False))  # Assert required is either True or False
        # Assert the new value of required matches our provided one
        assert str(results["content"]["task"]["required"]).lower() in task_utils_payload["content"]

    @pytest.mark.parametrize("incident_id, task_id, task_utils_payload", [
        (2096, 9999, {"type": "text", "content": '{\n"required": true\n}'})
    ])
    def test_failure_not_found(self, circuits_app, incident_id, task_id, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_utils_payload": task_utils_payload
        }
        with pytest.raises(ValueError) as err:
            call_task_utils_update_task_function(circuits_app, function_params)

            assert u"Unable to find object with ID" in err.value.args[0]

