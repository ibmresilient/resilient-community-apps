# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import get_mock_config, send_emails, connect_to_account

PACKAGE_NAME = "fn_exchange"
FUNCTION_NAME = "exchange_send_email"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_exchange_send_email_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("exchange_send_email", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("exchange_send_email_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestExchangeSendEmail:
    """ Tests for the exchange_send_email function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
    @pytest.mark.livetest
    @patch('fn_exchange.lib.exchange_utils.Message', side_effect=send_emails)
    @patch('fn_exchange.lib.exchange_utils.exchange_interface.connect_to_account', side_effect=connect_to_account)
    @pytest.mark.parametrize("exchange_email, exchange_message_subject, exchange_message_body, exchange_email_recipients, expected_results", [
        ("user@exch.com", "Example Subject", "Testing", "jdoe@exch.com", {'msg_body': 'Testing', 'recipients': 'jdoe@exch.com', 'sender': 'user@exch.com', 'msg_subject': 'Example Subject'})
    ])
    def test_success(self, mock_send_email, mock_connect_account, circuits_app, exchange_email, exchange_message_subject, exchange_message_body, exchange_email_recipients, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "exchange_email": exchange_email,
            "exchange_message_subject": exchange_message_subject,
            "exchange_message_body": exchange_message_body,
            "exchange_email_recipients": exchange_email_recipients}
        results = call_exchange_send_email_function(circuits_app, function_params)
        assert(expected_results == results.get("content"))