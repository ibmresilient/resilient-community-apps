# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Tests for fn_sep_quarantine_endpoints function."""
from __future__ import print_function
import pytest
from unittest.mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config
PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_quarantine_endpoints"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_sep_quarantine_endpoints_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_quarantine_endpoints", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_quarantine_endpoints_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepQuarantineEndpoints:
    """ Tests for the fn_sep_quarantine_endpoints function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_quarantine_endpoints.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_group_ids, sep_computer_ids, sep_hardwarekey, sep_undo, expected_results", [
        ("E5E684A6092E5BB90F46E84BB6F35BBC", "01ECF4E8092E5BB91E4D52E45C3ABE4D", "8DACE2559C1C951E09CC0BF71D973BB7", False, "09114E42730A479993DD6D94CF9CAA53")
    ])
    def test_success(self, mock_post, circuits_app, sep_group_ids, sep_computer_ids, sep_hardwarekey, sep_undo, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_2 = ["commandID_computer", "commandID_group"]

        function_params = {
            "sep_group_ids": sep_group_ids,
            "sep_computer_ids": sep_computer_ids,
            "sep_hardwarekey": sep_hardwarekey,
            "sep_undo": sep_undo
        }
        results = call_fn_sep_quarantine_endpoints_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results.get("content", {})
        assert_keys_in(content, *keys_2)
        assert expected_results == content.get("commandID_computer")
