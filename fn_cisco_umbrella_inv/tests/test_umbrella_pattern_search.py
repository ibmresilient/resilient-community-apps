# -*- coding: utf-8 -*-
# pragma pylint: disable=unused-argument, no-self-use

# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock import patch

from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from  mock_umbrella import  mocked_response

PACKAGE_NAME = "fn_cisco_umbrella_inv"
FUNCTION_NAME = "umbrella_pattern_search"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"

def assert_keys_in(json_obj, *keys):
    for key in keys:
        assert key in json_obj

def call_umbrella_pattern_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("umbrella_pattern_search", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("umbrella_pattern_search_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUmbrellaPatternSearch:
    """ Tests for the umbrella_pattern_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @patch('investigate.Investigate.get', side_effect=mocked_response)
    @pytest.mark.parametrize("umbinv_regex, umbinv_start_epoch, umbinv_start_relative, umbinv_limit, umbinv_include_category", [
        ("paypal.*", None, "-30days", 10, True)
    ])
    def test_pattern_search(self, mock_get, circuits_app, umbinv_regex, umbinv_start_epoch, umbinv_start_relative, umbinv_limit, umbinv_include_category):
        """ Test pattern_search using mocked response. """

        keys_outer = ["matches", "limit", "totalResults", "expression", "moreDataAvailable"]
        keys_match = ["name", "securityCategories", "firstSeen", "name", "firstSeenISO"]
        function_params = {
            "umbinv_regex": umbinv_regex,
            "umbinv_start_epoch": umbinv_start_epoch,
            "umbinv_start_relative": umbinv_start_relative,
            "umbinv_limit": umbinv_limit,
            "umbinv_include_category": umbinv_include_category
        }
        results = call_umbrella_pattern_search_function(circuits_app, function_params)
        search_matches = results["search_matches"]
        assert_keys_in(search_matches, *keys_outer)
        match = search_matches["matches"].pop(0)
        assert_keys_in(match, *keys_match)
