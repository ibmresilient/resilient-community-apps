# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Tests for fn_sep_scan_endpoints function."""
from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_scan_endpoints"

# Read the default configuration-data section from the package
config_data = get_mock_config()

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_sep_scan_endpoints_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_scan_endpoints", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_scan_endpoints_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepScanEndpoints:
    """ Tests for the fn_sep_scan_endpoints function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_scan_endpoints.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_group_ids, sep_computer_ids, sep_scan_type, sep_file_path, sep_sha256, sep_sha1, "
                             "sep_md5, sep_description, sep_scan_action, expected_results_1, expected_results_2", [
        (None, "236A7100A9FE9DC50A4F1AC2819C158E", 'QUICK_SCAN', "C:\\temp\\eicar.zip", None, None, None, "EOC scan",
         None, "0F0CBDD7EDFF4634B23FA11F5AB81FFC", "BB37F78894DB451B8E8921EC127667A3"),

    ])
    def test_success(self, mock_post, circuits_app, sep_group_ids, sep_computer_ids, sep_scan_type, sep_file_path,
                     sep_sha256, sep_sha1, sep_md5, sep_description, sep_scan_action, expected_results_1, expected_results_2):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_2 = ["commandID_computer", "commandID_group"]

        function_params = {
            "sep_group_ids": sep_group_ids,
            "sep_computer_ids": sep_computer_ids,
            "sep_scan_type": sep_scan_type,
            "sep_file_path": sep_file_path,
            "sep_sha256": sep_sha256,
            "sep_sha1": sep_sha1,
            "sep_md5": sep_md5,
            "sep_description": sep_description,
            "sep_scan_action": sep_scan_action
        }
        results = call_fn_sep_scan_endpoints_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert_keys_in(content, *keys_2)
        assert expected_results_1 == content["commandID_computer"]
        assert expected_results_2 == content["commandID_group"]