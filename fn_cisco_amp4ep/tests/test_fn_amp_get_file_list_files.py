# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_amp_client, get_mock_config

PACKAGE_NAME = "fn_cisco_amp4ep"
FUNCTION_NAME = "fn_amp_get_file_list_files"

# Mock configuration-data section
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_amp_get_file_list_files_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_amp_get_file_list_files", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_amp_get_file_list_files_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnAmpGetFileListFiles:
    """ Tests for the fn_amp_get_file_list_files function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_cisco_amp4ep.components.fn_amp_get_file_list_files.Ampclient', side_effect=mocked_amp_client)
    @pytest.mark.parametrize("amp_file_list_guid, amp_file_sha256, amp_limit, amp_offset, expected_results_1, "
                             "expected_results_2, expected_results_3", [
        ("9710a198-b95a-462a-b184-9e688968fd94", None, None, None, "v1.2.0", 1, 10),
        ("9710a198-b95a-462a-b184-9e688968fd94", "e93faae7706644387cd3383aaf1bd9919f9f441acce498f15391eb60eb54288b",
         None, None, "v1.2.0", 1, "Created by entering SHA-256 via Public api.")
    ])
    def test_success(self, mock_get, circuits_app, amp_file_list_guid, amp_file_sha256, amp_limit, amp_offset,
                     expected_results_1, expected_results_2, expected_results_3):
        """ Test calling with sample values for the parameters """

        keys = ["response", "query_execution_time"]
        keys_flf = ["data", "metadata"]
        if amp_file_sha256 is None:
            keys_flf_d = ["guid", "items", "name", "policies"]
            keys_flf_d_p = ["guid", "name", "links"]
        else:
            keys_flf_d = ["links", "sha256", "source"]

        function_params = {
            "amp_file_list_guid": amp_file_list_guid,
            "amp_file_sha256": amp_file_sha256,
            "amp_limit": amp_limit,
            "amp_offset": amp_offset
        }
        results = call_fn_amp_get_file_list_files_function(circuits_app, function_params)
        assert expected_results_1 == results["response"]["version"]
        assert_keys_in(results, *keys)
        file_list_files = results["response"]
        assert_keys_in(file_list_files, *keys_flf)
        if amp_file_sha256 is None:
            assert expected_results_2 == file_list_files["metadata"]["results"]["total"]
            data = file_list_files["data"]
            assert_keys_in(data, *keys_flf_d)
            policies = data["policies"]
            assert expected_results_3 == len(policies)
            for p in policies:
                assert_keys_in(p, *keys_flf_d_p)
        else:
            assert expected_results_2 == len(file_list_files["metadata"]["links"])
            data = file_list_files["data"]
            assert_keys_in(data, *keys_flf_d)
            assert expected_results_3 == file_list_files["data"]["source"]
