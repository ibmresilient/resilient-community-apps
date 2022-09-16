# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Test fn_bigfix_action_status function"""
from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_artifacts import mocked_bigfix_client

"""
Suite of tests to test fn_bigfix_action_status Resilient Function
"""

PACKAGE_NAME = "fn_bigfix"
FUNCTION_NAME = "fn_bigfix_action_status"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_bigfix_action_status_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_bigfix_action_status", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_bigfix_action_status_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnBigfixActionStatus:
    """ Tests for the fn_bigfix_action_status function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_bigfix.components.fn_bigfix_action_status.BigFixClient', side_effect=mocked_bigfix_client)
    @pytest.mark.parametrize("bigfix_action_id, expected_results_1, expected_results_2", [
        (123, "OK", "The action executed successfully."),
        (124, "OK", "The Fixlet which this action addresses is not relevant on this machine."),
        (125, "Failed", "The action failed.")
    ])
    def test_success(self, mock_get, circuits_app, bigfix_action_id, expected_results_1, expected_results_2):
        """ Tests for fn_bigfix_action_status using mocked data.  """

        keys = ["status", "status_message"]

        function_params = { 
            "bigfix_action_id": bigfix_action_id
        }
        results = call_fn_bigfix_action_status_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        assert(expected_results_1 == results["status"])
        assert(expected_results_2 == results["status_message"])