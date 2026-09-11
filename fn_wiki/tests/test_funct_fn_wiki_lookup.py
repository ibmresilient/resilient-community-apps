# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_wiki"
FUNCTION_NAME = "fn_wiki_lookup"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_wiki_lookup_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_wiki_lookup", function_params)

    # Fire a message to the function
    circuits.manager.fire(evt)

    # circuits will fire an "exception" event if an exception is raised in the FunctionComponent
    # return this exception if it is raised
    exception_event = circuits.watcher.wait("exception", parent=None, timeout=timeout)

    if exception_event is not False:
        exception = exception_event.args[1]
        raise exception

    # else return the FunctionComponent's results
    else:
        event = circuits.watcher.wait("fn_wiki_lookup_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnWikiLookup:
    """ Tests for the fn_wiki_lookup function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_search_term = {
        "wiki_path": "wiki_lookup",
        "wiki_search_term": "line"
    }
    mock_search_results = ['line2', 'line3']

    mock_regex = {
        "wiki_path": "wiki_lookup",
        "wiki_search_term": "line[0123456789]+"
    }
    mock_regex_results = ['line2', 'line3']

    mock_not_found = {
        "wiki_path": "wiki_lookup",
        "wiki_search_term": "nadda"
    }
    mock_not_found_results = []

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_search_term, mock_search_results),
        (mock_regex, mock_regex_results),
        (mock_not_found, mock_not_found_results)
    ])
    def test_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_lookup_function(circuits_app, mock_inputs)
        assert(results['content'] == expected_results)
