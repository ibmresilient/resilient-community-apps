# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_slack"
FUNCTION_NAME = "slack_post_attachment"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_slack_post_attachment_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("slack_post_attachment", function_params)

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
        event = circuits.watcher.wait("slack_post_attachment_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSlackPostAttachment:
    """ Tests for the slack_post_attachment function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "attachment_id": 123,
        "task_id": 123,
        "slack_text": "sample text",
        "slack_participant_emails": "sample text",
        "artifact_id": 123,
        "incident_id": 123,
        "slack_channel": "sample text",
        "slack_is_channel_private": True
    }

    expected_results_1 = {"value": "xyz"}


    @patch('fn_slack.components.slack_post_attachment.SlackUtils.get_users_info', return_value = "")
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.get_channel_users_list')
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.get_permalink', return_value = "")
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.get_ts_from_file_upload_results')
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.slack_post_attachment')
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.get_file_attachment_data', return_value = ("", ""))
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.find_user_ids_based_on_email', return_value = [])
    @patch('fn_slack.components.slack_post_attachment.SlackUtils.find_or_create_channel', return_value = ("", True))
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, mock_find_or_create_channel, mock_user_id_list, mock_data, mock_post, mock_upload, mock_get_permalink, mock_user_list, mock_user_info, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_slack_post_attachment_function(circuits_app, mock_inputs)
        assert("channel" in results)
