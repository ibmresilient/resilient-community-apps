# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

"""
pytest --resilient_app_config=/path/to/app.config -vv test_teams_post_message.py

Note: This requires that 'selftest' is defined in app.config
"""

PACKAGE_NAME = "fn_teams"
FUNCTION_NAME = "teams_post_message"

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

    # Read the default configuration-data section from the package
    config_data = get_config_data(PACKAGE_NAME)

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, task_id, teams_channel, teams_payload, teams_mrkdown, expected_results", [
        (123, None, "selftest", '{"title": "titleЀЄЏ"}', False, None),
        (123, None, "selftest", '{"title": "title", "summary": "summaryЀЄЏ"}', False, None),
        (123, None, "selftest", '{"title": "title", "summary": "summaryЀЄЏ", "sections": [{"title": "sectionЀЄЏ"}]}', False, None),
        (123, None, "selftest", '{"title": "title", "summary": "summaryЀЄЏ", "sections": [{"title": "section1", "text": "section textЀЄЏ"}]}', False, None),
        (123, None, "selftest", '{"title": "title", "summary": "summaryЀЄЏ", "sections": [{"title": "section1", "text": "section text", "facts":[{"name": "fact1", "value": "valueЀЄЏ"}]}]}', False, None),
        (123, None, "selftest", '{"title": "title", "summary": "summaryЀЄЏ", "sections": [{"title": "section1", "text": "section text", "facts":[{"name": "fact1", "value": "value1"}, {"name": "fact2", "value": "value2"}]}]}', False, None),
        (123, None, "selftest", '{"title": "title", "summary": "<u>summaryЀЄЏ</u>", "sections": [{"title": "section1", "text": "section text", "facts":[{"name": "fact1", "value": "value1"}, {"name": "fact2", "value": "value2"}]},{"title": "section2", "text": "section text", "facts":[{"name": "fact1", "value": "value1"}, {"name": "fact2", "value": "value2"}]}]}', True, None)
    ])
    def test_success(self, circuits_app, incident_id, task_id, teams_channel, teams_payload, teams_mrkdown, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id,
            "task_id": task_id,
            "teams_channel": teams_channel,
            "teams_payload": teams_payload,
            "teams_mrkdown": teams_mrkdown
        }

        results = call_teams_post_message_function(circuits_app, function_params)
        assert results['success']
