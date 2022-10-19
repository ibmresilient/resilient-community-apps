# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import get_mock_config, mocked_exchange_utils

PACKAGE_NAME = "fn_exchange"
FUNCTION_NAME = "exchange_get_mailbox_info"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_exchange_get_mailbox_info_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("exchange_get_mailbox_info", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("exchange_get_mailbox_info_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value

class TestExchangeGetMailboxInfo:
    """ Tests for the exchange_get_mailbox_info function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_exchange.components.exchange_get_mailbox_info.exchange_utils', side_effect=mocked_exchange_utils)
    @pytest.mark.parametrize("exchange_email, expected_results", [
        ("user@exch.com", {'email_address': 'user@exch.com', 'mailbox_type': 'Mailbox', 'name': 'User', 'routing_type': 'SMTP',
                   'success': True}),
    ])
    def test_success(self, mock_utils, exchange_email, circuits_app, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "exchange_email": exchange_email,
        }
        results = call_exchange_get_mailbox_info_function(circuits_app, function_params)
        assert(expected_results == results)

class TestExchangeGetMailboxInfoEmpMailbox:
    """ Tests for the exchange_get_mailbox_info function"""

    def setup_method(self):
        global config_data
        config_data = get_mock_config("empty_user@exch.com")

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_exchange.components.exchange_get_mailbox_info.exchange_utils', side_effect=mocked_exchange_utils)
    @pytest.mark.parametrize("exchange_email, expected_results", [
        ("empty_user@exch.com", {'success': False}),
    ])
    def test_success(self, mock_utils, exchange_email, circuits_app, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = {
            "exchange_email": exchange_email,
        }
        results = call_exchange_get_mailbox_info_function(circuits_app, function_params)
        assert(expected_results == results)