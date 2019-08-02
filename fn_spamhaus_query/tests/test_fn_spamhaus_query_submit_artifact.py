# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import *

PACKAGE_NAME = "fn_spamhaus_query"
FUNCTION_NAME = "fn_spamhaus_query_submit_artifact"

# Read Configuration data from test_helper file

config_data = get_mock_config_data()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_spamhaus_query_submit_artifact_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_spamhaus_query_submit_artifact", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_spamhaus_query_submit_artifact_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnSpamhausQuerySubmitArtifact:
    """ Tests for the fn_spamhaus_query_submit_artifact function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    # Getting mock input data from test_helper file
    mock_input = get_mock_input_data_dict()
    spamhaus_query_string = mock_input.get('spamhaus_query_string')
    spamhaus_search_resource = mock_input.get('spamhaus_search_resource')

    @pytest.mark.parametrize("spamhaus_query_string, spamhaus_search_resource",
                             [(spamhaus_query_string, spamhaus_search_resource)])
    def test_invalid_api_key(self, circuits_app, spamhaus_query_string, spamhaus_search_resource):
        """ Test calling with sample values for the parameters """

        function_params = {
            "spamhaus_query_string": spamhaus_query_string,
            "spamhaus_search_resource": spamhaus_search_resource
        }
        results = call_fn_spamhaus_query_submit_artifact_function(circuits_app, function_params)
        response_code = results.get('content').get('status')
        assert response_code in [200, 404]

    @pytest.mark.parametrize("spamhaus_query_string, spamhaus_search_resource",
                             [(spamhaus_query_string, spamhaus_search_resource)])
    def test_function_output_results(self, circuits_app, spamhaus_query_string, spamhaus_search_resource):
        """ Test calling with sample values for the parameters """

        function_params = {
            "spamhaus_query_string": spamhaus_query_string,
            "spamhaus_search_resource": spamhaus_search_resource
        }
        results = call_fn_spamhaus_query_submit_artifact_function(circuits_app, function_params)
        response_data = results.get('content')
        expected_results_dict = get_mock_output_data_dict()
        assert response_data.get('status') == expected_results_dict.get('content').get('status')
        assert results.get('inputs').get('spamhaus_search_resource') == expected_results_dict.get('inputs').get(
            'spamhaus_search_resource')
        assert results.get('inputs').get('spamhaus_query_string') == expected_results_dict.get('inputs').get(
            'spamhaus_query_string')
        assert response_data.get('is_in_blocklist') == expected_results_dict.get('content').get('is_in_blocklist')
        assert response_data.get(1002).get('dataset') == expected_results_dict.get('content').get(1002).get('dataset')
