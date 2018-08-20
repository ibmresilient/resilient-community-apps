# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_computers"

# Mock configuration-data section
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj


def call_fn_amp_get_computers_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_computers", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_computers_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetComputers:
    """ Tests for the fn_amp_get_computers function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_computers.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_group_guid, amp_limit, amp_hostname, amp_internal_ip, amp_external_ip, "
                             "expected_results_1, expected_results_2", [
        (None, None, None, None, None, "v1.2.0", 4)
    ])
    def test_success(self, mock_get, circuits_app, amp_group_guid, amp_limit, amp_hostname, amp_internal_ip,
                     amp_external_ip, expected_results_1, expected_results_2):
        """ Test for classifiers 'classifiers' using mocked data.  """

        keys = ["computers", "query_execution_time"]
        keys_a = ["data", "metadata"]
        keys_a_d = ["operating_system", "connector_guid", "connector_version", "hostname", "active", "links"]

        function_params = {
            "amp_group_guid": amp_group_guid,
            "amp_limit": amp_limit,
            "amp_hostname": amp_hostname,
            "amp_internal_ip": amp_internal_ip,
            "amp_external_ip": amp_external_ip
        }
        results = call_fn_amp_get_computers_function(circuits_app, function_params)
        assert expected_results_1 == results["computers"]["version"]
        assert_keys_in(results, *keys)
        assert (expected_results_2 == len(results["computers"]["data"]))
        activity = results["computers"]
        assert_keys_in(activity, *keys_a)
        data = results["computers"]["data"]
        for d in data:
            assert_keys_in(d, *keys_a_d)

