# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.
# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_cve_search"
FUNCTION_NAME = "function_cve"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_function_cve_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("function_cve", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("function_cve_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFunctionCve:
    """ Tests for the function_cve function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("cve_search_data, cve_search_criteria, cve_id, cve_vendor, cve_product, cve_published_date_from, cve_published_date_to, expected_results", [
        ("text", "text", "text", "text", "text", 1518480000000, 1518480000000, {"value": "xyz"}),
        ("text", "text", "text", "text", "text", 1518480000000, 1518480000000, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, cve_search_data, cve_search_criteria, cve_id, cve_vendor, cve_product, cve_published_date_from, cve_published_date_to, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "cve_search_data": cve_search_data,
            "cve_search_criteria": cve_search_criteria,
            "cve_id": cve_id,
            "cve_vendor": cve_vendor,
            "cve_product": cve_product,
            "cve_published_date_from": cve_published_date_from,
            "cve_published_date_to": cve_published_date_to
        }
        results = call_function_cve_function(circuits_app, function_params)
        assert(expected_results == results)