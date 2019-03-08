# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_sep"
FUNCTION_NAME = "fn_sep_add_fingerprint_list"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


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

    @pytest.mark.parametrize("sep_data, set_description, sep_domainid, sep_hashtype, sep_name, expected_results", [
        ("text", "text", "text", 'MD5', "text", {"value": "xyz"}),
        ("text", "text", "text", 'MD5', "text", {"value": "xyz"})
    ])
    def test_success(self, circuits_app, sep_data, set_description, sep_domainid, sep_hashtype, sep_name, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "sep_data": sep_data,
            "set_description": set_description,
            "sep_domainid": sep_domainid,
            "sep_hashtype": sep_hashtype,
            "sep_name": sep_name
        }
        results = call_fn_sep_add_fingerprint_list_function(circuits_app, function_params)
        assert(expected_results == results)