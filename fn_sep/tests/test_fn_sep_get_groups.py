# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2024. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use

"""Tests for fn_sep_get_groups function."""
from __future__ import print_function
import pytest
from unittest.mock import patch
from resilient_circuits.util import get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from mock_artifacts import mocked_sep_client, get_mock_config

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_get_groups"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_fn_sep_get_groups_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_sep_get_groups", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_sep_get_groups_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSepGetGroups:
    """ Tests for the fn_sep_get_groups function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('fn_sep.components.fn_sep_get_groups.Sepclient', side_effect=mocked_sep_client)
    @pytest.mark.parametrize("sep_domain, sep_fullpathname, sep_mode, sep_pageindex, sep_pagesize, sep_order, sep_sort, expected_results", [
        (None, None, None, None, None, None, None, 2)
    ])
    def test_success(self, mock_get, circuits_app, sep_domain, sep_fullpathname, sep_mode, sep_pageindex, sep_pagesize, sep_order, sep_sort, expected_results):
        """ Test calling with sample values for the parameters """

        keys = ["content", "inputs", "metrics", "raw", "reason", "success", "version"]
        keys_2 = ["content", "firstPage", "lastPage", "number", "numberOfElements", "size", "sort", "totalElements",
                  "totalPages"]

        function_params = {
            "sep_domain": sep_domain,
            "sep_fullpathname": sep_fullpathname,
            "sep_mode": sep_mode,
            "sep_pageindex": sep_pageindex,
            "sep_pagesize": sep_pagesize,
            "sep_order": sep_order,
            "sep_sort": sep_sort
        }
        results = call_fn_sep_get_groups_function(circuits_app, function_params)
        assert_keys_in(results, *keys)
        content = results.get("content", {})
        assert_keys_in(content, *keys_2)
        assert expected_results == content.get("numberOfElements")
        assert expected_results == content.get("totalElements")
        assert expected_results == len(content.get("content"))
