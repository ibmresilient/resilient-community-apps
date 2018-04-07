# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from mock_search import SearchMock
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_utilities"
FUNCTION_NAME = "utilities_resilient_search"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = SearchMock


def call_utilities_resilient_search_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction(FUNCTION_NAME, function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("{}_result".format(FUNCTION_NAME), parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestUtilitiesResilientSearch:
    """ Tests for the utilities_resilient_search function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("resilient_search_template, resilient_search_query, expected_results", [
        ({"type": "text", "content": '{"something":1}'}, "query", ["results"])
    ])
    def test_success(self, circuits_app, resilient_search_template, resilient_search_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "resilient_search_template": resilient_search_template,
            "resilient_search_query": resilient_search_query
        }
        results = call_utilities_resilient_search_function(circuits_app, function_params)
        for key in expected_results:
            assert(key in results)
