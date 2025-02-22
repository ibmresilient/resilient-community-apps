# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from requests_mock import mock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_slack"
FUNCTION_NAME = "slack_archive_channel"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_slack_archive_channel_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("slack_archive_channel", function_params)

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
        event = circuits.watcher.wait("slack_archive_channel_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestSlackArchiveChannel:
    """ Tests for the slack_archive_channel function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "task_id": 123,
        "incident_id": 123
    }

    expected_results_1 = {"channel": "xyz"}

    @patch('fn_slack.components.slack_archive_channel.SlackUtils.archive_channel')
    @patch('fn_slack.components.slack_archive_channel.SlackUtils.save_conversation_history_as_attachment')
    @patch('fn_slack.components.slack_archive_channel.SlackUtils.get_channel_complete_history')
    @patch('fn_slack.components.slack_archive_channel.SlackUtils.slack_post_message')
    @patch('fn_slack.components.slack_archive_channel.SlackUtils.get_channel')
    @patch('fn_slack.components.slack_archive_channel.SlackUtils.find_channel')
    @patch('fn_slack.components.slack_archive_channel.slack_channel_name_datatable_lookup', return_value = {"channel" : "xyz"})
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1)
    ])
    def test_success(self, mock_dt_lookup, mock_name, mock_get_channel, mock_post_message, mock_get_channel_history, mock_save_history, mock_archive, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_slack_archive_channel_function(circuits_app, mock_inputs)
        assert("channel" in results)
