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

    mock_fail_title = {
        "wiki_parent_title_or_id": None,
        "wiki_title_or_id": "sample text",
        "wiki_body": "sample text",
        "wiki_create_if_missing": False
    }

    mock_fail_id = {
        "wiki_parent_title_or_id": None,
        "wiki_title_or_id": "99",
        "wiki_body": "sample text",
        "wiki_create_if_missing": False,
    }

    mock_fail_parent_title = {
        "wiki_parent_title_or_id": "sample text",
        "wiki_title_or_id": "sample text",
        "wiki_body": "sample text",
        "wiki_create_if_missing": False
    }

    mock_fail_parent_id = {
        "wiki_parent_title_or_id": "99",
        "wiki_title_or_id": "sample text",
        "wiki_body": "sample text",
        "wiki_create_if_missing": True
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_fail_title, None),
        (mock_fail_id, None),
        (mock_fail_parent_title, None),
        (mock_fail_parent_id, None),
    ])
    def test_fail_update(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'] == False)
        assert(results['reason'])


    mock_success_title = {
        "wiki_parent_title_or_id": None,
        "wiki_title_or_id": "ΣΤ",
        "wiki_body": "ΣΤ",
        "wiki_create_if_missing": True
    }

    mock_success_w_parent_title = {
        "wiki_parent_title_or_id": "parent1",
        "wiki_title_or_id": "new3",
        "wiki_body": "ΣΤ",
        "wiki_create_if_missing": True
    }

    mock_success_w_parent_id = {
        "wiki_parent_title_or_id": "1",
        "wiki_title_or_id": "new3",
        "wiki_body": "ΣΤ",
        "wiki_create_if_missing": True
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_success_title, None),
        (mock_success_w_parent_title, None),
        (mock_success_w_parent_id, None),
    ])
    def test_create_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'])


    mock_success_update_title = {
        "wiki_parent_title_or_id": None,
        "wiki_title_or_id": "ΣΤ3",
        "wiki_body": "ΣΤ3",
        "wiki_create_if_missing": False
    }

    mock_success_update_id = {
        "wiki_parent_title_or_id": None,
        "wiki_title_or_id": "2",
        "wiki_body": "ΣΤ3",
        "wiki_create_if_missing": False
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_success_update_title, None),
        (mock_success_update_id, None)
    ])
    def test_update_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'])

    
    mock_success_update_parent_title = {
        "wiki_parent_title_or_id": "parent1",
        "wiki_title_or_id": "2",
        "wiki_body": "ΣΤ3",
        "wiki_create_if_missing": False
    }

    mock_success_update_parent_title = {
        "wiki_parent_title_or_id": "1",
        "wiki_title_or_id": "json2",
        "wiki_body": "ΣΤ3",
        "wiki_create_if_missing": False
    }

    @pytest.mark.parametrize("mock_inputs, expected_results", [
        (mock_success_update_title, None),
        (mock_success_update_id, None)
    ])
    def test_update_parent_success(self, circuits_app, mock_inputs, expected_results):
        """ Test calling with sample values for the parameters """

        results = call_fn_wiki_create_update_function(circuits_app, mock_inputs)
        assert(results['success'])
