# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
import json
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_mcafee"
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


def remove_dynamic_values(response):
    # Verify system_list exists then delete it
    assert "system_list" in response
    del response["system_list"]

    # Verify Prevalence exists then delete it
    assert "Prevalence" in response["Enterprise"]["Attributes"]
    del response["Enterprise"]["Attributes"]["Prevalence"]

    # Verify Enterprise Size exists then delete it
    assert "Enterprise Size" in response["Enterprise"]["Attributes"]
    del response["Enterprise"]["Attributes"]["Enterprise Size"]

    return response


class TestMcafeeTieSearchHash:
    """ Tests for the mcafee_tie_search_hash function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("mcafee_tie_hash_type, mcafee_tie_hash, expected_result", [
        ("md5", "30CB8BA19E19B42701CDB3627D6F4023", json.load(open("md5_hash_search_expected.txt"))),
        ("sha1", "C61AC5FE73D50BD41D0CAD1A43C471925E7DDCD4", json.load(open("sha1_hash_search_expected.txt"))),
        ("sha256", "A8B03AD33BC6D7A7F376B943F763EEDD1CDAF125D012F9018F2F56678AE67EA4",
         json.load(open("sha256_hash_search_expected.txt")))

    ])
    def test_success(self, circuits_app, mcafee_tie_hash_type, mcafee_tie_hash, expected_result):
        """ Test calling with sample values for the parameters """
        function_params = {
            "mcafee_tie_hash_type": mcafee_tie_hash_type,
            "mcafee_tie_hash": mcafee_tie_hash
        }
        result = call_mcafee_tie_search_hash_function(circuits_app, function_params)
        result = remove_dynamic_values(result)
        assert(expected_result == result)
