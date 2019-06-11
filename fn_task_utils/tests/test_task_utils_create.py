"""Tests using pytest_resilient_circuits"""
# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

from __future__ import print_function, unicode_literals
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

def call_task_utils_create_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("task_utils_create", function_params)
    circuits.manager.fire(evt)
    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

        # else return the FunctionComponent's results
    else:
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

    @pytest.mark.parametrize("incident_id, task_name, task_utils_payload", [
        (123, "New Task Name", {"type": "text", "content": '{\n"required": false\n}'}),
        (123, "My New Task", {"type": "text", "content": '{\n"required": false\n}'})
    ])
    def test_success(self, circuits_app, incident_id, task_name, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_name": task_name,
            "task_utils_payload": task_utils_payload
        }
        results = call_task_utils_create_function(circuits_app, function_params)
        assert(results["content"]["task"])

    @pytest.mark.parametrize("incident_id, task_name, task_utils_payload", [
        (123, "Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ", {"type": "text", "content": '{\n"required": false\n}'}),
        (123, " Й К Л М Н О П Р С Т ", {"type": "text", "content": '{\n"required": false\n}'})
    ])
    def test_success_unicode(self, circuits_app, incident_id, task_name, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_name": task_name,
            "task_utils_payload": task_utils_payload
        }
        results = call_task_utils_create_function(circuits_app, function_params)
        assert (results["content"]["task"])
        assert function_params["task_name"] == results["content"]["task"]["name"]

    @pytest.mark.parametrize("incident_id, task_name, task_utils_payload", [
        (123, "text", {"type": "text", "content": '{\n"required": false\n}'}),
    ])
    def test_owner_as_email_user(self, circuits_app, incident_id, task_name, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_name": task_name,
            "task_utils_payload": task_utils_payload
        }
        results = call_task_utils_create_function(circuits_app, function_params)
        assert (results["content"]["task"])

    @pytest.mark.parametrize("incident_id, task_name, task_utils_payload", [
        (123, "text", {"type": "text", "content": '{\n"required": false\n}'}),
        (123, "text", {"type": "text", "content": '{\n"required": false\n}'})
    ])
    def test_owner_as_user_id(self, circuits_app, incident_id, task_name, task_utils_payload):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_name": task_name,
            "task_utils_payload": task_utils_payload
        }
        results = call_task_utils_create_function(circuits_app, function_params)
        assert results["content"]["task"]

