# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Tests for fn_sep_assign_fingerprint_list_to_group function."""
from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_assign_fingerprint_list_to_group"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_sep_assign_fingerprint_list_to_group_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_assign_fingerprint_list_to_group", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_assign_fingerprint_list_to_group_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepAssignFingerprintListToGroup:
    """ Tests for the fn_sep_assign_fingerprint_list_to_group function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_assign_fingerprint_list_to_group.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_groupid, sep_fingerprintlist_id, expected_results", [
        ("114BA13D0946C25D49CE7D3A846CBEDB", "7992BAC1C36E46FDBCD95F7E5A063AFB", ""),
    ])
    def test_success(self, mock_put, circuits_app, sep_groupid, sep_fingerprintlist_id, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]

        function_params = { 
            "sep_groupid": sep_groupid,
            "sep_fingerprintlist_id": sep_fingerprintlist_id
        }
        results = call_fn_sep_assign_fingerprint_list_to_group_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert expected_results == content