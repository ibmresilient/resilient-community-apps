# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from data import mock_data
from unittest.mock import patch

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
        "jira_comment": "404 error is thrown"
    }

    expected_results_1 = {
        "self": "https://example.com/rest/api/2/issue/10055/comment/10350",
        "id": "10350",
        "author": {
            "self": "https://example.com/rest/api/2/user?accountId=123456",
            "accountId": "123456",
            "emailAddress": "test@example.com",
            "displayName": "test",
            "active": True,
            "timeZone": "America/New_York",
            "accountType": "atlassian"
        },
        "body": "404 error is thrown",
        "updateAuthor": {
            "self": "https://example.com/rest/api/2/user?accountId=123456",
            "accountId": "123456",
            "emailAddress": "test@example.com",
            "displayName": "test",
            "active": True,
            "timeZone": "America/New_York",
            "accountType": "atlassian"
        },
        "created": "2023-01-31T09:52:58.464-0500",
        "updated": "2023-01-31T09:52:58.464-0500",
        "jsdPublic": True,
        "jira_url": "https://example.com"
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """
        with patch("fn_jira.components.jira_create_comment.AppCommon.get_jira_client") as patch_add:
            patch_add.return_value = mock_data.mock_init()
            results = call_jira_create_comment_function(circuits_app, mock_inputs)
            assert(expected_results == results.get("content"))
