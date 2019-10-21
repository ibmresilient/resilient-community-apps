# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_teams"
FUNCTION_NAME = "teams_post_message"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_teams_post_message_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("teams_post_message", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("teams_post_message_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestTeamsPostMessage:
    """ Tests for the teams_post_message function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, task_id, teams_webhook, teams_text, teams_mrkdown, expected_results", [
        (123, None, None, "text", True, {"value": "xyz"}),
        (123, 1234, None, "text", True, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, incident_id, task_id, teams_webhook, teams_text, teams_mrkdown, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "task_id": task_id,
            "teams_webhook": teams_webhook,
            "teams_text": teams_text,
            "teams_mrkdown": teams_mrkdown
        }
        results = call_teams_post_message_function(circuits_app, function_params)
        assert(expected_results == results)