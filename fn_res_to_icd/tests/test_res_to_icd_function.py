# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2019. All Rights Reserved.
# pragma pylint: disable=unused-argument, no-self-use 
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_res_to_icd"
FUNCTION_NAME = "res_to_icd_function"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_res_to_icd_function_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("res_to_icd_function", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("res_to_icd_function_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestResToIcdFunction:
    """ Tests for the res_to_icd_function function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("incident_id, expected_results", [
        (2097, {'success':True}),
        (2098, {'success':True})
    ])
    def test_success(self, circuits_app, incident_id, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "incident_id": incident_id
        }
        results = call_res_to_icd_function_function(circuits_app, function_params)
        assert(expected_results['success'] == results['success'])