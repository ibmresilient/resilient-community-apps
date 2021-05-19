# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from .mock_artifacts import *

PACKAGE_NAME = "fn_zia"
FUNCTION_NAME = "funct_zia_add_to_allowlist"

# Read the mock configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_funct_zia_add_to_allowlist_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("funct_zia_add_to_allowlist", function_params)

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
        event = circuits.watcher.wait("funct_zia_add_to_allowlist_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFunctZiaAddToAllowlist:
    """ Tests for the funct_zia_add_to_allowlist function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_inputs_1 = {
        "zia_allowlisturls": "goodhost"
    }

    expected_results_1 = {"whitelistUrls": ["goodhost.com"]}

    mock_inputs_2 = {
        "zia_allowlisturls": "goodhost, 192.168.1.1"
    }

    expected_results_2 = {"whitelistUrls": ["192.168.1.1", "goodhost.com"]}

    @patch('fn_zia.components.funct_zia_add_to_allowlist.ZiaClient', side_effect=mocked_zia_client)
    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_inputs_1, expected_results_1),
        (mock_inputs_2, expected_results_2)
    ])
    def test_success(self, mock_cli, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]

        results = call_funct_zia_add_to_allowlist_function(circuits_app, mock_inputs)
        assert_keys_in(results, *keys)
        assert(expected_results == results["content"])
