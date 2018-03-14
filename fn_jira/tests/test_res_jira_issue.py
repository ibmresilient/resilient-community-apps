# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_jira"
FUNCTION_NAME = "jira_open_issue"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_jira_open_issue_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("jira_open_issue", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("jira_open_issue_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestJiraOpenIssue:
    """ Tests for the jira_open_issue function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incidentID, jira_project, jira_issuetype, jira_summary, jira_description, expected_result", [
        (1234, {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, "text", "text", {"value": "xyz"}),
        (4567, {"type": "text", "content": "line1\nline2"}, {"type": "text", "content": "line1\nline2"}, "text", "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incidentID, jira_project, jira_issuetype, jira_summary, jira_description, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = {
            "incidentID" : incidentID,
            "jira_project": jira_project,
            "jira_issuetype": jira_issuetype,
            "jira_summary": jira_summary,
            "jira_description": jira_description
        }
        result = call_jira_open_issue_function(circuits_app, function_params)
        assert result is not None