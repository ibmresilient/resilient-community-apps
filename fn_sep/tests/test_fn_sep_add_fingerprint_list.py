# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Tests for fn_sep_add_fingerprint_list function."""
from __future__ import print_function
import pytest
from mock import patch
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_add_fingerprint_list"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_sep_add_fingerprint_list_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_add_fingerprint_list", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_add_fingerprint_list_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepAddFingerprintList:
    """ Tests for the fn_sep_add_fingerprint_list function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_add_fingerprint_list.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value, expected_results", [
        ("Blacklist", "Hash of type Malware MD5 Hash", "A9B4B7160946C25D24B6AA458EF5557F", "582F9B6E0CC4C1DBBD772AAAF088CB3A",
         "B5F9985ED6C449A6905A0D570A5733FC")
    ])
    def test_success(self, mock_post, circuits_app, sep_fingerprintlist_name, sep_description, sep_domainid, sep_hash_value, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_2 = ["id"]

        function_params = {
            "sep_fingerprintlist_name": sep_fingerprintlist_name,
            "sep_description": sep_description,
            "sep_domainid": sep_domainid,
            "sep_hash_value": sep_hash_value
        }
        results = call_fn_sep_add_fingerprint_list_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results["content"]
        assert_keys_in(content, *keys_2)
        assert expected_results == content["id"]