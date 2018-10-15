# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_groups"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_amp_get_groups_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_groups", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_groups_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetGroups:
    """ Tests for the fn_amp_get_groups function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_groups.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_group_guid, amp_group_name, amp_limit, expected_results_1, expected_results_2,"
                             "expected_results_3", [
        ("4060cf94-26e5-4176-8dea-cd3d0b68d8bc", None, 1, "v1.2.0", 2, "Audit Group"),
        (None, "Audit", 1, "v1.2.0", 1, "Audit Group for FireAMP API Docs")
    ])
    def test_success(self, mock_get, circuits_app, amp_group_guid, amp_group_name, amp_limit, expected_results_1,
                     expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_gg = ["data", "metadata"]
        keys_gg_d = ["description", "guid", "links", "name", "source"]

        function_params = {
            "amp_group_guid": amp_group_guid,
            "amp_group_name": amp_group_name,
            "amp_limit": amp_limit
        }
        results = call_fn_amp_get_groups_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        assert(expected_results_2 == results["response"]["metadata"]["results"]["total"])
        get_groups = results["response"]
        assert_keys_in(get_groups, *keys_gg)
        data = results["response"]["data"]
        for d in data:
            assert_keys_in(d, *keys_gg_d)
        assert expected_results_3 == get_groups["data"][0]["description"]