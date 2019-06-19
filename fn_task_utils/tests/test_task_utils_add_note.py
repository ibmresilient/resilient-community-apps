# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function, unicode_literals
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import TasksResilientMock


PACKAGE_NAME = "fn_task_utils"
FUNCTION_NAME = "task_utils_add_note"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = TasksResilientMock


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

    @pytest.mark.parametrize("incident_id, task_id, task_utils_note_type, task_utils_note_body", [
        (2096, 123, 'text', "Progress made on Task."),
        (2097, 123, 'html', "Task overdue for closure, provide progress report")
    ])
    def test_notes_are_present(self, circuits_app, incident_id, task_id, task_utils_note_type, task_utils_note_body):
        """ Test adding a note to a Task and then check if the response sent contains at least 1 task note. """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_utils_note_type": task_utils_note_type,
            "task_utils_note_body": task_utils_note_body
        }
        results = call_task_utils_add_note_function(circuits_app, function_params)
        # Assert there is at least one task note
        assert len(results["content"]["task_note"])

    @pytest.mark.parametrize("incident_id, task_id, task_utils_note_type, task_utils_note_body", [
        (2096, 123, 'text', "Progress made on Task."),
        (2097, 123, 'html', "Task overdue for closure, provide progress report")
    ])
    def test_last_note_is_added_note(self, circuits_app, incident_id, task_id, task_utils_note_type, task_utils_note_body):
        """ Test adding a note to a Task and then check if the response sent contains at least 1 task note. """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_utils_note_type": task_utils_note_type,
            "task_utils_note_body": task_utils_note_body
        }
        results = call_task_utils_add_note_function(circuits_app, function_params)

        newest_task_note = results["content"]["task_note"]
        assert newest_task_note
        assert task_utils_note_body in newest_task_note["text"]["content"]

    @pytest.mark.parametrize("incident_id, task_id, task_utils_note_type, task_utils_note_body", [
        (2096, 123, 'text', "Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ"),
        (2097, 123, 'html', " Й К Л М Н О П Р С Т ")
    ])
    def test_notes_with_unicode_text(self, circuits_app, incident_id, task_id, task_utils_note_type, task_utils_note_body):
        """ Test adding a note to a Task and then check if the response sent contains at least 1 task note. """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_utils_note_type": task_utils_note_type,
            "task_utils_note_body": task_utils_note_body
        }
        results = call_task_utils_add_note_function(circuits_app, function_params)

        newest_task_note = results["content"]["task_note"]

        assert newest_task_note
        assert task_utils_note_body in newest_task_note["text"]["content"]
