# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import json
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee_tie_functions"
FUNCTION_NAME = "mcafee_tie_search_hash"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_mcafee_tie_search_hash_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    circuits.manager.fire(SubmitTestFunction("mcafee_tie_search_hash", function_params))
    event = circuits.watcher.wait("mcafee_tie_search_hash_result", timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestMcafeeTieSearchHash:
    """ Tests for the mcafee_tie_search_hash function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("mcafee_tie_hash_type, mcafee_tie_hash, expected_result", [
        ("md5", "0E4D13CC9AF04CC64B68FC38FE0A0DAC", json.load(open("md5_hash_search_response.txt"))),
        ("sha1", "84132654FBA9669952EF116ACCA9273362806512", {"value": "xyz"}),
        ("sha256", "766A6A19991AAFE91BFAE3DA931041FA9BFD2B3BC181E2124940DCF98E906FF8", {"value": "xyz"})

    ])
    def test_success(self, circuits_app, mcafee_tie_hash_type, mcafee_tie_hash, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = {
            "mcafee_tie_hash_type": mcafee_tie_hash_type,
            "mcafee_tie_hash": mcafee_tie_hash
        }
        result = call_mcafee_tie_search_hash_function(circuits_app, function_params)
        assert(expected_result == result)
