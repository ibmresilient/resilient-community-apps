# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_delete_file_list_files"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_amp_delete_file_list_files_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_delete_file_list_files", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_delete_file_list_files_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpDeleteFileListFiles:
    """ Tests for the fn_amp_delete_file_list_files function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_delete_file_list_files.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize(
        "amp_file_list_guid, amp_file_sha256, expected_results_1, expected_results_2, expected_results_3", [
            ("e773a9eb-296c-40df-98d8-bed46322589d", "8a68fc7ffd25e12cb92e3cb8a51bf219cada775baef73991bee384b3656fa284", "v1.2.0", 1, 0)
    ])
    def test_success(self, mock_get, circuits_app, amp_file_list_guid, amp_file_sha256, expected_results_1, expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_df = ["data", "metadata"]

        function_params = {
            "amp_file_list_guid": amp_file_list_guid,
            "amp_file_sha256": amp_file_sha256
        }
        results = call_fn_amp_delete_file_list_files_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        delete_file_list_files = results["response"]
        assert_keys_in(delete_file_list_files, *keys_df)
        assert expected_results_2 == len(delete_file_list_files["metadata"]["links"])
        data = delete_file_list_files["data"]
        assert expected_results_3 == len(data)

