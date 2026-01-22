# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult

PACKAGE_NAME = "fn_wiki"
FUNCTION_NAME = "fn_wiki_create_update"

# Read the default configuration-data section from the package
config_data = get_config_data(PACKAGE_NAME)

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def call_fn_wiki_create_update_function(circuits, function_params, timeout=5):
    # Create the submitTestFunction event
    evt = SubmitTestFunction("fn_wiki_create_update", function_params)

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
        event = circuits.watcher.wait("fn_wiki_create_update_result", parent=evt, timeout=timeout)
        assert event
        assert isinstance(event.kwargs["result"], FunctionResult)
        pytest.wait_for(event, "complete", True)
        return event.kwargs["result"].value


class TestFnWikiCreateUpdate:
    """ Tests for the fn_wiki_create_update function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    mock_fail_path = {
        "wiki_path": None,
        "wiki_body": "sample text",
        "wiki_create_if_missing": False
    }

    mock_fail_page_not_found = {
        "wiki_path": "not found",
        "wiki_body": "sample text",
        "wiki_create_if_missing": False,
    }

    mock_fail_parent_not_found = {
        "wiki_path": "parent not found/new page",
        "wiki_body": "sample text",
        "wiki_create_if_missing": False
    }


    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_fail_path, None),
        (mock_fail_parent_not_found, None),
    ])
    def test_fail_update(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        with pytest.raises(ValueError):
            results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
            assert(results['success'] == False)
            assert(results['reason'])

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_fail_page_not_found, None)
    ])
    def test_page_not_found(self, circuits_app, mock_inputs, expected_results):
        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'] == False)
        assert(results['reason'] == 'Unable to find page with title: not found')

    mock_success_title = {
        "wiki_path": "ΣΤ",
        "wiki_body": "ΣΤ",
        "wiki_create_if_missing": True
    }

    mock_success_w_parent_title = {
        "wiki_path": "ΣΤ3/new3",
        "wiki_body": "new3",
        "wiki_create_if_missing": True
    }


    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_success_title, None),
        (mock_success_w_parent_title, None),
    ])
    def test_create_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'])


    mock_success_update_title = {
        "wiki_path": "parent1/json2",
        "wiki_body": "new3 ΣΤ3",
        "wiki_create_if_missing": False
    }


    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_success_update_title, None)
    ])
    def test_update_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'])

    
    mock_success_update_parent_title = {
        "wiki_path": "ΣΤ3/ΣΤ4",
        "wiki_body": "ΣΤ4",
        "wiki_create_if_missing": True
    }

    mock_success_update_parent_subparent = {
        "wiki_path": "parent1/json2/ΣΤ5",
        "wiki_body": "ΣΤ5",
        "wiki_create_if_missing": True
    }


    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_success_update_parent_title, None),
        (mock_success_update_parent_subparent, None)
    ])
    def test_update_parent_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'])
