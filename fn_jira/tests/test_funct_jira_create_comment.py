# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from data import mock_data
from mock import patch

PACKAGE_NAME = "fn_jira"
FUNCTION_NAME = "jira_create_comment"

# Read the default configuration-data section from the package
config_data = mock_data.get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def call_jira_create_comment_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("jira_create_comment", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("jira_create_comment_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value

class TestJiraCreateComment:
    """ Tests for the jira_create_comment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "incident_id": 2230,
        "jira_label": "my-server",
        "jira_issue_id": "",
        "jira_comment": "404 error is thrown",
        "task_id": 214
    }

    expected_results_1 = {"value": "xyz"}

    client = mock_data.mock_init()
    print("f")

    @patch("fn_jira.components.jira_create_comment.AppCommon", side_effect=mock_data.mock_init())
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_jira_create_comment_function(circuits_app, mock_inputs)
        assert(expected_results == results)
