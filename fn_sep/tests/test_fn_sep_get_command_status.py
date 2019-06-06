# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_get_command_status"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_sep_get_command_status_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_get_command_status", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_get_command_status_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepGetCommandStatus:
    """ Tests for the fn_sep_get_command_status function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_get_command_status.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_incident_id, sep_commandid, sep_order, sep_pageindex, sep_pagesize, sep_sort, "
                             "sep_status_type, sep_matching_endpoint_ids, expected_results_1, expected_results_2, "
                             "expected_results_3", [
        (123, "3FEB081B2A144479A32980272C9C1E23", None, None, None, "text", "scan", False, 4, 1, 0)
    ])
    def test_success(self, mock_get, circuits_app, sep_incident_id, sep_commandid, sep_order, sep_pageindex,
                     sep_pagesize, sep_sort, sep_status_type, sep_matching_endpoint_ids, expected_results_1,
                     expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_2 = ["overall_command_state", "total_ep_count", "total_match_count", "total_match_ep_count",
                  "total_not_completed", "total_remediation_count", "total_remediation_ep_count"]

        function_params = {
            "sep_incident_id": sep_incident_id,
            "sep_commandid": sep_commandid,
            "sep_order": sep_order,
            "sep_pageindex": sep_pageindex,
            "sep_pagesize": sep_pagesize,
            "sep_sort": sep_sort,
            "sep_status_type": sep_status_type,
            "sep_matching_endpoint_ids": sep_matching_endpoint_ids
        }
        results = call_fn_sep_get_command_status_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert_keys_in(content, *keys_2)
        assert expected_results_1 == content["total_ep_count"]
        assert expected_results_2 == content["total_not_completed"]
        assert expected_results_3 == content["total_match_count"]
