# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_exchange"
FUNCTION_NAME = "exchange_create_meeting"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_exchange_create_meeting_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("exchange_create_meeting", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("exchange_create_meeting_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestExchangeCreateMeeting:
    """ Tests for the exchange_create_meeting function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("exchange_email, exchange_meeting_start_time, exchange_meeting_end_time, exchange_meeting_subject, exchange_message_body, exchange_required_attendees, exchange_optional_attendees, expected_results", [
        ("text", 1518367008000, 1518367008000, "text", "text", "text", "text", {"value": "xyz"}),
        ("text", 1518367008000, 1518367008000, "text", "text", "text", "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, exchange_email, exchange_meeting_start_time, exchange_meeting_end_time, exchange_meeting_subject, exchange_message_body, exchange_required_attendees, exchange_optional_attendees, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "exchange_email": exchange_email,
            "exchange_meeting_start_time": exchange_meeting_start_time,
            "exchange_meeting_end_time": exchange_meeting_end_time,
            "exchange_meeting_subject": exchange_meeting_subject,
            "exchange_message_body": exchange_message_body,
            "exchange_required_attendees": exchange_required_attendees,
            "exchange_optional_attendees": exchange_optional_attendees
        }
        results = call_exchange_create_meeting_function(circuits_app, function_params)
        assert(expected_results == results)