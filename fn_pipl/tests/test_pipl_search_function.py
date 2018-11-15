# -*- coding: utf-8 -*-
"""Tests using pytest_resilient_circuits"""

from __future__ import print_function
import pytest
from resilient_circuits.util import get_config_data, get_function_definition
from resilient_circuits import SubmitTestFunction, FunctionResult
from test_helper import get_mock_config

try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

PACKAGE_NAME = "fn_pipl"
FUNCTION_NAME = "pipl_search_function"

# Read the default configuration-data section from the package
config_data = get_mock_config()

# Provide a simulation of the Resilient REST API (uncomment to connect to a real appliance)
resilient_mock = "pytest_resilient_circuits.BasicResilientMock"


def mocked_requests_get(*args, **kwargs):
    class MockResponse:
        """
        A mock class intended to mock the entire Response attribute for a requests.
        """
        def __init__(self, http_status_code, raw_json, persons_count, error):
            self.http_status_code = http_status_code
            self.raw_json = raw_json
            self.persons_count = persons_count
            self.error = error

    if kwargs.get("success") and kwargs.get("no_match"):
        return MockResponse(200, '{}', 0, None)
    elif kwargs.get("success") and not kwargs.get("definite"):
        return MockResponse(200, '{"possible_persons": [{"@id": "id1"}, {"@id": "id2"}]}', 2, None)
    elif kwargs.get("success") and kwargs.get("definite"):
        return MockResponse(200, '{"person": {"@id": "id1"}}', 1, None)
    else:
        return MockResponse(400, None, None, "Bad Request")


def call_pipl_search_function_function(circuits, function_params, timeout=10):
    # Fire a message to the function
    evt = SubmitTestFunction("pipl_search_function", function_params)
    circuits.manager.fire(evt)
    event = circuits.watcher.wait("pipl_search_function_result", parent=evt, timeout=timeout)
    assert event
    assert isinstance(event.kwargs["result"], FunctionResult)
    pytest.wait_for(event, "complete", True)
    return event.kwargs["result"].value


class TestPiplSearchFunction:
    """ Tests for the pipl_search_function function"""

    def test_function_definition(self):
        """ Test that the package provides customization_data that defines the function """
        func = get_function_definition(PACKAGE_NAME, FUNCTION_NAME)
        assert func is not None

    @pytest.mark.parametrize("inputs,results_success,results_pipl_response,results_person_list", [
        ({"pipl_artifact_type": "Email Sender", "pipl_artifact_value": "clark.kent@example.com"},
         True, "possible person matches", [{"@id": "id1"}, {"@id": "id2"}])
    ])
    @patch("fn_pipl.components.pipl_search_function.SearchAPIRequest.send")
    def test_success_possible_matches(self, mocked_api_call, circuits_app, inputs, results_success, results_pipl_response, results_person_list):
        """ Test calling with sample values for the parameters """

        function_params = inputs

        # Replace the return value of our mock_session with a custom function
        mocked_api_call.return_value = mocked_requests_get(success=True)

        # Fire the function with mocked functionality
        results = call_pipl_search_function_function(circuits_app, function_params)
        assert results.get("success") == results_success
        assert results.get("pipl_response") == results_pipl_response
        assert results.get("person_list") == results_person_list

    @pytest.mark.parametrize("inputs,results_success,results_pipl_response,results_person_list", [
        ({"pipl_artifact_type": "Email Sender", "pipl_artifact_value": "clark.kent@example.com"},
         True, "definite match", [{"@id": "id1"}])
    ])
    @patch("fn_pipl.components.pipl_search_function.SearchAPIRequest.send")
    def test_success_definite_match(self, mocked_api_call, circuits_app, inputs, results_success, results_pipl_response, results_person_list):
        """ Test calling with sample values for the parameters """

        function_params = inputs

        # Replace the return value of our mock_session with a custom function
        mocked_api_call.return_value = mocked_requests_get(success=True, definite=True)

        # Fire the function with mocked functionality
        results = call_pipl_search_function_function(circuits_app, function_params)
        assert results.get("success") == results_success
        assert results.get("pipl_response") == results_pipl_response
        assert results.get("person_list") == results_person_list

    @pytest.mark.parametrize("inputs,results_success,results_pipl_response,results_person_list", [
        ({"pipl_artifact_type": "Email Sender", "pipl_artifact_value": "clark.kent@example.com"},
         True, "no match", [])
    ])
    @patch("fn_pipl.components.pipl_search_function.SearchAPIRequest.send")
    def test_success_no_match(self, mocked_api_call, circuits_app, inputs, results_success, results_pipl_response, results_person_list):
        """ Test calling with sample values for the parameters """

        function_params = inputs

        # Replace the return value of our mock_session with a custom function
        mocked_api_call.return_value = mocked_requests_get(success=True, definite=True, no_match=True)

        # Fire the function with mocked functionality
        results = call_pipl_search_function_function(circuits_app, function_params)
        assert results.get("success") == results_success
        assert results.get("pipl_response") == results_pipl_response
        assert results.get("person_list") == results_person_list

    @pytest.mark.parametrize("inputs", [
        ({"pipl_artifact_type": "Email Sender", "pipl_artifact_value": "clark.kent@example.com"})
    ])
    @patch("fn_pipl.components.pipl_search_function.SearchAPIRequest.send")
    def test_fail(self, mocked_api_call, circuits_app, inputs):
        """ Test calling with sample values for the parameters """

        function_params = inputs

        # Replace the return value of our mock_session with a custom function
        mocked_api_call.return_value = mocked_requests_get(success=False)

        # Fire the function with mocked functionality
        evt = SubmitTestFunction("pipl_search_function", function_params)
        circuits_app.manager.fire(evt)
        try:
            event = circuits_app.watcher.wait("pipl_search_function_result", parent=evt, timeout=3)
            assert event is False
        except ValueError:
            assert True
