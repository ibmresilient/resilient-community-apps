# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2025. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from data import mock_data
from unittest.mock import patch

FUNCTION_NAME = "jira_transition_issue"

# Read the default configuration-data section from the package
config_data = mock_data.get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_jira_transition_issue_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("jira_transition_issue", function_params)

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
        event = circuits.watcher.wait("jira_transition_issue_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestJiraTransitionIssue:
    """ Tests for the jira_transition_issue function """

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(mock_data.PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "jira_comment": "Closed in IBM SOAR\n\nResolution: Done\n",
        "jira_fields": "{  }",
        "jira_transition_id": "Done",
        "jira_label": "my-server",
        "jira_issue_id": "JRA-46"
    }

    expected_results_1 = "Done"

    @pytest.mark.parametrize("mock_inputs, expected_results", [(mock_inputs_1, expected_results_1)])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_jira.components.jira_transition_issue.AppCommon.get_jira_client") as patch_transition:
            patch_transition.return_value = mock_data.mock_init()
            results = call_jira_transition_issue_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
