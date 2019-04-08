# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2018. All Rights Reserved.

"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_elasticsearch"
FUNCTION_NAME = "fn_elasticsearch_query"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_elasticsearch_query_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("fn_elasticsearch_query", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("fn_elasticsearch_query_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestFnElasticsearchQuery:
    """ Tests for the fn_elasticsearch_query function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None
    @pytest.mark.parametrize("index, doc_type, es_query, expected_results", [
        ("", "", {"type": "text", "content": '{ "query": { "match_all": {} } }'}, {"value": "xyz"}),
        ("test_data", "", {"type": "text", "content": '{ "query": { "match_all": {} } }'}, {"value": "xyz"})
    ])
    def test_success(self, circuits_app, index, doc_type, es_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "index": index,
            "doc_type": doc_type,
            "es_query": es_query
        }
        results = call_fn_elasticsearch_query_function(circuits_app, function_params)
        assert(results)

    @pytest.mark.parametrize("index, doc_type, es_query, expected_results", [
        ("badIndex", "", {"type": "text", "content": '{ "query": { "match_all": {} } }'}, {"value": "xyz"}),
        ("BadIndex2", "badType", {"type": "text", "content": '{ "query": { "match_all": {} } }'}, {"value": "xyz"})
    ])
    def test_failure(self, circuits_app, index, doc_type, es_query, expected_results):
        """ Test calling with sample values for the parameters """
        function_params = { 
            "index": index,
            "doc_type": doc_type,
            "es_query": es_query
        }
        results = call_fn_elasticsearch_query_function(circuits_app, function_params)

        assert(results["query_results"] is None )