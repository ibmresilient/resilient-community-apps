# -*- coding: utf-8 -*-
# Copyright © IBM Corporation 2010, 2019

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function, unicode_literals
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import TasksResilientMock

PACKAGE_NAME = "fn_task_utils"
FUNCTION_NAME = "task_utils_close_task"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = TasksResilientMock


def call_task_utils_close_task_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("task_utils_close_task", function_params)
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None)

    if exception_event is not False:
        exception = exception_event.args[1].args[1]
        raise exception

        # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("task_utils_close_task_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestTaskUtilsCloseTask:
    """ Tests for the task_utils_close_task function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.mock_test
    @pytest.mark.parametrize("incident_id, task_id, task_name, expected_results", [
        (2096, 2251301, "text", {"task_id": 2251301}),
        (2096, 2251301, "text", {"task_id": 2251301})
    ])
    def test_close_task_success(self, circuits_app, incident_id, task_id, task_name, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_name": task_name
        }
        results = call_task_utils_close_task_function(circuits_app, function_params)
        assert(expected_results["task_id"] == results["content"]["task_id"])

    @pytest.mark.mock_test
    @pytest.mark.parametrize("incident_id, task_id, task_name", [
        (2096, 0, "Determine if illegal activity is involved"),
        (2096, 0, "Ensure updated antivirus signatures are deployed")
    ])
    def test_close_task_by_name_success(self, circuits_app, incident_id, task_id, task_name):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_name": task_name
        }
        results = call_task_utils_close_task_function(circuits_app, function_params)
        assert (function_params["task_name"] == results["content"]["task_name"])

    @pytest.mark.mock_test
    @pytest.mark.parametrize("incident_id, task_id, task_name", [
        (2096, 0, "text")
    ])
    def test_close_task_failure(self, circuits_app, incident_id, task_id, task_name):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_name": task_name
        }

        with pytest.raises(ValueError) as err:
            call_task_utils_close_task_function(circuits_app, function_params)

            assert err.value.args[0] == u"Could not find task with name {}".format(function_params["task_name"])

    @pytest.mark.mock_test
    @pytest.mark.parametrize("incident_id, task_id, task_name, expected_results", [
        (2096, 2251301, "text", {"task_id": 2251301})
    ])
    def test_close_task_status(self, circuits_app, incident_id, task_id, task_name, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_name": task_name
        }
        results = call_task_utils_close_task_function(circuits_app, function_params)
        if not results["content"].get("status") and not results["content"].get("task"):
            pytest.xfail("Unsupported test. No task object or status found")
        assert (results["content"]["status"] == 'C')

    @pytest.mark.mock_test
    @pytest.mark.parametrize("incident_id, task_id, task_name", [
        (2096, 0, "Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ"),
        (2096, 0, " Й К Л М Н О П Р С Т ")
    ])
    def test_close_task_by_name_unicode(self, circuits_app, incident_id, task_id, task_name):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_name": task_name
        }
        results = call_task_utils_close_task_function(circuits_app, function_params)
        assert (function_params["task_name"] == results["content"]["task_name"])

    @pytest.mark.mock_test
    @pytest.mark.parametrize("incident_id, task_id, task_name, expected_results", [
        (2096, 2251218, "Η Θ Ι Κ Λ Μ Ν Ξ Ο Π Ρ", {"task_id": 2251218}),
        (2096, 2251216, " Й К Л М Н О П Р С Т ", {"task_id": 2251216})
    ])
    def test_close_task_by_id_unicode(self, circuits_app, incident_id, task_id, task_name, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incident_id": incident_id,
            "task_id": task_id,
            "task_name": task_name
        }
        results = call_task_utils_close_task_function(circuits_app, function_params)
        assert (expected_results["task_id"] == results["content"]["task_id"])
